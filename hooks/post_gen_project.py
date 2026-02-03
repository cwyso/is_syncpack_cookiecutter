#!/usr/bin/env python
import os
import shutil


def remove_mcp_components():
    """Remove MCP components if not required by user"""
    include_mcp = "{{ cookiecutter.include_mcp_components }}"

    if include_mcp.lower() == "no":
        # Path to the samcp_components directory
        samcp_path = os.path.join(
            "{{ cookiecutter.syncpack_name }}", "samcp_components"
        )

        if os.path.exists(samcp_path):
            try:
                shutil.rmtree(samcp_path)
            except Exception as err:
                print(
                    f"Issue encountered when attempting to remove MCP components: {err}"
                )
        else:
            print(f"MCP components directory not found: {samcp_path}")


if __name__ == "__main__":
    remove_mcp_components()
