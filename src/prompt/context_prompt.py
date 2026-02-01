from prompt_component import PromptComponent


class ContextPrompt(PromptComponent):
    def __init__(self, context: str):
        self.context = context

    def render(self) -> str:
        return f"## 前提情報\n{self.context}"
