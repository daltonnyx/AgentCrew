"""
Adapters for converting between SwissKnife and A2A message formats.
"""

import base64
from typing import Dict, Any, List, Optional
from a2a.types import (
    GetTaskResponse,
    Message,
    Task,
    TextPart,
    FilePart,
    FileWithBytes,
    FileWithUri,
    Artifact,
    Part,
    SendMessageResponse,
    JSONRPCErrorResponse,
    DataPart,
    Role,
)


# TODO: cover all of cases for images
def convert_a2a_message_to_agent(message: Message) -> Dict[str, Any]:
    """
    Convert an A2A message to SwissKnife format.

    Args:
        message: The A2A message to convert

    Returns:
        The message in SwissKnife format
    """
    role = "user" if message.role == Role.user else "assistant"
    content = []

    for part in message.parts:
        part_data = part.root

        if part_data.kind == "text":
            content.append({"type": "text", "text": part_data.text})
        elif part_data.kind == "file":
            # Handle file content
            file_data = part_data.file
            if isinstance(file_data, FileWithBytes) and file_data.bytes:
                # Base64 encoded file
                content.append(
                    {
                        "type": "file",
                        "file_data": base64.b64decode(file_data.bytes),
                        "file_name": file_data.name or "file",
                        "mime_type": file_data.mimeType or "application/octet-stream",
                    }
                )
            elif isinstance(file_data, FileWithUri) and file_data.uri:
                # File URI
                content.append(
                    {
                        "type": "file_uri",
                        "uri": file_data.uri,
                        "file_name": file_data.name or "file",
                        "mime_type": file_data.mimeType or "application/octet-stream",
                    }
                )
        elif part_data.kind == "data":
            # Convert structured data
            content.append({"type": "data", "data": part_data.data})

    return {"role": role, "content": content}


# TODO: cover all of cases for images
def convert_agent_message_to_a2a(
    message: Dict[str, Any], message_id: Optional[str] = None
) -> Message:
    """
    Convert a SwissKnife message to A2A format.

    Args:
        message: The SwissKnife message to convert
        message_id: Optional message ID

    Returns:
        The message in A2A format
    """
    role = Role.user if message.get("role") == "user" else Role.agent
    parts = []

    content = message.get("content", [])
    if isinstance(content, str):
        # Handle string content (common in some providers)
        parts.append(TextPart(text=content))
    else:
        # Handle list of content parts
        for part in content:
            if isinstance(part, str):
                parts.append(TextPart(text=part))
            elif isinstance(part, dict):
                if part.get("type") == "text":
                    parts.append(TextPart(text=part.get("text", "")))
                elif part.get("type") == "file":
                    # Handle file content
                    parts.append(
                        FilePart(
                            file=FileWithBytes(
                                name=part.get("file_name"),
                                mimeType=part.get("mime_type"),
                                bytes=part.get("file_data", ""),
                            )
                        )
                    )
                elif part.get("type") == "file_uri":
                    # Handle file URI
                    parts.append(
                        FilePart(
                            file=FileWithUri(
                                name=part.get("file_name"),
                                mimeType=part.get("mime_type"),
                                uri=part.get("uri", ""),
                            )
                        )
                    )
                elif part.get("type") == "data":
                    # Handle structured data
                    parts.append(DataPart(data=part.get("data", {})))

    return Message(
        messageId=message_id or f"msg_{hash(str(parts))}",
        role=role,
        parts=parts,
        metadata=message.get("metadata"),
    )


def convert_agent_response_to_a2a_artifact(
    response: str,
    tool_uses: Optional[List[Dict[str, Any]]] = None,
    artifact_id: Optional[str] = None,
) -> Artifact:
    """
    Convert a SwissKnife response to an A2A artifact.

    Args:
        response: The response text from SwissKnife
        tool_uses: Optional list of tool uses
        artifact_id: Optional artifact ID

    Returns:
        The response as an A2A artifact
    """
    parts = [Part(root=TextPart(text=response))]

    # If there were tool uses, we could add them as metadata
    metadata = None
    if tool_uses:
        metadata = {"tool_uses": tool_uses}

    return Artifact(
        artifactId=artifact_id or f"artifact_{hash(response)}",
        parts=parts,
        metadata=metadata,
    )


def convert_agent_response_to_a2a_message(
    response: str,
    tool_uses: Optional[List[Dict[str, Any]]] = None,
    message_id: Optional[str] = None,
    role: Role = Role.agent,
) -> Message:
    """
    Convert a SwissKnife response to an A2A artifact.

    Args:
        response: The response text from SwissKnife
        tool_uses: Optional list of tool uses
        artifact_id: Optional artifact ID

    Returns:
        The response as an A2A artifact
    """
    parts = [Part(root=TextPart(text=response))]

    # If there were tool uses, we could add them as metadata
    metadata = None
    if tool_uses:
        metadata = {"tool_uses": tool_uses}

    return Message(
        messageId=message_id or f"message_{hash(response)}",
        parts=parts,
        metadata=metadata,
        role=role,
    )


def convert_file_to_a2a_part(
    file_path: str, file_content: bytes, mime_type: Optional[str] = None
) -> Part:
    """
    Convert a file to an A2A part.

    Args:
        file_path: The path to the file
        file_content: The content of the file
        mime_type: Optional MIME type

    Returns:
        The file as an A2A part
    """
    import os
    import mimetypes

    if not mime_type:
        mime_type, _ = mimetypes.guess_type(file_path)
        if not mime_type:
            mime_type = "application/octet-stream"

    file_name = os.path.basename(file_path)

    # Encode file content as base64
    base64_content = base64.b64encode(file_content).decode("utf-8")

    return Part(
        root=FilePart(
            file=FileWithBytes(name=file_name, mimeType=mime_type, bytes=base64_content)
        )
    )


def convert_a2a_send_task_response_to_agent_message(
    response: SendMessageResponse | GetTaskResponse, agent_name: str
) -> Optional[str]:
    """Convert A2A response to agent message format"""
    if not response or not hasattr(response, "root"):
        return None

    if isinstance(response.root, JSONRPCErrorResponse):
        return None

    result = response.root.result if hasattr(response.root, "result") else None

    # Handle both Task and Message results
    if isinstance(result, Task) and result.artifacts:
        # Task result with artifacts
        latest_artifact = result.artifacts[-1]
        content_parts = []
        for part in latest_artifact.parts:
            part_data = part.root
            if part_data.kind == "text":
                content_parts.append(part_data.text)
        return "\n".join(content_parts)
    elif isinstance(result, Message) and result.parts:
        # Direct message result
        content_parts = []
        for part in result.parts:
            part_data = part.root
            if part_data.kind == "text":
                content_parts.append(part_data.text)
        return "\n".join(content_parts)

    return None
