from abc import ABC, abstractmethod

from prompt.prompt_priority import PromptPriority


class PromptComponent(ABC):
    priority: PromptPriority | None = None

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if cls.priority is None:
            raise TypeError(
                f"{cls.__name__} must define class variable 'priority'"
            )

    @abstractmethod
    def render(self) -> str:
        pass
