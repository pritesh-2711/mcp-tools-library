"""Local development entrypoint for the research assistant MCP server."""

from server.app import mcp
from server.config import settings


if __name__ == "__main__":
    mcp.run(transport=settings.mcp_transport)
