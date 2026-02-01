from prompt.component.prompt_component import PromptComponent
from typing import override


class InstructionPrompt(PromptComponent):
    def __init__(self, instruction: str):
        self.instruction = instruction

    @override
    def render(self) -> str:
        return self.instruction
