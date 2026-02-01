from prompt.component.prompt_component import PromptComponent
from typing import override

from prompt.prompt_priority import PromptPriority


class OutputFormatPrompt(PromptComponent):
    priority = PromptPriority.OUTPUT_FORMAT

    def __init__(self, format: str):
        self.format = format

    @override
    def render(self) -> str:
        return f"## 出力形式\n{self.format}"
