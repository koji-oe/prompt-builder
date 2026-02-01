from prompt.component.prompt_component import PromptComponent
from typing import override

from prompt.prompt_priority import PromptPriority


class ContextPrompt(PromptComponent):
    priority = PromptPriority.CONTEXT

    def __init__(self, context: str):
        self.context = context

    @override
    def render(self) -> str:
        return f"## 前提情報\n{self.context}"
