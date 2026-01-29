from samcp.base_components import BaseResource

SYNCPACK = "cookie_cutter_syncpack"  # replace with your syncpack name


class DummyResource(BaseResource):

    def __init__(self):
        super().__init__(
            uri=f"resource://dummy",
            name="dummy",
            description="dummy",
            tags=[
                "dummy",
            ],
        )
        self.function_resource = self.dummy_function
        self.prefix = SYNCPACK

    @staticmethod
    def dummy_function():
        return "hello world"
