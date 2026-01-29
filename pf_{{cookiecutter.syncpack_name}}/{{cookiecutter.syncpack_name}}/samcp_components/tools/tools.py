from typing import Dict, Any

from samcp.base_components import BaseTool

SYNCPACK = "cookie_cutter_syncpack"  # replace with your syncpack name


class DummyTool(BaseTool):
    def __init__(self):
        super().__init__(
            name="dummy_tool",
            description="Dummy Tool",
            tags=["dummy"],
        )
        self.function_tool = self.dummy_function
        self.prefix = SYNCPACK

    @staticmethod
    def dummy_function(name: str, config: str) -> Dict[str, Any]:
        return {"name": name, "run": config}
