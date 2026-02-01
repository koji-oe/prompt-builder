from prompt.component.prompt_component import PromptComponent
from typing import override

from prompt.prompt_priority import PromptPriority


class InstructionPrompt(PromptComponent):
    priority = PromptPriority.INSTRUCTION

    def __init__(self, instruction: str):
        self.instruction = instruction

    @override
    def render(self) -> str:
        return self.instruction
