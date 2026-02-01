from prompt.component.prompt_component import PromptComponent
from typing import override


class SystemPrompt(PromptComponent):
    def __init__(self, role: str):
        self.role = role

    @override
    def render(self) -> str:
        return f"あなたは{self.role}です。"
