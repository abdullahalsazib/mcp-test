from mcp.server.fastmcp import FastMCP

# Initialize MCP server
mcp = FastMCP(name="abdullah", stateless_http=True)

def _ok(result):
    return {"ok": True, "data": result, "error": None, "meta": {}}

def _err(message: str, code: str = "VALIDATION_ERROR"):
    return {"ok": False, "data": None, "error": {"message": message, "code": code}, "meta": {}}

# Define a simple tool
@mcp.tool()
def addNumber(a: int, b: int) -> dict:
    """Add two numbers"""
    return _ok({"result": a + b})
@mcp.tool()
def addSub(a: int, b: int) -> dict:
    """Subtract two numbers"""
    return _ok({"result": a - b})
@mcp.tool()
def addMul(a: int, b: int) -> dict:
    """Multiply two numbers"""
    return _ok({"result": a * b})
@mcp.tool()
def addDiv(a: int, b: int) -> dict:
    """Divide two numbers"""
    if b == 0:
        return _err("division by zero", code="MATH_ERROR")
    return _ok({"result": a / b})


