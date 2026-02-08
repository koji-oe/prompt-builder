from typing import Iterable, override
from prompt.component.composite_prompt_component import CompositePromptComponent
from prompt.prompt_priority import PromptPriority


class TaskStepPrompt(CompositePromptComponent):
    """
    見出し階層で表現される作業ステップ。

    - title: 見出しタイトル
    - content: 見出し直下の説明（複数行可）
    """
    priority = PromptPriority.TASK

    def __init__(self, title: str, content: str | None = None):
        super().__init__()
        self.title = title
        self.content = content

    @override
    def render(self, *, depth: int, number_path: Iterable[int]) -> str:
        heading_level = depth + 2
        number = ".".join(map(str, number_path))

        lines: list[str] = []
        lines.append(f"{'#' * heading_level} {number}. {self.title}")

        if self.content:
            lines.append(self.content.strip())

        for i, child in enumerate(self.children, start=1):
            lines.append(
                child.render(
                    depth=depth + 1,
                    number_path=[*number_path, i],
                )
            )

        return "\n\n".join(lines)
