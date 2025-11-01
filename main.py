from mcp.server.fastmcp import FastMCP

# Initialize MCP server
mcp = FastMCP(name="abdullah", stateless_http=True)

# Define a simple tool
@mcp.tool()
def addNumber(a: int, b: int) -> dict:
    """Add two numbers"""
    return {"result": a + b}
@mcp.tool()
def addSub(a: int, b: int) -> dict:
    """Subtract two numbers"""
    return {"result": a - b}
@mcp.tool()
def addMul(a: int, b: int) -> dict:
    """Multiply two numbers"""
    return {"result": a * b}
@mcp.tool()
def addDiv(a: int, b: int) -> dict:
    """Divide two numbers"""
    return {"result": a / b}


