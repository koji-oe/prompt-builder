from prompt.component.prompt_component import PromptComponent
from typing import override


class OutputFormatPrompt(PromptComponent):
    def __init__(self, format: str):
        self.format = format

    @override
    def render(self) -> str:
        return f"## 出力形式\n{self.format}"
