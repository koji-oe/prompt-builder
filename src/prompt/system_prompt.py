from prompt_component import PromptComponent


class SystemPrompt(PromptComponent):
    def __init__(self, role: str):
        self.role = role

    def render(self) -> str:
        return f"あなたは{self.role}です。"
