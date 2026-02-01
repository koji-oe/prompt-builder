from prompt.component.prompt_component import PromptComponent
from typing import override

from prompt.prompt_priority import PromptPriority


class ProhibitedPrompt(PromptComponent):
    priority = PromptPriority.PROHIBITED

    def __init__(self, items: list[str]):
        self.items = items

    @override
    def render(self) -> str:
        return f"## 禁止事項\n{"\n".join(f"- {i}" for i in self.items)}"
