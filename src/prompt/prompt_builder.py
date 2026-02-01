from prompt.component.output_format_prompt import OutputFormatPrompt
from prompt.component.prompt_component import PromptComponent
from prompt.component.system_prompt import SystemPrompt
from prompt.component.instruction_prompt import InstructionPrompt
from prompt.component.context_prompt import ContextPrompt
from prompt.component.constraint_prompt import ConstraintPrompt
from prompt.prompt import Prompt


class PromptBuilder():
    def __init__(self):
        self._components: list[PromptComponent] = []

    def system(self, role: str) -> "PromptBuilder":
        self._components.append(SystemPrompt(role))
        return self

    def instruction(self, text: str) -> "PromptBuilder":
        self._components.append(InstructionPrompt(text))
        return self

    def context(self, text: str) -> "PromptBuilder":
        self._components.append(ContextPrompt(text))
        return self

    def constraints(self, constraints: list[str]) -> "PromptBuilder":
        self._components.append(ConstraintPrompt(constraints))
        return self

    def output_format(self, format: str) -> "PromptBuilder":
        self._components.append(OutputFormatPrompt(format))
        return self

    def build(self) -> Prompt:
        return Prompt(self._components)
