# Information
Personal MCP Server has many tools for AI Agent.

# Setup

### Init project    

```bash
> uv init --project .
```

- Run
    ```bash
    > uv run python -m personal_mcp.main
    ```

- Run Dev
    ```bash
    > uv run fastmcp dev src/personal_mcp/server.py
    ```

- Run publish/cached package
    ```bash
    > uvx --from . personal-mcp
    ```

- Integrations
    ```json
    {
        "mcpServers": {
            "My Server": {
            "command": "uv",
            "args": [
                "run",
                "--with",
                "fastmcp", 
                "fastmcp",
                "run",
                "/absolute/path/to/server.py"
            ]
            }
        }
    }
    ```
- Test
    ```bash
    # Simply run pytest --inline-snapshot=fix,create to fill in the snapshot() with actual data.
    pytest --inline-snapshot=fix,create
    
    # Run all tests
    uv run pytest

    # Run specific test file
    uv run pytest tests/server/test_auth.py

    # Run with coverage
    uv run pytest --cov=fastmcp
    ```



### Setup MCPs

#### Serena

- Add MCP
```json
"serena": {
        "type": "stdio",
        "command": "uvx",
        "args": [
            "--from",
            "git+https://github.com/oraios/serena",
            "serena",
            "start-mcp-server",
            "--context",
            "ide-assistant",
            "--project",
            "${workspaceFolder}"
        ]
    }
```

- Register Project
```Bash
> uvx --from git+https://github.com/oraios/serena serena project create --index
```