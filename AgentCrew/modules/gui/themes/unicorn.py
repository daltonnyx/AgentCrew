"""Unicorn theme styles for AgentCrew GUI."""


class UnicornTheme:
    """Static class containing Unicorn theme styles.

    Based on the Unicorn Candy color palette: https://www.color-hex.com/color-palette/79054

    Unicorn Candy Palette:
    - Light Cyan: #d0f4f4 (Cool cyan - primary backgrounds)
    - Lavender: #eed5ff (Light purple - secondary backgrounds) 
    - Pink: #ffc0d7 (Soft pink - accent elements)
    - Cream: #fff9c1 (Light yellow - highlights)
    - Mint: #cfebd2 (Light green - success states)
    
    Extended palette for dark elements:
    - Deep Purple: #6b46c1 (Primary actions)
    - Dark Slate: #374151 (Text and borders)
    - Midnight: #1f2937 (Dark backgrounds)
    - Charcoal: #111827 (Deepest backgrounds)
    """

    # Main application styles
    MAIN_STYLE = """
QMainWindow {
    background-color: #f8fafc; /* Very light background */
}
QScrollArea {
    border: none;
    background-color: #f1f5f9; /* Light slate background */
}
QWidget#chatContainer { /* Specific ID for chat_container */
    background-color: #f8fafc; /* Very light background */
}
QSplitter::handle {
    background-color: #e2e8f0; /* Light slate border */
}
QSplitter::handle:hover {
    background-color: #cbd5e1; /* Darker slate on hover */
}
QSplitter::handle:pressed {
    background-color: #6b46c1; /* Deep purple when pressed */
}
QStatusBar {
    background-color: #f1f5f9; /* Light slate background */
    color: #374151; /* Dark slate text */
}
QToolTip {
    background-color: #eed5ff; /* Lavender background */
    color: #374151; /* Dark slate text */
    border: 1px solid #6b46c1; /* Deep purple border */
    padding: 4px;
}
QMessageBox {
    background-color: #f1f5f9; /* Light slate background */
}
QMessageBox QLabel { /* For message text in QMessageBox */
    color: #374151; /* Dark slate text */
    background-color: transparent;
}
/* QCompleter's popup is often a QListView */
QListView { /* General style for QListView, affects completer */
    background-color: #eed5ff; /* Lavender background */
    color: #374151; /* Dark slate text */
    border: 1px solid #6b46c1; /* Deep purple border */
    padding: 2px;
    outline: 0px;
}
QListView::item {
    padding: 4px 8px;
    border-radius: 2px;
}
QListView::item:selected {
    background-color: #6b46c1; /* Deep purple selection */
    color: #ffffff; /* White text on selection */
}
QListView::item:hover {
    background-color: #ffc0d7; /* Pink hover */
}

/* Modern Scrollbar Styles */
QScrollBar:vertical {
    border: none;
    background: #f1f5f9; /* Light slate track */
    width: 10px;
    margin: 0px 0px 0px 0px;
}
QScrollBar::handle:vertical {
    background: #cbd5e1; /* Slate handle */
    min-height: 20px;
    border-radius: 5px;
}
QScrollBar::handle:vertical:hover {
    background: #6b46c1; /* Deep purple hover */
}
QScrollBar::handle:vertical:pressed {
    background: #553c9a; /* Darker purple pressed */
}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    border: none;
    background: none;
    height: 0px;
    subcontrol-position: top;
    subcontrol-origin: margin;
}
QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
    background: none;
}

QScrollBar:horizontal {
    border: none;
    background: #f1f5f9; /* Light slate track */
    height: 10px;
    margin: 0px 0px 0px 0px;
}
QScrollBar::handle:horizontal {
    background: #cbd5e1; /* Slate handle */
    min-width: 20px;
    border-radius: 5px;
}
QScrollBar::handle:horizontal:hover {
    background: #6b46c1; /* Deep purple hover */
}
QScrollBar::handle:horizontal:pressed {
    background: #553c9a; /* Darker purple pressed */
}
QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
    border: none;
    background: none;
    width: 0px;
    subcontrol-position: left;
    subcontrol-origin: margin;
}
QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
    background: none;
}

/* Context menu styling for QLabel widgets */
QLabel QMenu {
    background-color: #f1f5f9; /* Light slate background */
    border: 1px solid #6b46c1; /* Deep purple border */
    padding: 4px;
    border-radius: 6px;
}
QLabel QMenu::item {
    color: #374151; /* Dark slate text */
    padding: 8px 24px 8px 12px;
    border-radius: 4px;
    margin: 2px;
}
QLabel QMenu::item:selected {
    background-color: #6b46c1; /* Deep purple selection */
    color: #ffffff; /* White text */
}
QLabel QMenu::item:pressed {
    background-color: #553c9a; /* Darker purple */
}
QLabel QMenu::separator {
    height: 1px;
    background: #cbd5e1; /* Light slate separator */
    margin: 4px 8px;
}
"""

    # Button styles
    PRIMARY_BUTTON = """
QPushButton {
    background-color: #6b46c1; /* Deep purple */
    color: #ffffff; /* White text */
    border: none;
    border-radius: 4px; 
    padding: 8px;
    font-weight: bold;
}
QPushButton:hover {
    background-color: #553c9a; /* Darker purple hover */
}
QPushButton:pressed {
    background-color: #4c1d95; /* Even darker purple pressed */
}
QPushButton:disabled {
    background-color: #cbd5e1; /* Light slate disabled */
    color: #6b7280; /* Gray text */
}
"""

    SECONDARY_BUTTON = """
QPushButton {
    background-color: #eed5ff; /* Lavender background */
    color: #374151; /* Dark slate text */
    border: none;
    border-radius: 4px; 
    padding: 8px;
    font-weight: bold;
}
QPushButton:hover {
    background-color: #e4d4fd; /* Darker lavender hover */
}
QPushButton:pressed {
    background-color: #6b46c1; /* Deep purple pressed */
    color: #ffffff; /* White text when pressed */
}
QPushButton:disabled {
    background-color: #f1f5f9; /* Light slate disabled */
    color: #9ca3af; /* Light gray text */
}
"""

    STOP_BUTTON = """
QPushButton {
    background-color: #ef4444; /* Red */
    color: #ffffff; /* White text */
    border: none;
    border-radius: 4px; 
    padding: 8px;
    font-weight: bold;
}
QPushButton:hover {
    background-color: #dc2626; /* Darker red hover */
}
QPushButton:pressed {
    background-color: #b91c1c; /* Even darker red pressed */
}
"""

    RED_BUTTON = """
QPushButton {
    background-color: #ef4444; /* Red */
    color: #ffffff; /* White text */
    border: none;
    border-radius: 4px;
    padding: 8px;
    font-weight: bold;
}
QPushButton:hover {
    background-color: #dc2626; /* Darker red hover */
}
QPushButton:pressed {
    background-color: #b91c1c; /* Even darker red pressed */
}
QPushButton:disabled {
    background-color: #cbd5e1; /* Light slate disabled */
    color: #6b7280; /* Gray text */
}
"""

    GREEN_BUTTON = """
QPushButton {
    background-color: #10b981; /* Green (similar to mint #cfebd2 but darker) */
    color: #ffffff; /* White text */
    border: none;
    border-radius: 4px;
    padding: 8px;
    font-weight: bold;
}
QPushButton:hover {
    background-color: #059669; /* Darker green hover */
}
QPushButton:pressed {
    background-color: #047857; /* Even darker green pressed */
}
QPushButton:disabled {
    background-color: #cbd5e1; /* Light slate disabled */
    color: #6b7280; /* Gray text */
}
"""

    API_KEYS_GROUP = """
QGroupBox {
    background-color: #f1f5f9; /* Light slate background */
}
QLabel {
    background-color: #f1f5f9; 
}
"""

    EDITOR_CONTAINER_WIDGET = """
QWidget {
    background-color: #f1f5f9; /* Light slate background */
}
"""

    MENU_BUTTON = """
QPushButton {
    background-color: #6b46c1; /* Deep purple */
    color: #ffffff; /* White text */
    border: none;
    border-radius: 4px;
    padding: 8px;
    font-weight: bold;
    padding-left: 12px;
}
QPushButton:hover {
    background-color: #553c9a; /* Darker purple hover */
}
QPushButton:pressed {
    background-color: #4c1d95; /* Even darker purple pressed */
}
QPushButton:disabled {
    background-color: #cbd5e1; /* Light slate disabled */
    color: #6b7280; /* Gray text */
}
QPushButton::menu-indicator {
    subcontrol-origin: padding;
    subcontrol-position: right center;
    right: 5px;
    width: 16px;
}
"""

    DISABLED_BUTTON = """
QPushButton {
    background-color: #cbd5e1; /* Light slate disabled */
    color: #6b7280; /* Gray text */
    border: none;
    border-radius: 4px; 
    padding: 8px;
    font-weight: bold;
}
"""

    STOP_BUTTON_STOPPING = """
QPushButton {
    background-color: #e2e8f0; /* Light slate */
    color: #6b7280; /* Gray text */
    border: none;
    border-radius: 4px; 
    padding: 8px;
    font-weight: bold;
}
"""

    COMBO_BOX = """
QComboBox {
    background-color: #ffffff; /* White background */
    color: #374151; /* Dark slate text */
    border: 1px solid #d1d5db; /* Light gray border */
    border-radius: 4px;
    padding: 6px 8px;
    min-width: 120px;
}
QComboBox:hover {
    border: 1px solid #6b46c1; /* Deep purple hover border */
}
QComboBox:focus {
    border: 1px solid #6b46c1; /* Deep purple focus border */
}
QComboBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 20px;
    border-left-width: 1px;
    border-left-color: #d1d5db; /* Light gray */
    border-left-style: solid;
    border-top-right-radius: 4px;
    border-bottom-right-radius: 4px;
    background-color: #f9fafb; /* Very light gray */
}
QComboBox::down-arrow {
    width: 0;
    height: 0;
    border-left: 4px solid transparent;
    border-right: 4px solid transparent;
    border-top: 6px solid #374151; /* Dark slate arrow */
}
QComboBox QAbstractItemView {
    background-color: #ffffff; /* White dropdown */
    color: #374151; /* Dark slate text */
    border: 1px solid #d1d5db; /* Light gray border */
    border-radius: 4px;
    selection-background-color: #6b46c1; /* Deep purple selection */
    selection-color: #ffffff; /* White selected text */
    outline: 0px;
}
"""

    # Input styles
    TEXT_INPUT = """
QTextEdit {
    background-color: #ffffff; /* White background */
    color: #374151; /* Dark slate text */
    border: 1px solid #d1d5db; /* Light gray border */
    border-radius: 4px;
    padding: 8px;
}
QTextEdit:focus {
    border: 1px solid #6b46c1; /* Deep purple focus border */
}
"""

    LINE_EDIT = """
QLineEdit {
    background-color: #ffffff; /* White background */
    color: #374151; /* Dark slate text */
    border: 1px solid #d1d5db; /* Light gray border */
    border-radius: 4px;
    padding: 8px;
}
QLineEdit:focus {
    border: 1px solid #6b46c1; /* Deep purple focus border */
}
"""

    # Menu styles
    MENU_BAR = """
QMenuBar {
    background-color: #f1f5f9; /* Light slate background */
    color: #374151; /* Dark slate text */
    padding: 2px;
}
QMenuBar::item {
    background-color: transparent;
    color: #374151; /* Dark slate text */
    padding: 4px 12px;
    border-radius: 4px;
}
QMenuBar::item:selected {
    background-color: #eed5ff; /* Lavender selection */
}
QMenuBar::item:pressed {
    background-color: #e4d4fd; /* Darker lavender pressed */
}
QMenu {
    background-color: #ffffff; /* White menu background */
    color: #374151; /* Dark slate text */
    border: 1px solid #d1d5db; /* Light gray border */
    padding: 4px;
}
QMenu::item {
    padding: 6px 24px 6px 12px;
    border-radius: 4px;
}
QMenu::item:selected {
    background-color: #6b46c1; /* Deep purple selection */
    color: #ffffff; /* White selected text */
}
QMenu::separator {
    height: 1px;
    background: #e5e7eb; /* Light gray separator */
    margin-left: 10px;
    margin-right: 5px;
}
"""

    CONTEXT_MENU = """
QMenu {
    background-color: #ffffff; /* White background */
    color: #374151; /* Dark slate text */
    border: 1px solid #d1d5db; /* Light gray border */
    padding: 4px;
    border-radius: 6px;
}
QMenu::item {
    padding: 8px 24px 8px 12px;
    border-radius: 4px;
    margin: 2px;
    color: #374151; /* Dark slate text */
}
QMenu::item:selected {
    background-color: #6b46c1; /* Deep purple selection */
    color: #ffffff; /* White selected text */
}
QMenu::item:pressed {
    background-color: #553c9a; /* Darker purple pressed */
}
QMenu::item:disabled {
    background-color: transparent;
    color: #9ca3af; /* Light gray disabled text */
}
QMenu::separator {
    height: 1px;
    background: #e5e7eb; /* Light gray separator */
    margin: 4px 8px;
}
"""

    AGENT_MENU = """
QMenu {
    background-color: #ffffff; /* White background */
    color: #374151; /* Dark slate text */
    border: 1px solid #eed5ff; /* Lavender border */
    border-radius: 4px;
    padding: 4px;
}
QMenu::item {
    padding: 6px 20px;
    background-color: transparent;
}
QMenu::item:selected {
    background-color: #6b46c1; /* Deep purple selection */
    color: #ffffff; /* White selected text */
    border-radius: 3px;
}
QMenu::separator {
    height: 1px;
    background-color: #eed5ff; /* Lavender separator */
    margin-left: 5px;
    margin-right: 5px;
}
"""

    # Label styles
    STATUS_INDICATOR = """
QLabel {
    background-color: #eed5ff; /* Lavender background */
    color: #374151; /* Dark slate text */
    padding: 8px; 
    border-radius: 5px;
    font-weight: bold;
}
"""

    VERSION_LABEL = """
QLabel {
    color: #6b7280; /* Gray text */
    padding: 2px 8px;
    font-size: 11px;
}
"""

    SYSTEM_MESSAGE_TOGGLE_BUTTON = """
QPushButton {
    background-color: transparent;
    color: #6b46c1; /* Deep purple */
    border: none;
    text-align: left;
    padding: 2px;
}
QPushButton:hover {
    color: #553c9a; /* Darker purple hover */
}
"""

    # Widget-specific styles
    SIDEBAR = """
background-color: #f1f5f9; /* Light slate background */
"""

    CONVERSATION_LIST = """
QListWidget {
    background-color: #f8fafc; /* Very light background */
    border: 1px solid #e2e8f0; /* Light slate border */
    border-radius: 4px;
}
QListWidget::item {
    color: #374151; /* Dark slate text */
    background-color: #f8fafc; /* Very light background */
    border: none;
    border-bottom: 1px solid #e2e8f0; /* Light slate border */
    margin: 0px;
    padding: 8px;
}
QListWidget::item:selected {
    background-color: #6b46c1; /* Deep purple selection */
    color: #ffffff; /* White selected text */
}
QListWidget::item:hover:!selected {
    background-color: #eed5ff; /* Lavender hover */
}
"""

    SEARCH_BOX = """
QLineEdit {
    background-color: #ffffff; /* White background */
    color: #374151; /* Dark slate text */
    border: 1px solid #d1d5db; /* Light gray border */
    border-radius: 4px;
    padding: 8px;
}
QLineEdit:focus {
    border: 1px solid #6b46c1; /* Deep purple focus border */
}
"""

    TOKEN_USAGE = """
QLabel {
    color: #374151; /* Dark slate text */
    font-weight: bold;
    padding: 8px;
    background-color: #f8fafc; /* Very light background */
    border-top: 1px solid #e2e8f0; /* Light slate border */
}
"""

    TOKEN_USAGE_WIDGET = """
background-color: #f8fafc; /* Very light background */
"""

    # Message bubble styles
    USER_BUBBLE = """
QFrame { 
    border-radius: 5px; 
    background-color: #6b46c1; /* Deep purple */
    border: none;
    padding: 2px;
}
"""

    ASSISTANT_BUBBLE = """
QFrame { 
    border-radius: 5px; 
    background-color: #eed5ff; /* Lavender */
    border: none;
    padding: 2px;
}
"""

    THINKING_BUBBLE = """
QFrame { 
    border-radius: 5px; 
    background-color: #f1f5f9; /* Light slate */
    border: none;
    padding: 2px;
}
"""

    CONSOLIDATED_BUBBLE = """
QFrame { 
    border-radius: 5px; 
    background-color: #eed5ff; /* Lavender */
    border: 1px solid #d1d5db; /* Light gray border */
    padding: 2px;
}
"""

    ROLLBACK_BUTTON = """
QPushButton {
    background-color: #ffc0d7; /* Pink */
    color: #374151; /* Dark slate text */
    border: none;
    border-radius: 15px;
    padding: 8px;
    font-size: 24px;
    font-weight: bold;
    width: 30px;
    height: 30px;
}
QPushButton:hover {
    background-color: #ffadd0; /* Darker pink hover */
}
QPushButton:pressed {
    background-color: #ff9ac5; /* Even darker pink pressed */
}
"""

    CONSOLIDATED_BUTTON = """
QPushButton {
    background-color: #ffc0d7; /* Pink */
    color: #374151; /* Dark slate text */
    border: none;
    border-radius: 15px;
    padding: 8px;
    font-size: 16px;
    font-weight: bold;
    width: 30px;
    height: 30px;
}
QPushButton:hover {
    background-color: #ffadd0; /* Darker pink hover */
}
QPushButton:pressed {
    background-color: #ff9ac5; /* Even darker pink pressed */
}
"""

    # Tool dialog styles
    TOOL_DIALOG_TEXT_EDIT = """
QTextEdit {
    background-color: #ffffff; /* White background */
    color: #374151; /* Dark slate text */
    border: 1px solid #d1d5db; /* Light gray border */
    border-radius: 4px;
    padding: 8px;
    font-family: monospace;
}
QTextEdit:focus {
    border: 1px solid #6b46c1; /* Deep purple focus border */
}
"""

    TOOL_DIALOG_YES_BUTTON = """
QPushButton {
    background-color: #10b981; /* Green */
    color: #ffffff; /* White text */
    font-weight: bold;
    padding: 6px 14px;
    border: none;
    border-radius: 4px;
}
QPushButton:hover {
    background-color: #059669; /* Darker green hover */
}
"""

    TOOL_DIALOG_ALL_BUTTON = """
QPushButton {
    background-color: #6b46c1; /* Deep purple */
    color: #ffffff; /* White text */
    font-weight: bold;
    padding: 6px 14px;
    border: none;
    border-radius: 4px;
}
QPushButton:hover {
    background-color: #553c9a; /* Darker purple hover */
}
"""

    TOOL_DIALOG_NO_BUTTON = """
QPushButton {
    background-color: #ef4444; /* Red */
    color: #ffffff; /* White text */
    font-weight: bold;
    padding: 6px 14px;
    border: none;
    border-radius: 4px;
}
QPushButton:hover {
    background-color: #dc2626; /* Darker red hover */
}
"""

    AGENT_MENU_BUTTON = """
QPushButton {
    background-color: #6b46c1; /* Deep purple */
    color: #ffffff; /* White text */
    border: none;
    border-radius: 4px;
    padding: 8px;
    font-weight: bold;
    padding-left: 12px;
}
QPushButton:hover {
    background-color: #553c9a; /* Darker purple hover */
}
QPushButton:pressed {
    background-color: #4c1d95; /* Even darker purple pressed */
}
QPushButton:disabled {
    background-color: #cbd5e1; /* Light slate disabled */
    color: #6b7280; /* Gray text */
}
QPushButton::menu-indicator {
    subcontrol-origin: padding;
    subcontrol-position: right center;
    right: 5px;
    width: 16px;
}
"""

    # Widget-specific styles
    SYSTEM_MESSAGE_LABEL = """
color: #6b7280; /* Gray text */
padding: 2px;
"""

    SYSTEM_MESSAGE_TOGGLE = """
QPushButton {
    background-color: transparent;
    color: #6b46c1; /* Deep purple */
    border: none;
    text-align: left;
    padding: 2px;
}
QPushButton:hover {
    color: #553c9a; /* Darker purple hover */
}
"""

    # Config window styles
    CONFIG_DIALOG = """
QDialog {
    background-color: #f8fafc; /* Very light background */
    color: #374151; /* Dark slate text */
}
QTabWidget::pane {
    border: 1px solid #e2e8f0; /* Light slate border */
    background-color: #ffffff; /* White pane background */
    border-radius: 4px;
}
QTabBar::tab {
    background-color: #f1f5f9; /* Light slate tab background */
    color: #374151; /* Dark slate text */
    padding: 8px;
    border-top-left-radius: 4px;
    border-top-right-radius: 4px;
    border: 1px solid #d1d5db; /* Light gray border */
    border-bottom: none;
    margin-right: 2px;
}
QTabBar::tab:selected {
    background-color: #ffffff; /* White selected tab */
    border-bottom-color: #ffffff; /* White */
    color: #6b46c1; /* Deep purple selected text */
}
QTabBar::tab:hover:!selected {
    background-color: #eed5ff; /* Lavender hover */
}
QPushButton {
    background-color: #6b46c1; /* Deep purple */
    color: #ffffff; /* White text */
    border: none;
    border-radius: 4px;
    padding: 8px;
    font-weight: bold;
}
QPushButton:hover {
    background-color: #553c9a; /* Darker purple hover */
}
QPushButton:pressed {
    background-color: #4c1d95; /* Even darker purple pressed */
}
QPushButton:disabled {
    background-color: #cbd5e1; /* Light slate disabled */
    color: #6b7280; /* Gray text */
}
QListWidget {
    background-color: #ffffff; /* White background */
    border: 1px solid #e2e8f0; /* Light slate border */
    border-radius: 4px;
    padding: 4px;
    color: #374151; /* Dark slate text */
}
QListWidget::item {
    padding: 6px;
    border-radius: 2px;
    color: #374151; /* Dark slate text */
    background-color: #ffffff; /* White background */
}
QListWidget::item:selected {
    background-color: #6b46c1; /* Deep purple selection */
    color: #ffffff; /* White selected text */
}
QListWidget::item:hover:!selected {
    background-color: #eed5ff; /* Lavender hover */
}
QLineEdit, QTextEdit {
    border: 1px solid #d1d5db; /* Light gray border */
    border-radius: 4px;
    padding: 6px;
    background-color: #ffffff; /* White background */
    color: #374151; /* Dark slate text */
}
QLineEdit:focus, QTextEdit:focus {
    border: 1px solid #6b46c1; /* Deep purple focus border */
}
QCheckBox {
    spacing: 8px;
    color: #374151; /* Dark slate text */
}
QCheckBox::indicator {
    width: 16px;
    height: 16px;
    border-radius: 2px;
    background-color: #ffffff; /* White background */
    border: 1px solid #d1d5db; /* Light gray border */
}
QCheckBox::indicator:checked {
    background-color: #6b46c1; /* Deep purple checked */
    border: 1px solid #6b46c1; /* Deep purple border */
}
QCheckBox::indicator:hover {
    border: 1px solid #553c9a; /* Darker purple hover border */
}
QGroupBox {
    font-weight: bold;
    border: 1px solid #d1d5db; /* Light gray border */
    border-radius: 4px;
    margin-top: 12px;
    padding-top: 12px;
    background-color: #ffffff; /* White groupbox background */
}
QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top left;
    padding: 0 4px 4px 4px;
    color: #6b46c1; /* Deep purple title */
    background-color: #ffffff; /* White title background */
    left: 10px;
}
QScrollArea {
    background-color: #ffffff; /* White background */
    border: none;
}
QScrollArea > QWidget > QWidget {
     background-color: #ffffff; /* White background */
}
QLabel {
    color: #374151; /* Dark slate text */
    padding: 2px;
}
QSplitter::handle {
    background-color: #e2e8f0; /* Light slate */
}
QSplitter::handle:hover {
    background-color: #cbd5e1; /* Darker slate hover */
}
QSplitter::handle:pressed {
    background-color: #6b46c1; /* Deep purple pressed */
}
"""

    PANEL = """
background-color: #f1f5f9; /* Light slate background */
"""

    SCROLL_AREA = """
background-color: #f1f5f9; /* Light slate background */
border: none;
"""

    EDITOR_WIDGET = """
background-color: #f1f5f9; /* Light slate background */
"""

    GROUP_BOX = """
background-color: #f8fafc; /* Very light background */
"""

    SPLITTER_COLOR = """
QSplitter::handle {
    background-color: #e2e8f0; /* Light slate */
}
QSplitter::handle:hover {
    background-color: #cbd5e1; /* Darker slate hover */
}
QSplitter::handle:pressed {
    background-color: #6b46c1; /* Deep purple pressed */
}
"""

    METADATA_HEADER_LABEL = """
QLabel {
    color: #6b7280; /* Gray text */
    font-style: italic;
    padding-bottom: 5px;
}
"""

    # Message label styles
    USER_MESSAGE_LABEL = """
QLabel {
    color: #ffffff; /* White text on purple bubble */
}
"""

    ASSISTANT_MESSAGE_LABEL = """
QLabel {
    color: #374151; /* Dark slate text on lavender bubble */
}
"""

    THINKING_MESSAGE_LABEL = """
QLabel {
    color: #374151; /* Dark slate text */
}
"""

    # Sender label styles
    USER_SENDER_LABEL = """
QLabel {
    font-weight: bold;
    color: #ffffff; /* White text */
    padding: 2px;
}
"""

    ASSISTANT_SENDER_LABEL = """
QLabel {
    font-weight: bold;
    color: #374151; /* Dark slate text */
    padding: 2px;
}
"""

    THINKING_SENDER_LABEL = """
QLabel {
    font-weight: bold;
    color: #374151; /* Dark slate text */
    padding: 2px;
}
"""

    # File display label styles
    USER_FILE_NAME_LABEL = """
QLabel {
    font-weight: bold;
    color: #ffffff; /* White text */
    padding-left: 10px;
}
"""

    ASSISTANT_FILE_NAME_LABEL = """
QLabel {
    font-weight: bold;
    color: #374151; /* Dark slate text */
    padding-left: 10px;
}
"""

    USER_FILE_INFO_LABEL = """
QLabel {
    color: #e2e8f0; /* Light slate - good contrast on purple bubble */
}
"""

    ASSISTANT_FILE_INFO_LABEL = """
QLabel {
    color: #6b7280; /* Gray text on lavender bubble */
}
"""

    CODE_CSS = """
pre { line-height: 1; background-color: #ffffff; border-radius: 8px; padding: 12px; color: #374151; white-space: pre-wrap; word-wrap: break-word; border: 1px solid #e5e7eb; } /* White background, dark slate text */
td.linenos .normal { color: #9ca3af; background-color: transparent; padding-left: 5px; padding-right: 5px; } /* Light gray line numbers */
span.linenos { color: #9ca3af; background-color: transparent; padding-left: 5px; padding-right: 5px; } /* Light gray line numbers */
td.linenos .special { color: #374151; background-color: #f9fafb; padding-left: 5px; padding-right: 5px; } /* Dark slate special line numbers */
span.linenos.special { color: #374151; background-color: #f9fafb; padding-left: 5px; padding-right: 5px; } /* Dark slate special line numbers */
.codehilite .hll { background-color: #fff9c1 } /* Cream highlight */
.codehilite { background: #ffffff; border-radius: 8px; padding: 10px; color: #374151; border: 1px solid #e5e7eb; } /* White background, dark slate text */
.codehilite .c { color: #9ca3af; font-style: italic } /* Comment -> Light gray */
.codehilite .err { border: 1px solid #ef4444; color: #ef4444; } /* Error -> Red */
.codehilite .k { color: #6b46c1; font-weight: bold } /* Keyword -> Deep purple */
.codehilite .o { color: #059669 } /* Operator -> Green */
.codehilite .ch { color: #9ca3af; font-style: italic } /* Comment.Hashbang -> Light gray */
.codehilite .cm { color: #9ca3af; font-style: italic } /* Comment.Multiline -> Light gray */
.codehilite .cp { color: #d97706 } /* Comment.Preproc -> Orange */
.codehilite .cpf { color: #9ca3af; font-style: italic } /* Comment.PreprocFile -> Light gray */
.codehilite .c1 { color: #9ca3af; font-style: italic } /* Comment.Single -> Light gray */
.codehilite .cs { color: #9ca3af; font-style: italic } /* Comment.Special -> Light gray */
.codehilite .gd { color: #ef4444 } /* Generic.Deleted -> Red */
.codehilite .ge { font-style: italic } /* Generic.Emph */
.codehilite .ges { font-weight: bold; font-style: italic } /* Generic.EmphStrong */
.codehilite .gr { color: #ef4444 } /* Generic.Error -> Red */
.codehilite .gh { color: #6b46c1; font-weight: bold } /* Generic.Heading -> Deep purple */
.codehilite .gi { color: #10b981 } /* Generic.Inserted -> Green */
.codehilite .go { color: #374151 } /* Generic.Output -> Dark slate */
.codehilite .gp { color: #6b46c1; font-weight: bold } /* Generic.Prompt -> Deep purple */
.codehilite .gs { font-weight: bold } /* Generic.Strong */
.codehilite .gu { color: #6b46c1; font-weight: bold } /* Generic.Subheading -> Deep purple */
.codehilite .gt { color: #ef4444 } /* Generic.Traceback -> Red */
.codehilite .kc { color: #6b46c1; font-weight: bold } /* Keyword.Constant -> Deep purple */
.codehilite .kd { color: #6b46c1; font-weight: bold } /* Keyword.Declaration -> Deep purple */
.codehilite .kn { color: #6b46c1; font-weight: bold } /* Keyword.Namespace -> Deep purple */
.codehilite .kp { color: #6b46c1 } /* Keyword.Pseudo -> Deep purple */
.codehilite .kr { color: #6b46c1; font-weight: bold } /* Keyword.Reserved -> Deep purple */
.codehilite .kt { color: #dc2626; font-weight: bold } /* Keyword.Type -> Dark red */
.codehilite .m { color: #7c3aed } /* Literal.Number -> Purple */
.codehilite .s { color: #10b981 } /* Literal.String -> Green */
.codehilite .na { color: #0ea5e9 } /* Name.Attribute -> Sky blue */
.codehilite .nb { color: #6b46c1 } /* Name.Builtin -> Deep purple */
.codehilite .nc { color: #d97706; font-weight: bold } /* Name.Class -> Orange */
.codehilite .no { color: #dc2626 } /* Name.Constant -> Dark red */
.codehilite .nd { color: #6b46c1 } /* Name.Decorator -> Deep purple */
.codehilite .ni { color: #374151; font-weight: bold } /* Name.Entity -> Dark slate */
.codehilite .ne { color: #ef4444; font-weight: bold } /* Name.Exception -> Red */
.codehilite .nf { color: #6b46c1; font-weight: bold } /* Name.Function -> Deep purple */
.codehilite .nl { color: #374151 } /* Name.Label -> Dark slate */
.codehilite .nn { color: #d97706; font-weight: bold } /* Name.Namespace -> Orange */
.codehilite .nt { color: #6b46c1; font-weight: bold } /* Name.Tag -> Deep purple */
.codehilite .nv { color: #374151 } /* Name.Variable -> Dark slate */
.codehilite .ow { color: #059669; font-weight: bold } /* Operator.Word -> Green */
.codehilite .w { color: #9ca3af } /* Text.Whitespace -> Light gray */
.codehilite .mb { color: #7c3aed } /* Literal.Number.Bin -> Purple */
.codehilite .mf { color: #7c3aed } /* Literal.Number.Float -> Purple */
.codehilite .mh { color: #7c3aed } /* Literal.Number.Hex -> Purple */
.codehilite .mi { color: #7c3aed } /* Literal.Number.Integer -> Purple */
.codehilite .mo { color: #7c3aed } /* Literal.Number.Oct -> Purple */
.codehilite .sa { color: #10b981 } /* Literal.String.Affix -> Green */
.codehilite .sb { color: #10b981 } /* Literal.String.Backtick -> Green */
.codehilite .sc { color: #10b981 } /* Literal.String.Char -> Green */
.codehilite .dl { color: #10b981 } /* Literal.String.Delimiter -> Green */
.codehilite .sd { color: #9ca3af; font-style: italic } /* Literal.String.Doc -> Light gray */
.codehilite .s2 { color: #10b981 } /* Literal.String.Double -> Green */
.codehilite .se { color: #dc2626; font-weight: bold } /* Literal.String.Escape -> Dark red */
.codehilite .sh { color: #10b981 } /* Literal.String.Heredoc -> Green */
.codehilite .si { color: #10b981; font-weight: bold } /* Literal.String.Interpol -> Green */
.codehilite .sx { color: #10b981 } /* Literal.String.Other -> Green */
.codehilite .sr { color: #10b981 } /* Literal.String.Regex -> Green */
.codehilite .s1 { color: #10b981 } /* Literal.String.Single -> Green */
.codehilite .ss { color: #10b981 } /* Literal.String.Symbol -> Green */
.codehilite .bp { color: #6b46c1 } /* Name.Builtin.Pseudo -> Deep purple */
.codehilite .fm { color: #6b46c1; font-weight: bold } /* Name.Function.Magic -> Deep purple */
.codehilite .vc { color: #374151 } /* Name.Variable.Class -> Dark slate */
.codehilite .vg { color: #374151 } /* Name.Variable.Global -> Dark slate */
.codehilite .vi { color: #374151 } /* Name.Variable.Instance -> Dark slate */
.codehilite .vm { color: #374151 } /* Name.Variable.Magic -> Dark slate */
.codehilite .il { color: #7c3aed } /* Literal.Number.Integer.Long -> Purple */
"""

    # Tool widget styles
    TOOL_WIDGET = """
QWidget {
    background-color: transparent;
}
"""

    TOOL_CARD = """
QFrame#toolCard {
    border-radius: 6px;
    background-color: rgba(107, 70, 193, 0.08); /* Subtle deep purple transparency */
    border: 1px solid rgba(107, 70, 193, 0.4); /* Softer purple border */
    padding: 1px;
}
"""

    TOOL_CARD_ERROR = """
QFrame#toolCard {
    border-radius: 6px;
    background-color: rgba(239, 68, 68, 0.08); /* Subtle red transparency */
    border: 1px solid rgba(239, 68, 68, 0.4); /* Softer red border */
    padding: 1px;
}
"""

    TOOL_HEADER = """
QLabel {
    font-weight: 500;
    color: #374151; /* Dark slate */
}
"""

    TOOL_TOGGLE_BUTTON = """
QPushButton {
    background-color: transparent;
    border: none;
    color: #6b7280; /* Gray */
    font-weight: normal;
    font-size: 11px;
}
QPushButton:hover {
    color: #6b46c1; /* Deep purple */
}
"""

    TOOL_STATUS = """
QLabel {
    font-weight: 500;
    padding: 2px;
    font-size: 11px;
}
QLabel[status="running"] {
    color: #d97706; /* Orange */
}
QLabel[status="complete"] {
    color: #10b981; /* Green */
}
QLabel[status="error"] {
    color: #ef4444; /* Red */
}
"""

    TOOL_CONTENT = """
QLabel {
    color: #374151; /* Dark slate */
    padding: 1px;
    font-size: 11px;
}
QLabel[role="title"] {
    font-weight: 500;
    color: #374151;
    font-size: 12px;
}
QLabel[role="key"] {
    color: #6b46c1; /* Deep purple */
    font-weight: 500;
    font-size: 11px;
}
QLabel[role="value"] {
    color: #6b7280; /* Gray */
    font-size: 11px;
}
QLabel[role="error"] {
    color: #ef4444; /* Red */
    font-size: 11px;
}
"""

    TOOL_PROGRESS = """
QProgressBar {
    border: none;
    background-color: rgba(203, 213, 225, 0.4); /* Light slate with transparency */
    border-radius: 5px;
    text-align: center;
}
QProgressBar::chunk {
    background-color: #6b46c1; /* Deep purple */
    border-radius: 5px;
}
"""

    TOOL_SEPARATOR = """
QFrame {
    background-color: rgba(107, 70, 193, 0.3); /* Deep purple with transparency */
    border: none;
}
"""

    # Tool icons (consistent across all themes)
    TOOL_ICONS = {
        "web_search": "🔍",
        "fetch_webpage": "🌐",
        "transfer": "↗️",
        "adapt": "🧠",
        "retrieve_memory": "💭",
        "forget_memory_topic": "🗑️",
        "analyze_repo": "📂",
        "read_file": "📄",
        "default": "🔧",  # Default icon for unspecified tools
    }

    # JSON Editor styles
    JSON_EDITOR_COLORS = {
        "background": "#ffffff",
        "text": "#374151",
        "border": "#d1d5db",
        "string": "#10b981",  # Green
        "number": "#d97706",  # Orange
        "keyword": "#6b46c1",  # Deep purple
        "punctuation": "#374151",  # Dark slate
        "error": "#ef4444",  # Red
    }

    JSON_EDITOR_STYLE = """
QPlainTextEdit {
    background-color: #ffffff; /* White background */
    color: #374151; /* Dark slate text */
    border: 1px solid #d1d5db; /* Light gray border */
    border-radius: 4px;
    padding: 8px;
    font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
    font-size: 12px;
    line-height: 1.4;
}
QPlainTextEdit:focus {
    border: 1px solid #6b46c1; /* Deep purple focus border */
}
"""

    # Markdown Editor styles
    MARKDOWN_EDITOR_COLORS = {
        "background": "#ffffff",  # White background
        "text": "#374151",  # Dark slate text
        "border": "#d1d5db",  # Light gray border
        "header": "#6b46c1",  # Deep purple for headers
        "bold": "#dc2626",  # Dark red for bold text
        "italic": "#10b981",  # Green for italic text
        "code": "#7c3aed",  # Purple for code blocks
        "code_background": "#f9fafb",  # Very light gray code background
        "link": "#0ea5e9",  # Sky blue for links
        "image": "#06b6d4",  # Cyan for images
        "list": "#d97706",  # Orange for list markers
        "blockquote": "#059669",  # Green for blockquotes
        "hr": "#d1d5db",  # Light gray for horizontal rules
        "strikethrough": "#ef4444",  # Red for strikethrough text
        "error": "#ef4444",  # Red for errors
    }

    MARKDOWN_EDITOR_STYLE = """
QPlainTextEdit {
    background-color: #ffffff; /* White background */
    color: #374151; /* Dark slate text */
    border: 1px solid #d1d5db; /* Light gray border */
    border-radius: 4px;
    padding: 8px;
    font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;
    font-size: 13px;
    line-height: 1.6;
    selection-background-color: #eed5ff; /* Lavender selection */
    selection-color: #374151; /* Dark slate selected text */
}
QPlainTextEdit:focus {
    border: 1px solid #6b46c1; /* Deep purple focus border */
}
"""