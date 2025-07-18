from typing import Any

from PySide6.QtWidgets import QApplication


class MessageEventHandler:
    """Handles message-related events in the chat UI."""

    def __init__(self, chat_window):
        from AgentCrew.modules.gui import ChatWindow

        if isinstance(chat_window, ChatWindow):
            self.chat_window = chat_window
        self.chat_window.thinking_content = ""
        self.chunk_buffer_queue = []
        self.think_buffer_queue = []

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
        self.chunk_buffer_queue.extend(list(chunk_text))

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
            self.chat_window.current_response_bubble.add_streaming_chunk(
                self.chunk_buffer_queue
            )

    def handle_user_message_created(self, data):
        """Handle user message creation."""
        if self.chat_window.current_user_bubble:
            self.chat_window.current_user_bubble.message_index = (
                self.chat_window.message_handler.current_user_input_idx
            )
            self.chat_window.current_user_bubble = None
            self.chat_window.chat_scroll.verticalScrollBar().setValue(
                self.chat_window.chat_scroll.verticalScrollBar().maximum()
            )

    def handle_response_completed(self, data):
        """Handle response completion."""
        self.chunk_buffer_queue = []
        if self.chat_window.current_response_bubble:
            # Finalize streaming and ensure full content is rendered
            self.chat_window.current_response_bubble.raw_text_buffer = data
            self.chat_window.current_response_bubble.raw_text = data
            self.chat_window.current_response_bubble._finalize_streaming()
            self.chat_window.current_response_bubble.message_index = (
                len(self.chat_window.message_handler.streamline_messages) - 1
            )
        QApplication.processEvents()
        self.chat_window.chat_scroll.repaint()

    def handle_thinking_started(self, data):
        """Handle thinking process started."""
        self.think_buffer_queue = []
        agent_name = data
        self.chat_window.chat_components.add_system_message(
            f"💭 {agent_name.upper()}'s thinking process started"
        )

        # Create a new thinking bubble
        self.chat_window.current_thinking_bubble = (
            self.chat_window.chat_components.append_thinking_message("", agent_name)
        )
        self.chat_window.thinking_content = ""  # Initialize thinking content

    def handle_thinking_chunk(self, chunk):
        """Handle a chunk of the thinking process."""
        self.think_buffer_queue.extend(list(chunk))
        self.chat_window.thinking_content += chunk
        # Use smooth streaming for thinking chunks too
        if self.chat_window.current_thinking_bubble:
            self.chat_window.current_thinking_bubble.add_streaming_chunk(
                self.think_buffer_queue
            )

    def handle_thinking_completed(self):
        """Handle thinking process completion."""
        self.chat_window.display_status_message("Thinking completed.")
        # Finalize thinking stream if active
        if self.chat_window.current_thinking_bubble:
            self.chat_window.current_thinking_bubble.raw_text_buffer = (
                self.chat_window.thinking_content
            )
            self.chat_window.current_thinking_bubble._finalize_streaming()
        # Reset thinking bubble reference
        self.think_buffer_queue = []
        self.chat_window.current_thinking_bubble = None
        self.chat_window.thinking_content = ""

    def handle_user_context_request(self):
        """Handle user context request."""
        self.chat_window.chat_components.add_system_message("Refreshing my memory...")
