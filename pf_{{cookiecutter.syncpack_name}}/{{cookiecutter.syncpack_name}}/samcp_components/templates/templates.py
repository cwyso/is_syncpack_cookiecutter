from samcp.base_components import BaseTemplate

SYNCPACK = "cookie_cutter_syncpack"  # replace with your syncpack name


class DummyTemplate(BaseTemplate):

    def __init__(self):
        super().__init__(
            uri_template="resource://dummy/{name}",
            name="Dummy Template",
            title="Dummy Template",
            description="Dummy Template",
            tags=[
                "dummy",
            ],
        )
        self.function_template = self.dummy_function
        self.prefix = SYNCPACK

    @staticmethod
    def dummy_function(name: str):
        return f"This is a placeholder which takes an input: {name}. Print the {name}."
