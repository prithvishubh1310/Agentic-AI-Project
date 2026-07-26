"""
==================================================
SIMPLE FLOWISE MCP SERVER
==================================================

Purpose:
    1. Wrap Flowise endpoint as MCP Tool
    2. Expose tool via MCP Server
    3. Demonstrate MCP integration

Requirements:

    pip install fastmcp
    pip install requests

Run:

    python simple_flowise_mcp_server.py

==================================================
"""

import requests

from fastmcp import FastMCP


# ==================================================
# CONFIGURATION
# ==================================================

FLOWISE_API_URL = (
    "https://cloud.flowiseai.com/"
    "api/v1/prediction/"
    "c7f91a50-e934-4842-80a8-539738a31cd9"
)


# ==================================================
# MCP SERVER
# ==================================================

mcp = FastMCP(
    name="simple-flowise-server"
)


# ==================================================
# TOOL 1
# ==================================================

@mcp.tool
def health_check():

    """
    Simple health check.
    """

    return {
        "status": "healthy"
    }


# ==================================================
# TOOL 2
# ==================================================

@mcp.tool
def ask_cis_windows11(
    question: str
):

    """
    Query CIS Windows 11
    knowledge base through Flowise.
    """

    payload = {
        "question": question
    }

    response = requests.post(
        #r"http://127.0.0.1:8000/ask",
        FLOWISE_API_URL,
        json=payload,
        timeout=60
    )

    response.raise_for_status()

    return response.json()


# ==================================================
# MAIN
# ==================================================

if __name__ == "__main__":

    print(
        "\nStarting MCP Server..."
    )

    print(
        "\nRegistered Tools:"
    )

    print(
        "- health_check"
    )

    print(
        "- ask_cis_windows11"
    )

    mcp.run()