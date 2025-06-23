from typing import Any


class MessageEventHandler:
    """Handles message-related events in the chat UI."""

    def __init__(self, chat_window):
        from AgentCrew.modules.gui import ChatWindow

        if isinstance(chat_window, ChatWindow):
            self.chat_window = chat_window
        self.thinking_content = ""

    def handle_event(self, event: str, data: Any):
        """Handle a message-related event."""
        if event == "response_chunk":
            self.handle_response_chunk(data)
        elif event == "user_message_created":
            self.handle_user_message_created(data)
        elif event == "response_completed" or event == "assistant_message_added":
            self.handle_response_completed(data)
        elif event == "thinking_started":
            self.handle_thinking_started(data)
        elif event == "thinking_chunk":
            self.handle_thinking_chunk(data)
        elif event == "thinking_completed":
            self.handle_thinking_completed()
        elif event == "user_context_request":
            self.handle_user_context_request()

    def handle_response_chunk(self, data):
        """Handle response chunks with smooth streaming."""
        chunk_text, full_response = data

        if full_response.strip():
            # Create bubble immediately if needed
            if (
                self.chat_window.expecting_response
                and self.chat_window.current_response_bubble is None
            ):
                self.chat_window.current_response_bubble = (
                    self.chat_window.chat_components.append_message("", False)
                )

            # Use the individual chunk for smooth streaming
            if self.chat_window.current_response_bubble:
                print(chunk_text)
                self.chat_window.current_response_bubble.add_streaming_chunk(chunk_text)

    def handle_user_message_created(self, data):
        """Handle user message creation."""
        if self.chat_window.current_user_bubble:
            self.chat_window.current_user_bubble.message_index = (
                self.chat_window.message_handler.current_user_input_idx
            )
            self.chat_window.current_user_bubble = None

    def handle_response_completed(self, data):
        """Handle response completion."""
        if self.chat_window.current_response_bubble:
            # Finalize streaming and ensure full content is rendered
            self.chat_window.current_response_bubble._finalize_streaming()
            self.chat_window.current_response_bubble.message_index = (
                len(self.chat_window.message_handler.streamline_messages) - 1
            )

        # # Reset response expectation flag
        # self.chat_window.expecting_response = False
        # self.chat_window.current_response_bubble = None

    def handle_thinking_started(self, data):
        """Handle thinking process started."""
        agent_name = data
        self.chat_window.chat_components.add_system_message(
            f"💭 {agent_name.upper()}'s thinking process started"
        )

        # Create a new thinking bubble
        self.chat_window.current_thinking_bubble = (
            self.chat_window.chat_components.append_thinking_message(" ", agent_name)
        )
        self.thinking_content = ""  # Initialize thinking content
        # self.chat_window.thinking_buffer = ""  # Initialize thinking buffer

    def handle_thinking_chunk(self, data):
        """Handle a chunk of the thinking process."""
        chunk = data
        # Use smooth streaming for thinking chunks too
        if self.chat_window.current_thinking_bubble:
            self.chat_window.current_thinking_bubble.add_streaming_chunk(chunk)

    def handle_thinking_completed(self):
        """Handle thinking process completion."""
        self.chat_window.display_status_message("Thinking completed.")
        # self.chat_window.chat_scroll.verticalScrollBar().setValue(
        #     self.chat_window.chat_scroll.verticalScrollBar().maximum()
        # )
        # Finalize thinking stream if active
        if self.chat_window.current_thinking_bubble:
            self.chat_window.current_thinking_bubble._finalize_streaming()
        # Reset thinking bubble reference
        self.chat_window.current_thinking_bubble = None

    def handle_user_context_request(self):
        """Handle user context request."""
        self.chat_window.chat_components.add_system_message("Refreshing my memory...")
