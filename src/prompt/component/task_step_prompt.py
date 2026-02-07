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
    def render(self) -> str:
        if not self.children:
            return self.title

        lines = [self.title]
        for child in self.children:
            rendered = child.render()
            lines.append(f"  - {rendered}")
        return "\n".join(lines)
