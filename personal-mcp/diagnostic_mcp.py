"""Diagnostic script to test server MCP protocol compatibility."""

import subprocess
import sys
import time
import json
import threading

def test_server_connection():
    """Test if the server can handle MCP protocol messages."""
    
    # Start the server process
    proc = subprocess.Popen(
        [sys.executable, "-m", "fastmcp", "run", "src/personal_mcp/server.py:mcp", "--transport", "stdio"],
        cwd="C:\\Users\\cuong\\workspace\\ToolBelt\\personal-mcp",
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1
    )
    
    try:
        # Send initialize message
        init_msg = json.dumps({
            "jsonrpc": "2.0",
            "id": 1,
            "method": "initialize",
            "params": {
                "protocolVersion": "2024-11-05",
                "capabilities": {},
                "clientInfo": {"name": "test-client", "version": "1.0"}
            }
        })
        
        print(f"Sending: {init_msg}", file=sys.stderr)
        proc.stdin.write(init_msg + "\n")
        proc.stdin.flush()
        
        # Read response with timeout
        def read_output():
            try:
                line = proc.stdout.readline()
                if line:
                    print(f"Received: {line}", file=sys.stderr)
                    return json.loads(line)
            except Exception as e:
                print(f"Error reading: {e}", file=sys.stderr)
            return None
        
        # Give it 3 seconds to respond
        response = None
        start = time.time()
        while time.time() - start < 3:
            response = read_output()
            if response:
                break
            time.sleep(0.1)
        
        if response:
            print(json.dumps({"status": "success", "response": response}), file=sys.stderr)
        else:
            print(json.dumps({"status": "no_response", "timeout": 3}), file=sys.stderr)
            # Check if process is still alive
            if proc.poll() is not None:
                stderr = proc.stderr.read()
                print(json.dumps({"status": "process_exited", "stderr": stderr}), file=sys.stderr)
    
    finally:
        proc.terminate()
        try:
            proc.wait(timeout=2)
        except subprocess.TimeoutExpired:
            proc.kill()

if __name__ == "__main__":
    test_server_connection()
