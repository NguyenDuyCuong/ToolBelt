#!/usr/bin/env python
"""Quick test to verify server loads with new configuration."""

import subprocess
import time

# Test the new command format
cmd = [
    "uv", "run", "--with", "fastmcp",
    "fastmcp", "run",
    "src/personal_mcp/server.py:mcp",
    "--transport", "stdio"
]

print("Testing server with new configuration...")
print(f"Command: {' '.join(cmd)}")
print()

proc = subprocess.Popen(
    cmd,
    cwd="C:\\Users\\cuong\\workspace\\ToolBelt\\personal-mcp",
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    text=True,
    bufsize=1
)

print("Server output:")
start = time.time()
while time.time() - start < 5:  # Run for 5 seconds
    line = proc.stdout.readline()
    if line:
        print(line.rstrip())
    if proc.poll() is not None:
        print(f"Process exited with code: {proc.returncode}")
        break

if proc.poll() is None:
    print("✓ Server is still running after 5 seconds (good!)")
    proc.terminate()
    try:
        proc.wait(timeout=2)
    except subprocess.TimeoutExpired:
        proc.kill()
else:
    print("✗ Server exited - this might be the issue")
