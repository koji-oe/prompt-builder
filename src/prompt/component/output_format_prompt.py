from prompt.component.prompt_component import PromptComponent
from typing import override

from prompt.prompt_priority import PromptPriority


class OutputFormatPrompt(PromptComponent):
    """
    AI の出力形式を指定するプロンプト要素。

    diff 形式、箇条書き、ファイル単位など、
    出力結果の構造やフォーマットを明示するために使用する。
    """

    priority = PromptPriority.OUTPUT_FORMAT

    def __init__(self, format: str):
        self.format = format

    @override
    def render(self) -> str:
        return f"## 出力形式\n{self.format}"
