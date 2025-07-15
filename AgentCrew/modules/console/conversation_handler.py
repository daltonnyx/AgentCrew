"""
Conversation handling for console UI.
Manages conversation loading, listing, and display functionality.
"""

from typing import List, Dict, Any
from rich.console import Console
from rich.text import Text

from .constants import RICH_STYLE_YELLOW, RICH_STYLE_RED


class ConversationHandler:
    """Handles conversation-related operations for the console UI."""

    def __init__(self, console: Console, display_handlers):
        """Initialize the conversation handler."""
        self.console = console
        self.display_handlers = display_handlers
        self._cached_conversations = []

    def handle_load_conversation(self, load_arg: str, message_handler):
        """
        Handle loading a conversation by number or ID.

        Args:
            load_arg: Either a conversation number (from the list) or a conversation ID
            message_handler: The message handler instance
        """
        # First check if we have a list of conversations cached
        if not self._cached_conversations:
            # If not, get the list first
            self._cached_conversations = message_handler.list_conversations()

        try:
            # Check if the argument is a number (index in the list)
            if load_arg.isdigit():
                index = int(load_arg) - 1  # Convert to 0-based index
                if 0 <= index < len(self._cached_conversations):
                    convo_id = self._cached_conversations[index].get("id")
                    if convo_id:
                        self.console.print(
                            Text(
                                f"Loading conversation #{load_arg}...",
                                style=RICH_STYLE_YELLOW,
                            )
                        )
                        messages = message_handler.load_conversation(convo_id)
                        if messages:
                            self.display_handlers.display_loaded_conversation(
                                messages, message_handler
                            )
                        return
                self.console.print(
                    Text(
                        "Invalid conversation number. Use '/list' to see available conversations.",
                        style=RICH_STYLE_RED,
                    )
                )
            else:
                # Assume it's a conversation ID
                self.console.print(
                    Text(
                        f"Loading conversation with ID: {load_arg}...",
                        style=RICH_STYLE_YELLOW,
                    )
                )
                messages = message_handler.load_conversation(load_arg)
                if messages:
                    self.display_handlers.display_loaded_conversation(
                        messages, message_handler
                    )
        except Exception as e:
            self.console.print(
                Text(f"Error loading conversation: {str(e)}", style=RICH_STYLE_RED)
            )

    def update_cached_conversations(self, conversations: List[Dict[str, Any]]):
        """Update the cached conversations list."""
        self._cached_conversations = conversations

    def get_cached_conversations(self):
        """Get the cached conversations list."""
        return self._cached_conversations
