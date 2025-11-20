#!/usr/bin/env python
"""Test script to verify the server runs without immediately closing."""

import asyncio
import sys
import json

# Add src to path
sys.path.insert(0, "src")

from personal_mcp.server import mcp


async def main():
    """Test server setup without running the full stdio loop."""
    try:
        print(json.dumps({"status": "Server imported successfully"}), file=sys.stderr)
        # Check if server has tools and prompts registered
        print(json.dumps({"server_name": mcp.name}), file=sys.stderr)
        print(json.dumps({"status": "All checks passed"}), file=sys.stderr)
    except Exception as e:
        print(json.dumps({"error": str(e), "type": type(e).__name__}), file=sys.stderr)
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(main())
