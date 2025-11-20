"""Debug script to check which middleware is causing the issue."""

import sys
sys.path.insert(0, "src")

from fastmcp import FastMCP
from personal_mcp.tools import register_tools
from personal_mcp.prompts import register_prompts

# Create server
mcp = FastMCP("Personal MCP Server - Debug")

# Try registering without middlewares first
try:
    register_tools(mcp)
    print("✓ Tools registered successfully", file=sys.stderr)
except Exception as e:
    print(f"✗ Tools registration failed: {e}", file=sys.stderr)
    import traceback
    traceback.print_exc()

try:
    register_prompts(mcp)
    print("✓ Prompts registered successfully", file=sys.stderr)
except Exception as e:
    print(f"✗ Prompts registration failed: {e}", file=sys.stderr)
    import traceback
    traceback.print_exc()

# Now try with middlewares
try:
    from personal_mcp.middwares import register_middwares
    register_middwares(mcp)
    print("✓ Middlewares registered successfully", file=sys.stderr)
except Exception as e:
    print(f"✗ Middlewares registration failed: {e}", file=sys.stderr)
    import traceback
    traceback.print_exc()

print("All registrations completed!", file=sys.stderr)
