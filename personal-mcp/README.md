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
- Run publish/cached package
    ```bash
    > uvx --from . personal-mcp
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