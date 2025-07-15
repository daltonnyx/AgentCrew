"""
Tool display handlers for console UI.
Handles rendering of tool-related information like tool use, results, errors, and confirmations.
"""

import json
from typing import Dict
from rich.console import Console
from rich.text import Text

from .constants import (
    RICH_STYLE_YELLOW,
    RICH_STYLE_GREEN,
    RICH_STYLE_BLUE,
    RICH_STYLE_RED,
    RICH_STYLE_YELLOW_BOLD,
    RICH_STYLE_GREEN_BOLD,
    RICH_STYLE_RED_BOLD,
)


class ToolDisplayHandlers:
    """Handles display of tool-related information."""

    def __init__(self, console: Console):
        """Initialize the tool display handlers with a console instance."""
        self.console = console

    def get_tool_icon(self, tool_name: str) -> str:
        """Get the appropriate icon for a tool based on its name."""
        tool_icons = {
            "web_search": "🔍",
            "fetch_webpage": "🌐",
            "transfer": "↗️",
            "adapt": "🧠",
            "retrieve_memory": "💭",
            "forget_memory_topic": "🗑️",
            "analyze_repo": "📂",
            "read_file": "📄",
        }
        return tool_icons.get(tool_name, "🔧")

    def display_tool_use(self, tool_use: Dict):
        """Display information about a tool being used."""
        tool_icon = self.get_tool_icon(tool_use["name"])

        # Display tool header with better formatting
        header = Text(f"\n┌───── {tool_icon} Tool: ", style=RICH_STYLE_YELLOW)
        header.append(tool_use["name"], style=RICH_STYLE_YELLOW_BOLD)
        header.append(" ─────", style=RICH_STYLE_YELLOW)
        self.console.print(header)

        # Format tool input parameters
        if isinstance(tool_use.get("input"), dict):
            self.console.print(Text("│ Parameters:", style=RICH_STYLE_YELLOW))
            for key, value in tool_use["input"].items():
                # Format value based on type
                if isinstance(value, dict) or isinstance(value, list):
                    formatted_value = json.dumps(value, indent=2)
                    # Add indentation to all lines after the first
                    formatted_lines = formatted_value.split("\n")
                    param_text = Text("│ • ", style=RICH_STYLE_YELLOW)
                    param_text.append(key, style=RICH_STYLE_BLUE)
                    param_text.append(": " + formatted_lines[0])
                    self.console.print(param_text)

                    for line in formatted_lines[1:]:
                        indent_text = Text("│     ", style=RICH_STYLE_YELLOW)
                        indent_text.append(line)
                        self.console.print(indent_text)
                else:
                    param_text = Text("│ • ", style=RICH_STYLE_YELLOW)
                    param_text.append(key, style=RICH_STYLE_BLUE)
                    param_text.append(f": {value}")
                    self.console.print(param_text)
        else:
            input_text = Text("│ Input: ", style=RICH_STYLE_YELLOW)
            input_text.append(str(tool_use.get("input", "")))
            self.console.print(input_text)

        self.console.print(Text("└", style=RICH_STYLE_YELLOW))

    def display_tool_result(self, data: Dict):
        """Display the result of a tool execution."""
        tool_use = data["tool_use"]
        tool_result = data["tool_result"]
        tool_icon = self.get_tool_icon(tool_use["name"])

        # Display tool result with better formatting
        header = Text(f"\n┌───── {tool_icon} Tool Result: ", style=RICH_STYLE_GREEN)
        header.append(tool_use["name"], style=RICH_STYLE_GREEN_BOLD)
        header.append(" ─────", style=RICH_STYLE_GREEN)
        self.console.print(header)

        # Format the result based on type
        result_str = str(tool_result)
        # If result is very long, try to format it
        if len(result_str) > 500:
            result_line = Text("│ ", style=RICH_STYLE_GREEN)
            result_line.append(result_str[:500] + "...")
            self.console.print(result_line)

            truncated_line = Text("│ ", style=RICH_STYLE_GREEN)
            truncated_line.append(
                f"(Output truncated, total length: {len(result_str)} characters)"
            )
            self.console.print(truncated_line)
        else:
            # Split by lines to add prefixes
            for line in result_str.split("\n"):
                result_line = Text("│ ", style=RICH_STYLE_GREEN)
                result_line.append(line)
                self.console.print(result_line)

        self.console.print(Text("└", style=RICH_STYLE_GREEN))

    def display_tool_error(self, data: Dict):
        """Display an error that occurred during tool execution."""
        tool_use = data["tool_use"]
        error = data["error"]
        tool_icon = self.get_tool_icon(tool_use["name"])

        # Display tool error with better formatting
        header = Text(f"\n┌───── {tool_icon} Tool Error: ", style=RICH_STYLE_RED)
        header.append(tool_use["name"], style=RICH_STYLE_RED_BOLD)
        header.append(" ─────", style=RICH_STYLE_RED)
        self.console.print(header)

        error_line = Text("│ ", style=RICH_STYLE_RED)
        error_line.append(str(error))
        self.console.print(error_line)

        self.console.print(Text("└", style=RICH_STYLE_RED))

    def display_tool_denied(self, data):
        """Display information about a denied tool execution."""
        tool_use = data["tool_use"]
        denied_text = Text("\n❌ Tool execution denied: ", style=RICH_STYLE_RED)
        denied_text.append(tool_use["name"])
        self.console.print(denied_text)
