from prompt_component import PromptComponent


class Instruction(PromptComponent):
    def __init__(self, instruction: str):
        self.instruction = instruction

    def render(self) -> str:
        return self.instruction
