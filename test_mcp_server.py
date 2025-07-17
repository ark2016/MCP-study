from mcp.server.fastmcp import FastMCP

# Создаем простейший сервер для тестирования
mcp = FastMCP("TestMCP")

@mcp.tool(
    name="hello",
    description="Say hello",
)
def hello() -> str:
    return "Hello from MCP!"

if __name__ == "__main__":
    mcp.run(transport="stdio")