from prompt.component.prompt_component import PromptComponent
from typing import override

from prompt.prompt_priority import PromptPriority


class ContextPrompt(PromptComponent):
    """
    AI が判断する際の前提情報・背景情報を表すプロンプト要素。

    業務背景やシステム状況など、
    指示を正しく理解するために必要な文脈を提供する。
    """

    priority = PromptPriority.CONTEXT

    def __init__(self, context: str):
        self.context = context

    @override
    def render(self) -> str:
        return f"## 前提情報\n{self.context}"
