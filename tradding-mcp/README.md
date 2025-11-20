## RUN

```bash
uv --no-cache --directory C:\Users\cuong\workspace\ToolBelt\tradding-mcp run main.py
```

## Setting MCP

- Run as sse to bypass vnstock limit
```bash
uv --no-cache --directory C:\Users\cuong\workspace\ToolBelt\tradding-mcp run main.py    
```
- Setting MCP
```json
"tradding-mcp": {
    "url": "http://127.0.0.1:8000/sse"
}
```