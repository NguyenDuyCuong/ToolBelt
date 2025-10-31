import asyncio
import argparse
from typing import Literal
from vnstock_wraper.server import create_mcp_server

def main():
    """
    Main entry point for the trading MCP server.
    Supports multiple transport modes: stdio, sse, http, streamablehttp
    """
    parser = argparse.ArgumentParser(description='Trading MCP Server')
    parser.add_argument(
        '--transport', 
        type=str,
        choices=['stdio', 'sse', 'http', 'streamablehttp'],
        default='http',
        help='Transport mode for the server'
    )
    parser.add_argument(
        '--port',
        type=int,
        default=8000,
        help='Port number for http/sse modes'
    )
    parser.add_argument(
        '--log-level',
        type=str,
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'],
        default='INFO',
        help='Logging level'
    )

    args = parser.parse_args()
    
    # Create and run MCP server
    mcp_server = create_mcp_server()
    asyncio.run(mcp_server.run_async(
        transport=args.transport,
        port=args.port,
        log_level=args.log_level
    ))


if __name__ == "__main__":
    main()
