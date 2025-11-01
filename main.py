from mcp.server.fastmcp import FastMCP

# Initialize MCP server
mcp = FastMCP("abdullah", host="0.0.0.0", port=8000)

# Define a simple tool
@mcp.tool()
def addNumber(a: int, b: int) -> dict:
    """Add two numbers"""
    return {"result": a + b}

# Run the MCP server when executed
if __name__ == "__main__":
    # Run with HTTP transport (works in FastMCP Cloud)
    mcp.run("streamable-http")
