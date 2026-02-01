from prompt_component import PromptComponent


class ConstraintPrompt(PromptComponent):
    def __init__(self, constraints: list[str]):
        self.constraints = constraints

    def render(self) -> str:
        return f"## 制約\n{"\n".join(f"- {c}" for c in self.constraints)}"
