import os
import logging

def setup_logging():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    )

def main():
    setup_logging()
    logging.info("Starting MCP server...")    
    print("Hello from personal-mcp!!!")

if __name__ == "__main__":
    main()