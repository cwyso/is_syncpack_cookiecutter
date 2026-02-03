from samcp.base_components import BasePrompt

SYNCPACK = "cookie_cutter_syncpack"  # replace with your syncpack name


class DummyPrompt(BasePrompt):

    def __init__(self):
        super().__init__(
            name="Dummy Prompt",
            title="Dummy Prompt",
            description="Dummy Prompt",
            tags=[
                "dummy",
            ],
        )
        self.function_prompt = self.dummy_function
        self.prefix = SYNCPACK

    @staticmethod
    def dummy_function(name: str):
        return f"This is a placeholder which takes an input: {name}. Print the {name}."
