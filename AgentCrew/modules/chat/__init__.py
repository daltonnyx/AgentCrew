# ConsoleUI has been moved to AgentCrew.modules.console
# Import from the new location for backward compatibility

from .message_handler import MessageHandler

__all__ = ["MessageHandler"]
