from datetime import datetime
import os
from typing import Dict, Any, List, Optional
from AgentCrew.modules.llm.base import BaseLLMService
from AgentCrew.modules.llm.message import MessageTransformer
from AgentCrew.modules.agents.base import BaseAgent, MessageType
from AgentCrew.modules import logger


class LocalAgent(BaseAgent):
    """Base class for all specialized agents."""

    def __init__(
        self,
        name: str,
        description: str,
        llm_service: BaseLLMService,
        services: Dict[str, Any],
        tools: List[str],
        temperature: Optional[float] = None,
        is_remoting_mode: bool = False,
    ):
        """
        Initialize a new agent.

        Args:
            name: The name of the agent
            description: A description of the agent's capabilities
            llm_service: The LLM service to use for this agent
            services: Dictionary of available services
        """
        super().__init__(name, description)
        # self.name = name
        # self.description = description
        self.llm = llm_service
        self.temperature = temperature
        self.services = services
        self.tools: List[str] = tools  # List of tool names that the agent needs
        self.system_prompt = None
        self.custom_system_prompt = None
        self.tool_prompts = []
        self.is_remoting_mode = is_remoting_mode
        # self.history = []
        # self.shared_context_pool: Dict[str, List[int]] = {}
        # Store tool definitions in the same format as ToolRegistry
        self.tool_definitions = {}  # {tool_name: (definition_func, handler_factory, service_instance)}
        self.registered_tools = (
            set()
        )  # Set of tool names that are registered with the LLM

    def _extract_tool_name(self, tool_def: Any) -> str:
        """
        Extract tool name from definition regardless of format.

        Args:
            tool_def: The tool definition

        Returns:
            The name of the tool

        Raises:
            ValueError: If the tool name cannot be extracted
        """
        if "name" in tool_def:
            return tool_def["name"]
        elif "function" in tool_def and "name" in tool_def["function"]:
            return tool_def["function"]["name"]
        else:
            raise ValueError("Could not extract tool name from definition")

    def register_tools(self):
        """
        Register tools for this agent using the services dictionary.
        """

        if self.services.get("agent_manager") and not self.is_remoting_mode:
            from AgentCrew.modules.agents.tools.transfer import (
                register as register_transfer,
            )

            register_transfer(self.services["agent_manager"], self)
        for tool_name in self.tools:
            if self.services and tool_name in self.services:
                service = self.services[tool_name]
                if service:
                    if tool_name == "memory":
                        from AgentCrew.modules.memory.tool import (
                            register as register_memory,
                            adaptive_instruction_prompt,
                        )

                        register_memory(
                            service, self.services.get("context_persistent", None), self
                        )
                        self.tool_prompts.append(adaptive_instruction_prompt())
                    elif tool_name == "clipboard":
                        from AgentCrew.modules.clipboard.tool import (
                            register as register_clipboard,
                        )

                        register_clipboard(service, self)
                    elif tool_name == "code_analysis":
                        from AgentCrew.modules.code_analysis.tool import (
                            register as register_code_analysis,
                        )

                        register_code_analysis(service, self)
                    elif tool_name == "web_search":
                        from AgentCrew.modules.web_search.tool import (
                            register as register_web_search,
                        )

                        register_web_search(service, self)
                    elif tool_name == "image_generation":
                        from AgentCrew.modules.image_generation.tool import (
                            register as register_image_generation,
                        )

                        register_image_generation(service, self)
                    else:
                        logger.warning(f"⚠️ Tool {tool_name} not found in services")
            else:
                logger.warning(
                    f"⚠️ Service {tool_name} not available for tool registration"
                )

    def register_tool(self, definition_func, handler_factory, service_instance=None):
        """
        Register a tool with this agent.

        Args:
            definition_func: Function that returns tool definition given a provider or direct definition
            handler_factory: Function that creates a handler function or direct handler
            service_instance: Service instance needed by the handler (optional)
        """
        # Get the tool definition to extract the name
        tool_def = definition_func() if callable(definition_func) else definition_func
        tool_name = self._extract_tool_name(tool_def)

        # Store the definition function, handler factory, and service instance
        self.tool_definitions[tool_name] = (
            definition_func,
            handler_factory,
            service_instance,
        )

        # If the agent is active, register the tool with the LLM immediately
        if self.is_active and self.llm:
            # Get provider-specific definition
            provider = getattr(self.llm, "provider_name", None)
            if callable(definition_func) and provider:
                try:
                    tool_def = definition_func(provider)
                except TypeError:
                    # If definition_func doesn't accept provider argument
                    tool_def = definition_func()
            else:
                tool_def = definition_func

            # Get handler function
            if callable(handler_factory):
                handler = (
                    handler_factory(service_instance)
                    if service_instance
                    else handler_factory()
                )
            else:
                handler = handler_factory

            # Register with LLM
            self.llm.register_tool(tool_def, handler)
            self.registered_tools.add(tool_name)

    def set_system_prompt(self, prompt: str):
        """
        Set the system prompt for this agent.

        Args:
            prompt: The system prompt
        """
        self.system_prompt = prompt.replace(
            "{current_date}", datetime.today().strftime("%A, %d/%m/%Y")
        ).replace("{cwd}", os.getcwd())

    def set_custom_system_prompt(self, prompt: str):
        """
        Set the system prompt for this agent.

        Args:
            prompt: The system prompt
        """
        self.custom_system_prompt = prompt

    def get_system_prompt(self) -> str:
        """
        Get the system prompt for this agent.

        Returns:
            The system prompt
        """
        return self.system_prompt or ""

    def activate(self):
        """
        Activate this agent by registering all tools with the LLM service.

        Returns:
            True if activation was successful, False otherwise
        """
        if not self.llm:
            return False

        if self.is_active:
            return True  # Already active

        self.register_tools()
        self._register_tools_with_llm()
        system_prompt = self.get_system_prompt()
        if self.custom_system_prompt:
            system_prompt = system_prompt + "\n---\n\n" + self.custom_system_prompt
        if self.tool_prompts:
            system_prompt = system_prompt + "\n---\n\n" + "\n".join(self.tool_prompts)

        self.llm.set_system_prompt(system_prompt)
        self.llm.temperature = self.temperature if self.temperature is not None else 0.4
        self.is_active = True
        return True

    def deactivate(self):
        """
        Deactivate this agent by clearing all tools from the LLM service.

        Returns:
            True if deactivation was successful, False otherwise
        """
        if not self.llm:
            return False

        self._clear_tools_from_llm()
        self.tool_definitions = {}
        self.is_active = False
        return True

    def _register_tools_with_llm(self):
        """
        Register all of this agent's tools with the LLM service.
        """
        if not self.llm:
            return

        # Clear existing tools first to avoid duplicates
        self._clear_tools_from_llm()

        # Get the provider name if available
        provider = getattr(self.llm, "provider_name", None)

        for tool_name, (
            definition_func,
            handler_factory,
            service_instance,
        ) in self.tool_definitions.items():
            try:
                # Get provider-specific definition if possible
                if callable(definition_func) and provider:
                    try:
                        tool_def = definition_func(provider)
                    except TypeError:
                        # If definition_func doesn't accept provider argument
                        tool_def = definition_func()
                else:
                    tool_def = definition_func

                # Get handler function
                if callable(handler_factory):
                    handler = (
                        handler_factory(service_instance)
                        if service_instance
                        else handler_factory()
                    )
                else:
                    handler = handler_factory

                # Register with LLM
                self.llm.register_tool(tool_def, handler)
                self.registered_tools.add(tool_name)
            except Exception as e:
                logger.error(f"Error registering tool {tool_name}: {e}")

    def _clear_tools_from_llm(self):
        """
        Clear all tools from the LLM service.
        """
        if self.llm:
            self.llm.clear_tools()
            self.registered_tools.clear()
            # Note: We don't clear self.tool_definitions as we want to keep the definitions

    @property
    def std_history(self):
        return MessageTransformer.standardize_messages(
            self.history, self.llm.provider_name, self.name
        )

    def get_provider(self) -> str:
        return self.llm.provider_name

    def is_streaming(self) -> bool:
        return self.llm.is_stream

    def format_message(
        self, message_type: MessageType, message_data: Dict[str, Any]
    ) -> Optional[Dict[str, Any]]:
        if message_type == MessageType.Assistant:
            return self.llm.format_assistant_message(
                message_data.get("message", ""), message_data.get("tool_uses", None)
            )
        elif message_type == MessageType.Thinking:
            return self.llm.format_thinking_message(message_data.get("thinking", None))
        elif message_type == MessageType.ToolResult:
            return self.llm.format_tool_result(
                message_data.get("tool_use", {}),
                message_data.get("tool_result", ""),
                message_data.get("is_error", False),
            )
        elif message_type == MessageType.FileContent:
            return self.llm.process_file_for_message(message_data.get("file_uri", ""))

    def configure_think(self, think_setting):
        self.llm.set_think(think_setting)

    async def execute_tool_call(self, tool_name: str, tool_input: Dict) -> Any:
        return await self.llm.execute_tool(tool_name, tool_input)

    def calculate_usage_cost(self, input_tokens, output_tokens) -> float:
        return self.llm.calculate_cost(input_tokens, output_tokens)

    def get_model(self) -> str:
        return f"{self.llm.provider_name}/{self.llm.model}"

    def update_llm_service(self, new_llm_service: BaseLLMService) -> bool:
        """
        Update the LLM service used by this agent.

        Args:
            new_llm_service: The new LLM service to use

        Returns:
            True if the update was successful, False otherwise
        """
        was_active = self.is_active

        # Deactivate with the current LLM if active
        if was_active:
            self.deactivate()

        # Get the current provider
        current_provider = self.llm.provider_name

        # If we're switching providers, convert messages
        if current_provider != new_llm_service.provider_name:
            # Standardize messages from current provider
            std_messages = MessageTransformer.standardize_messages(
                self.history, current_provider, self.name
            )
            # Convert to new provider format
            self.history = MessageTransformer.convert_messages(
                std_messages, new_llm_service.provider_name
            )

        # Update the LLM service
        self.llm = new_llm_service

        # Reactivate with the new LLM if it was active before
        if was_active:
            self.activate()

        return True

    async def process_messages(self, messages: Optional[List[Dict[str, Any]]] = None):
        """
        Process messages using this agent.

        Args:
            messages: The messages to process

        Returns:
            The processed messages with the agent's response
        """
        from AgentCrew.modules.memory.context_persistent import (
            ContextPersistenceService,
        )

        assistant_response = ""
        self.tool_uses = []
        self.input_tokens_usage = 0
        self.output_tokens_usage = 0
        # Ensure the first message is a system message with the agent's prompt
        if not messages:
            final_messages = list(self.history)
        else:
            final_messages = list(messages)
            print(messages)
        if "context_persistent" in self.services and isinstance(
            self.services["context_persistent"], ContextPersistenceService
        ):
            adaptive_behaviors = self.services[
                "context_persistent"
            ].get_adaptive_behaviors(self.name)
            if (
                len(adaptive_behaviors.keys()) > 0
                and final_messages[-1].get("role", "assistant") == "user"
            ):
                # adaptive behaviors are only added if the last message is from the user
                if isinstance(final_messages[-1]["content"], str) or (
                    isinstance(final_messages[-1]["content"], list)
                    and final_messages[-1]["content"][0].get("type") != "tool_result"
                ):
                    adaptive_text = ""
                    for key, value in adaptive_behaviors.items():
                        adaptive_text += f"- {value} (id:{key})\n"

                    adaptive_messages = {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": f'MANDATORY: Check stored adaptive behaviors before responding. When "when...do..." conditions match, execute those behaviors immediately—they override default logic. Ask for clarification if uncertain which behaviors apply. List of adaptive behaviors: \n{adaptive_text}.\n END OF ADAPTABLE BEHAVIORS.\n\n',
                            }
                        ],
                    }
                    final_messages.insert(-1, adaptive_messages)
        try:
            async with await self.llm.stream_assistant_response(
                final_messages
            ) as stream:
                async for chunk in stream:
                    # Process the chunk using the LLM service
                    (
                        assistant_response,
                        tool_uses,
                        chunk_input_tokens,
                        chunk_output_tokens,
                        chunk_text,
                        thinking_chunk,
                    ) = self.llm.process_stream_chunk(
                        chunk, assistant_response, self.tool_uses
                    )
                    if tool_uses:
                        self.tool_uses = tool_uses
                    if chunk_input_tokens > 0:
                        self.input_tokens_usage = chunk_input_tokens
                    if chunk_output_tokens > 0:
                        self.output_tokens_usage = chunk_output_tokens
                    yield (assistant_response, chunk_text, thinking_chunk)
        except GeneratorExit as e:
            logger.warning(f"Stream processing interrupted: {e}")
        finally:
            return

    def get_process_result(self):
        return (self.tool_uses, self.input_tokens_usage, self.output_tokens_usage)
