import toml
import json
from typing import Dict, Any, Optional
from .base import Agent


class AgentManager:
    """Manager for specialized agents."""

    _instance = None

    def __new__(cls):
        """Ensure only one instance is created (singleton pattern)."""
        if cls._instance is None:
            cls._instance = super(AgentManager, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    @staticmethod
    def load_agents_from_config(config_path: str) -> list:
        """
        Load agent definitions from a TOML or JSON configuration file.

        Args:
            config_path: Path to the configuration file.

        Returns:
            List of agent dictionaries.
        """
        try:
            if config_path.endswith(".toml"):
                with open(config_path, "r") as file:
                    config = toml.load(file)
            elif config_path.endswith(".json"):
                with open(config_path, "r") as file:
                    config = json.load(file)
            else:
                raise ValueError(
                    "Unsupported configuration file format. Use TOML or JSON."
                )
        except FileNotFoundError:
            raise FileNotFoundError(f"Configuration file not found: {config_path}")
        except (toml.TomlDecodeError, json.JSONDecodeError):
            raise ValueError("Invalid configuration file format.")

        return config.get("agents", [])

    def __init__(self, config_path: Optional[str] = None):
        """Initialize the agent manager."""
        if not self._initialized:
            self.agents = {}
            self.current_agent = None
            self.handoff_history = []
            self._initialized = True

    @classmethod
    def get_instance(cls):
        """Get the singleton instance of AgentManager."""
        if cls._instance is None:
            cls._instance = AgentManager()
        return cls._instance

    def register_agent(self, agent: Agent):
        """
        Register an agent with the manager.

        Args:
            agent: The agent to register
        """
        self.agents[agent.name] = agent

    def select_agent(self, agent_name: str) -> bool:
        """
        Select an agent by name.

        Args:
            agent_name: The name of the agent to select

        Returns:
            True if the agent was selected, False otherwise
        """
        if agent_name in self.agents:
            # Get the new agent
            new_agent = self.agents[agent_name]

            # If there was a previous agent, deactivate it
            if self.current_agent:
                self.current_agent.deactivate()

            # Set the new agent as current
            self.current_agent = new_agent

            if not self.current_agent.custom_system_prompt:
                self.current_agent.set_custom_system_prompt(
                    self.get_handoff_system_prompt()
                )
            # Activate the new agent
            self.current_agent.activate()

            return True
        return False

    def get_agent(self, agent_name: str) -> Optional[Agent]:
        """
        Get an agent by name.

        Args:
            agent_name: The name of the agent to get

        Returns:
            The agent, or None if not found
        """
        return self.agents.get(agent_name)

    def get_current_agent(self) -> Agent:
        """
        Get the current agent.

        Returns:
            The current agent, or None if no agent is selected
        """
        if not self.current_agent:
            raise ValueError("Current agent is not set")
        return self.current_agent

    def perform_handoff(
        self, target_agent_name: str, task: str, context_summary: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Perform a handoff to another agent.

        Args:
            target_agent_name: The name of the agent to hand off to
            reason: The reason for the handoff
            context_summary: Optional summary of the conversation context

        Returns:
            A dictionary with the result of the handoff
        """
        if target_agent_name not in self.agents:
            return {
                "success": False,
                "error": f"Agent '{target_agent_name}' not found",
                "available_agents": list(self.agents.keys()),
            }

        source_agent = self.current_agent

        # Record the handoff
        handoff_record = {
            "from": source_agent.name if source_agent else "None",
            "to": target_agent_name,
            "reason": task,
            "context_summary": context_summary,
        }
        self.handoff_history.append(handoff_record)

        # Set the new current agent
        self.select_agent(target_agent_name)

        return {"success": True, "handoff": handoff_record}

    def update_llm_service(self, llm_service):
        """
        Update the LLM service for all agents.

        Args:
            llm_service: The new LLM service to use
        """
        if self.current_agent:
            # Deactivate the current agent
            self.current_agent.deactivate()

            # Update the LLM service for the current agent
            self.current_agent.update_llm_service(llm_service)

            # Reactivate the agent with the new LLM service
            self.current_agent.activate()

            # Update all other agents' LLM service but keep them deactivated
            for name, agent in self.agents.items():
                if agent != self.current_agent:
                    agent.update_llm_service(llm_service)

    def get_handoff_system_prompt(self):
        """
        Generate a handoff section for the system prompt based on available agents.

        Returns:
            str: A formatted string containing handoff instructions and available agents
        """
        if not self.agents:
            return ""

        # Build agent descriptions
        agent_descriptions = []
        for name, agent in self.agents.items():
            agent_desc = ""
            if hasattr(agent, "description") and agent.description:
                agent_desc = f"- {name}: {agent.description}"
            else:
                agent_desc = f"- {name}"
            if len(agent.tools) > 0:
                agent_desc += f" - available tools: {', '.join(agent.tools)}"
            agent_descriptions.append(agent_desc)

        handoff_prompt = (
            "## Agent Handoff\n\n"
            "You must hand off the conversation to another specialized agent when task is not in your specialized. "
            "Only set `report_back` to `true` when you need further processing based on target_agent findings"
            "To perform a handoff, use handoff tool with target_agent, task, context_summary arguments. Example:\n\n"
            """{'id': 'random id', 'name': 'handoff', 'input': {'target_agent': 'AgentName', 'task': 'Task need to be done', 'report_back': 'true/false', 'context_summary': 'Summary of the context'}, 'type': 'function' }\n"""
            f"Available agents:\n{chr(10).join(agent_descriptions)}\n"
        )

        return handoff_prompt
