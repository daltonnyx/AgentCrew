import sys


def copy_html_to_clipboard(html_content):
    if sys.platform != "darwin":
        raise NotImplementedError("This function is only implemented for MacOS.")

    from AppKit import NSPasteboard
    from Foundation import NSString

    pb = NSPasteboard.generalPasteboard()
    pb.clearContents()
    nshtml = NSString.stringWithString_(html_content)
    # Use the public.html UTI for HTML content:
    pb.declareTypes_owner_(["public.html"], None)
    pb.setString_forType_(nshtml, "public.html")
    print("Copied as formatted HTML (macOS)")
