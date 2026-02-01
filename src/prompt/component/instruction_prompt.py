from prompt.component.prompt_component import PromptComponent
from typing import override

from prompt.prompt_priority import PromptPriority


class InstructionPrompt(PromptComponent):
    """
    AI に実行してほしい主指示を表すプロンプト要素。

    プロンプト全体の中核となる命令文を担当する。
    「何をしてほしいか」を最も直接的に表現する部分。
    """

    priority = PromptPriority.INSTRUCTION

    def __init__(self, instruction: str):
        self.instruction = instruction

    @override
    def render(self) -> str:
        return self.instruction
