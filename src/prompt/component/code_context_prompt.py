from prompt.component.prompt_component import PromptComponent
from typing import override

from prompt.prompt_priority import PromptPriority


class CodeContextPrompt(PromptComponent):
    """
    コードやファイル内容を文脈として提示するプロンプト要素。

    特定のファイルパスとコード内容をセットで渡すことで、
    AI に対して「どのコードについて考えるべきか」を明確にする。
    主にコードレビューや修正指示用途を想定している。
    """

    priority = PromptPriority.CODE_CONTEXT

    def __init__(self, path: str, code: str):
        self.path = path
        self.code = code

    @override
    def render(self) -> str:
        return f"""## ファイル: {self.path}
```
{self.code}
```"""
