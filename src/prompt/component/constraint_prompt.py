from prompt.component.prompt_component import PromptComponent
from typing import override


class ConstraintPrompt(PromptComponent):
    def __init__(self, constraints: list[str]):
        self.constraints = constraints

    @override
    def render(self) -> str:
        return f"## 制約\n{"\n".join(f"- {c}" for c in self.constraints)}"
