from typing import override
from prompt.component.composite_prompt_component import CompositePromptComponent
from prompt.prompt_priority import PromptPriority


class TaskStepPrompt(CompositePromptComponent):
    """
    作業手順の各ステップを表すプロンプト要素。

    TaskPrompt の子要素として使用される。
    """
    priority = PromptPriority.TASK

    def __init__(self, title: str):
        super().__init__()
        self.title = title

    @override
    def render(self, depth: int = 0, index: int | None = None) -> str:
        indent = "  " * (depth - 1) if depth > 0 else ""
        prefix = f"{index}. " if index is not None else "- "

        lines = [f"{indent}{prefix}{self.title}"]

        for i, child in enumerate(self.children, start=1):
            lines.append(child.render(depth=depth + 1, index=i))
        return "\n".join(lines)
