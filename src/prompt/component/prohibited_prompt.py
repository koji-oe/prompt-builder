from prompt.component.prompt_component import PromptComponent
from typing import override

from prompt.prompt_priority import PromptPriority


class ProhibitedPrompt(PromptComponent):
    """
    AI が行ってはいけないことを明示するプロンプト要素。

    制約とは別に「禁止事項」として明示することで、
    意図しない振る舞いを抑制する目的で使用する。
    """

    priority = PromptPriority.PROHIBITED

    def __init__(self, items: list[str]):
        self.items = items

    @override
    def render(self) -> str:
        return f"## 禁止事項\n{"\n".join(f"- {i}" for i in self.items)}"
