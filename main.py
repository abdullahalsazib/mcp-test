from mcp.server.fastmcp import FastMCP

# Initialize MCP server
mcp = FastMCP("abdullah 🚀")

# Define a simple tool
@mcp.tool()
def addNumber(a: int, b: int) -> dict:
    """Add two numbers"""
    return {"result": a + b}

# Run the MCP server when executed
if __name__ == "__main__":
    # Run with HTTP transport (works in FastMCP Cloud)
    mcp.run("http", port=8000)
