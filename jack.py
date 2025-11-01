from mcp.server.fastmcp import FastMCP

# Initialize MCP server
mcp2 = FastMCP(name="jack", stateless_http=True)

# Define a simple tool
@mcp2.tool()
def showHello(name: str) -> dict:
    """Show a hello message"""
    return {"result": f"Hello, {name}!"}

