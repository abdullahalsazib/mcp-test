from mcp.server.fastmcp import FastMCP

mcp = FastMCP("abdullah 🚀")

@mcp.tool()
def addNumber(a: int, b: int) -> dict:
    """Add two numbers"""
    return { "result": a + b }

if __name__ == "__main__":
    mcp.run("stdio")