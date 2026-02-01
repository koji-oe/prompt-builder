from prompt.component.prompt_component import PromptComponent
from typing import override

from prompt.prompt_priority import PromptPriority


class ConstraintPrompt(PromptComponent):
    """
    AI の振る舞いを制限する条件を表すプロンプト要素。

    技術要件や前提条件など、
    守るべき制約を箇条書き形式で明示する。
    """

    priority = PromptPriority.CONSTRAINT

    def __init__(self, constraints: list[str]):
        self.constraints = constraints

    @override
    def render(self) -> str:
        return f"## 制約\n{"\n".join(f"- {c}" for c in self.constraints)}"
