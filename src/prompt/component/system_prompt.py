from prompt.component.prompt_component import PromptComponent
from typing import override

from prompt.prompt_priority import PromptPriority


class SystemPrompt(PromptComponent):
    """
    AI に与えるシステムロール（役割）を表すプロンプト要素。

    AI がどのような立場・専門性で振る舞うべきかを明示する目的で使用する。
    通常、プロンプトの先頭に配置される。
    """

    priority = PromptPriority.SYSTEM

    def __init__(self, role: str):
        self.role = role

    @override
    def render(self) -> str:
        return f"あなたは{self.role}です。"
