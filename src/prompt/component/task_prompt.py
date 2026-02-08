from typing import override
from prompt.component.composite_prompt_component import CompositePromptComponent
from prompt.prompt_priority import PromptPriority


class TaskPrompt(CompositePromptComponent):
    """
    作業手順全体を表すプロンプト要素。

    複数の TaskStepPrompt を子要素として保持する。
    """
    priority = PromptPriority.TASK

    def __init__(self, title: str = "作業手順"):
        super().__init__()
        self.title = title

    @override
    def render(self) -> str:
        lines = [f"## {self.title}"]
        for i, child in enumerate(self.children, start=1):
            lines.append(child.render(depth=1, index=i))
        return "\n".join(lines)
