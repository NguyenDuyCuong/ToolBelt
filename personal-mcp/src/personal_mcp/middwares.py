"""
Middleware registration for the personal MCP server.
"""

from typing import Callable
from fastmcp.server.middleware.logging import (
    LoggingMiddleware
)
from fastmcp.server.middleware.error_handling import (
    ErrorHandlingMiddleware
)
from fastmcp.server.middleware.timing import (
    DetailedTimingMiddleware
)
import pandas as pd


class MarkdownFormatterMiddleware:
    """
    Middleware to format tool responses as markdown strings.
    Wraps pandas.DataFrame responses in markdown tables.
    """
    def __init__(self, enable_markdown: bool = True):
        self.enable_markdown = enable_markdown

    async def __call__(self, request, call_next):
        response = await call_next(request)
        if self.enable_markdown and hasattr(response, 'to_markdown'):
            markdown = response.to_markdown(index=False, tablefmt="grid")
            return f"```markdown\n{markdown}\n```"
        if response is None:
            return "No data available."
        if isinstance(response, str) and response.startswith("Error"):
            return response
        return response

def register_middwares(mcp):
    """
    Register middlewares to enhance server capabilities.
    """
    # Markdown formatter middleware - formats responses as markdown strings (apply first)
    mcp.add_middleware(MarkdownFormatterMiddleware(enable_markdown=True))

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
