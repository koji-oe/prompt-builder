from prompt.component.prompt_component import PromptComponent
from typing import override

from prompt.prompt_priority import PromptPriority


class CodeContextPrompt(PromptComponent):
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
