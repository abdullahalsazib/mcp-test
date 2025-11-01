from mcp.server.fastmcp import FastMCP

# Initialize MCP server
mcp = FastMCP(name="abdullah", stateless_http=True)

# Define a simple tool
@mcp.tool()
def addNumber(a: int, b: int) -> dict:
    """Add two numbers"""
    return {"result": a + b}
