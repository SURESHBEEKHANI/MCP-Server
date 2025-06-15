from mcp.server.fastmcp import FastMCP

mcp=FastMCP("math server")

# Define a tool for addition
@mcp.tool()
def add(a: int, b: int) -> int:
    """Adds two integers."""
    return a + b

# Define a tool for subtraction
@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtracts the second integer from the first."""
    return a - b

# Define a tool for multiplication
@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiplies two integers."""
    return a * b

# Define a tool for division
@mcp.tool()
def divide(a: int, b: int) -> float:
    """Divides the first integer by the second."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

# Run the MCP server with stdio transport if the script is executed directly
#The transport="stdio" argument tells the server to:
#Use standard input/output (stdin and stdout) to receive and respond to tool function calls.

if __name__=="__main__":
    mcp.run(transport="stdio")