"""MCP server definition for the research assistant tools hub."""

from mcp.server.fastmcp import FastMCP

from .config import settings
from .tools import register_tools

mcp = FastMCP(settings.mcp_server_name)
register_tools(mcp)
