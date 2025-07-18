import sys


def copy_html_to_clipboard(html_content, text_fallback=None):
    """
    Copy HTML content to clipboard as formatted text with fallback to plain text

    Args:
        html_content (str): HTML content to copy
        text_fallback (str): Plain text fallback (optional)
    """
    if sys.platform != "win32":
        raise NotImplementedError("This function is only implemented for Windows.")

    import win32clipboard
    import win32con

    # If no text fallback provided, strip HTML tags
    if text_fallback is None:
        import re

        text_fallback = re.sub("<[^<]+?>", "", html_content)

    # Prepare HTML clipboard format
    html_clipboard_data = prepare_html_clipboard_data(html_content)

    win32clipboard.OpenClipboard()
    try:
        win32clipboard.EmptyClipboard()

        # Set HTML format (for rich text paste)
        html_format = win32clipboard.RegisterClipboardFormat("HTML Format")
        win32clipboard.SetClipboardData(
            html_format, html_clipboard_data.encode("utf-8")
        )

    except Exception:
        # Set plain text format (for fallback)
        win32clipboard.SetClipboardData(win32con.CF_TEXT, text_fallback.encode("utf-8"))

        # Set Unicode text format
        win32clipboard.SetClipboardData(win32con.CF_UNICODETEXT, text_fallback)

    finally:
        win32clipboard.CloseClipboard()


def prepare_html_clipboard_data(html_content):
    """
    Prepare HTML content for Windows clipboard format
    """
    # HTML clipboard format requires specific headers
    html_prefix = """Version:0.9
StartHTML:000000000
EndHTML:000000000
StartFragment:000000000
EndFragment:000000000
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
</head>
<body>
<!--StartFragment-->"""

    html_suffix = """<!--EndFragment-->
</body>
</html>"""

    # Calculate offsets
    start_html = len(html_prefix.split("\n")[0]) + 1  # After version line
    start_fragment = len(html_prefix)
    end_fragment = start_fragment + len(html_content)
    end_html = end_fragment + len(html_suffix)

    # Format the header with correct offsets
    header = f"""Version:0.9
StartHTML:{start_html:09d}
EndHTML:{end_html:09d}
StartFragment:{start_fragment:09d}
EndFragment:{end_fragment:09d}"""

    full_html = f"""{header}
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
</head>
<body>
<!--StartFragment-->{html_content}<!--EndFragment-->
</body>
</html>"""

    return full_html
