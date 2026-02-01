from abc import ABC, abstractmethod


class PromptComponent(ABC):
    @abstractmethod
    def render(self) -> str:
        pass
