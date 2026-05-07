"""Local development entrypoint for the research assistant MCP server."""

import signal
import sys

from server.app import mcp
from server.config import settings


def _handle_shutdown(*_):
    print("\nMCP server stopped.", file=sys.stderr, flush=True)
    sys.exit(0)


signal.signal(signal.SIGINT, _handle_shutdown)
signal.signal(signal.SIGTERM, _handle_shutdown)


if __name__ == "__main__":
    print("Starting MCP server...")
    try:
        mcp.run(transport=settings.mcp_transport)
    except KeyboardInterrupt:
        print("\nMCP server stopped.", file=sys.stderr, flush=True)
        sys.exit(0)
