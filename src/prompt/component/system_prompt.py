from prompt.component.prompt_component import PromptComponent
from typing import override

from prompt.prompt_priority import PromptPriority


class SystemPrompt(PromptComponent):
    priority = PromptPriority.SYSTEM

    def __init__(self, role: str):
        self.role = role

    @override
    def render(self) -> str:
        return f"あなたは{self.role}です。"
