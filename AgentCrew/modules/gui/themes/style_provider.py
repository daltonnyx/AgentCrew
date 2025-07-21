from .catppuccin import CatppuccinTheme
from .atom_light import AtomLightTheme
from .nord import NordTheme
from .dracula import DraculaTheme
from .unicorn import UnicornTheme
from AgentCrew.modules.config import ConfigManagement
from PySide6.QtCore import Signal, QObject


class StyleProvider(QObject):
    """Provides styling for the chat window and components."""

    # Signal emitted when theme changes
    theme_changed = Signal(str)

    _instance = None

    def __new__(cls):
        """Singleton pattern to ensure only one instance exists."""
        if cls._instance is None:
            cls._instance = super(StyleProvider, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        """Initialize the style provider by reading theme from global config."""
        if self._initialized:
            return

        super().__init__()
        self._initialized = True

        # Read theme from global config
        self.config_manager = ConfigManagement()
        global_config = self.config_manager.read_global_config_data()
        self.theme = global_config.get("global_settings", {}).get("theme", "dark")

        self._set_theme_class()

    def _set_theme_class(self):
        """Set the theme class based on the current theme setting."""
        if self.theme == "light":
            self.theme_class = AtomLightTheme
        elif self.theme == "nord":
            self.theme_class = NordTheme
        elif self.theme == "dracula":
            self.theme_class = DraculaTheme
        elif self.theme == "unicorn":
            self.theme_class = UnicornTheme
        else:
            self.theme_class = CatppuccinTheme  # Default to Catppuccin for "dark"

    def update_theme(self, reload=True):
        """
        Update the theme based on the current configuration.

        Args:
            reload (bool): If True, reload the theme from the configuration.
                          If False, use the currently set theme.

        Returns:
            bool: True if the theme changed, False otherwise.
        """
        if reload:
            # Re-read from config
            global_config = self.config_manager.read_global_config_data()
            new_theme = global_config.get("global_settings", {}).get("theme", "dark")

            # Check if theme changed
            if new_theme != self.theme:
                self.theme = new_theme
                self._set_theme_class()
                self.theme_changed.emit(self.theme)
                return True
        return False

    def get_main_style(self):
        """Get the main style for the chat window."""
        return self.theme_class.MAIN_STYLE

    def get_config_window_style(self):
        return self.theme_class.CONFIG_DIALOG

    def get_button_style(self, button_type="primary"):
        """Get style for buttons based on type."""
        if button_type == "primary":
            return self.theme_class.PRIMARY_BUTTON
        elif button_type == "secondary":
            return self.theme_class.SECONDARY_BUTTON
        elif button_type == "stop":
            return self.theme_class.STOP_BUTTON
        elif button_type == "disabled":
            return self.theme_class.DISABLED_BUTTON
        elif button_type == "stop_stopping":
            return self.theme_class.STOP_BUTTON_STOPPING
        elif button_type == "red":
            return self.theme_class.RED_BUTTON
        elif button_type == "green":
            return self.theme_class.GREEN_BUTTON
        elif button_type == "agent_menu":
            return self.theme_class.AGENT_MENU_BUTTON
        else:
            return ""

    def get_input_style(self):
        """Get style for text input."""
        return self.theme_class.TEXT_INPUT

    def get_menu_style(self):
        """Get style for menus."""
        return self.theme_class.MENU_BAR

    def get_status_indicator_style(self):
        """Get style for status indicator."""
        return self.theme_class.STATUS_INDICATOR

    def get_version_label_style(self):
        """Get style for version label."""
        return self.theme_class.VERSION_LABEL

    def get_tool_dialog_text_edit_style(self):
        """Get style for tool dialog text edit."""
        return self.theme_class.TOOL_DIALOG_TEXT_EDIT

    def get_tool_dialog_yes_button_style(self):
        """Get style for tool dialog yes button."""
        return self.theme_class.TOOL_DIALOG_YES_BUTTON

    def get_tool_dialog_all_button_style(self):
        """Get style for tool dialog all button."""
        return self.theme_class.TOOL_DIALOG_ALL_BUTTON

    def get_tool_dialog_no_button_style(self):
        """Get style for tool dialog no button."""
        return self.theme_class.TOOL_DIALOG_NO_BUTTON

    def get_system_message_label_style(self):
        """Get style for system message labels."""
        return self.theme_class.SYSTEM_MESSAGE_LABEL

    def get_system_message_toggle_style(self):
        """Get style for system message toggle buttons."""
        return self.theme_class.SYSTEM_MESSAGE_TOGGLE

    def get_sidebar_style(self):
        """Get style for sidebar widgets."""
        return self.theme_class.SIDEBAR

    def get_conversation_list_style(self):
        """Get style for conversation list."""
        return self.theme_class.CONVERSATION_LIST

    def get_search_box_style(self):
        """Get style for search boxes."""
        return self.theme_class.SEARCH_BOX

    def get_token_usage_style(self):
        """Get style for token usage widgets."""
        return self.theme_class.TOKEN_USAGE

    def get_token_usage_widget_style(self):
        """Get style for token usage widget background."""
        return self.theme_class.TOKEN_USAGE_WIDGET

    def get_context_menu_style(self):
        """Get style for context menus."""
        return self.theme_class.CONTEXT_MENU

    def get_agent_menu_style(self):
        """Get style for agent menus."""
        return self.theme_class.AGENT_MENU

    def get_user_bubble_style(self):
        """Get style for user message bubbles."""
        return self.theme_class.USER_BUBBLE

    def get_assistant_bubble_style(self):
        """Get style for assistant message bubbles."""
        return self.theme_class.ASSISTANT_BUBBLE

    def get_thinking_bubble_style(self):
        """Get style for thinking message bubbles."""
        return self.theme_class.THINKING_BUBBLE

    def get_consolidated_bubble_style(self):
        """Get style for consolidated message bubbles."""
        return self.theme_class.CONSOLIDATED_BUBBLE

    def get_splitter_style(self):
        return self.theme_class.SPLITTER_COLOR

    def get_code_color_style(self):
        return self.theme_class.CODE_CSS

    def get_rollback_button_style(self):
        """Get style for rollback buttons."""
        return self.theme_class.ROLLBACK_BUTTON

    def get_consolidated_button_style(self):
        """Get style for consolidated buttons."""
        return self.theme_class.CONSOLIDATED_BUTTON

    def get_user_message_label_style(self):
        """Get style for user message labels."""
        return self.theme_class.USER_MESSAGE_LABEL

    def get_assistant_message_label_style(self):
        """Get style for assistant message labels."""
        return self.theme_class.ASSISTANT_MESSAGE_LABEL

    def get_thinking_message_label_style(self):
        """Get style for thinking message labels."""
        return self.theme_class.THINKING_MESSAGE_LABEL

    def get_user_sender_label_style(self):
        """Get style for user sender labels."""
        return self.theme_class.USER_SENDER_LABEL

    def get_assistant_sender_label_style(self):
        """Get style for assistant sender labels."""
        return self.theme_class.ASSISTANT_SENDER_LABEL

    def get_thinking_sender_label_style(self):
        """Get style for thinking sender labels."""
        return self.theme_class.THINKING_SENDER_LABEL

    def get_metadata_header_label_style(self):
        """Get style for metadata header labels."""
        return self.theme_class.METADATA_HEADER_LABEL

    def get_user_file_name_label_style(self):
        """Get style for user file name labels."""
        return self.theme_class.USER_FILE_NAME_LABEL

    def get_assistant_file_name_label_style(self):
        """Get style for assistant file name labels."""
        return self.theme_class.ASSISTANT_FILE_NAME_LABEL

    def get_user_file_info_label_style(self):
        """Get style for user file info labels."""
        return self.theme_class.USER_FILE_INFO_LABEL

    def get_assistant_file_info_label_style(self):
        """Get style for assistant file info labels."""
        return self.theme_class.ASSISTANT_FILE_INFO_LABEL

    def get_api_keys_group_style(self):
        """Get style for API keys group boxes."""
        return self.theme_class.API_KEYS_GROUP

    def get_editor_container_widget_style(self):
        """Get style for editor container widgets."""
        return self.theme_class.EDITOR_CONTAINER_WIDGET

    def get_combo_box_style(self):
        """Get style for combo boxes."""
        return self.theme_class.COMBO_BOX

    def get_tool_widget_style(self):
        """Get style for tool widgets."""
        return (
            self.theme_class.TOOL_WIDGET
            if hasattr(self.theme_class, "TOOL_WIDGET")
            else ""
        )

    def get_tool_card_style(self):
        """Get style for tool widget cards."""
        return (
            self.theme_class.TOOL_CARD if hasattr(self.theme_class, "TOOL_CARD") else ""
        )

    def get_tool_card_error_style(self):
        """Get style for tool widget cards in error state."""
        return (
            self.theme_class.TOOL_CARD_ERROR
            if hasattr(self.theme_class, "TOOL_CARD_ERROR")
            else ""
        )

    def get_tool_header_style(self):
        """Get style for tool widget headers."""
        return (
            self.theme_class.TOOL_HEADER
            if hasattr(self.theme_class, "TOOL_HEADER")
            else ""
        )

    def get_tool_toggle_button_style(self):
        """Get style for tool widget toggle buttons."""
        return (
            self.theme_class.TOOL_TOGGLE_BUTTON
            if hasattr(self.theme_class, "TOOL_TOGGLE_BUTTON")
            else ""
        )

    def get_tool_status_style(self):
        """Get style for tool widget status indicators."""
        return (
            self.theme_class.TOOL_STATUS
            if hasattr(self.theme_class, "TOOL_STATUS")
            else ""
        )

    def get_tool_content_style(self):
        """Get style for tool widget content."""
        return (
            self.theme_class.TOOL_CONTENT
            if hasattr(self.theme_class, "TOOL_CONTENT")
            else ""
        )

    def get_tool_progress_style(self):
        """Get style for tool widget progress bars."""
        return (
            self.theme_class.TOOL_PROGRESS
            if hasattr(self.theme_class, "TOOL_PROGRESS")
            else ""
        )

    def get_tool_separator_style(self):
        """Get style for tool widget separators."""
        return (
            self.theme_class.TOOL_SEPARATOR
            if hasattr(self.theme_class, "TOOL_SEPARATOR")
            else ""
        )

    def get_tool_icon(self, tool_name):
        """Get icon for a specific tool."""
        icons = getattr(self.theme_class, "TOOL_ICONS", {})
        return icons.get(tool_name, icons.get("default", "🔧"))

    def get_json_editor_colors(self):
        """Get color scheme for JSON editor from current theme."""
        return self.theme_class.JSON_EDITOR_COLORS

    def get_json_editor_style(self):
        """Get complete stylesheet for JSON editor."""
        return self.theme_class.JSON_EDITOR_STYLE

    def get_markdown_editor_colors(self):
        """Get color scheme for Markdown editor from current theme."""
        return getattr(
            self.theme_class,
            "MARKDOWN_EDITOR_COLORS",
            {
                "background": "#313244",
                "text": "#cdd6f4",
                "border": "#45475a",
                "header": "#89b4fa",
                "bold": "#fab387",
                "italic": "#a6e3a1",
                "code": "#f5c2e7",
                "code_background": "#45475a",
                "link": "#74c7ec",
                "image": "#cba6f7",
                "list": "#f9e2af",
                "blockquote": "#94e2d5",
                "hr": "#6c7086",
                "strikethrough": "#eba0ac",
                "error": "#f38ba8",
            },
        )

    def get_markdown_editor_style(self):
        """Get complete stylesheet for Markdown editor."""
        return getattr(
            self.theme_class,
            "MARKDOWN_EDITOR_STYLE",
            """
QPlainTextEdit {
    background-color: #313244;
    color: #cdd6f4;
    border: 1px solid #45475a;
    border-radius: 4px;
    padding: 8px;
    font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
    font-size: 12px;
    line-height: 1.4;
}
QPlainTextEdit:focus {
    border: 1px solid #89b4fa;
}
""",
        )
