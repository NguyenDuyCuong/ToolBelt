"""
Middleware registration for the personal MCP server.
"""

from fastmcp.server.middleware.logging import (
    LoggingMiddleware
)
from fastmcp.server.middleware.error_handling import (
    ErrorHandlingMiddleware
)
from fastmcp.server.middleware.timing import (
    DetailedTimingMiddleware
)

def register_middwares(mcp):
    """
    Register middlewares to enhance server capabilities.
    """
    # Comprehensive error logging and transformation
    mcp.add_middleware(ErrorHandlingMiddleware(
        include_traceback=True,
        transform_errors=True
    ))

    # Detailed per-operation timing (tools, resources, prompts)
    mcp.add_middleware(DetailedTimingMiddleware())

    # Human-readable logging with payload support
    mcp.add_middleware(LoggingMiddleware(
        include_payloads=True,
        max_payload_length=1000
    ))
