from a2a.types import (
    ContentTypeNotSupportedError,
    JSONRPCErrorResponse,
    JSONRPCResponse,
    UnsupportedOperationError,
)


def are_modalities_compatible(
    server_output_modes: list[str], client_output_modes: list[str]
):
    """Modalities are compatible if they are both non-empty
    and there is at least one common element.
    """
    if client_output_modes is None or len(client_output_modes) == 0:
        return True

    if server_output_modes is None or len(server_output_modes) == 0:
        return True

    return any(x in server_output_modes for x in client_output_modes)


def new_incompatible_types_error(request_id):
    return JSONRPCResponse(
        root=JSONRPCErrorResponse(id=request_id, error=ContentTypeNotSupportedError())
    )


def new_not_implemented_error(request_id):
    return JSONRPCResponse(
        root=JSONRPCErrorResponse(id=request_id, error=UnsupportedOperationError())
    )
