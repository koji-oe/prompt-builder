from abc import abstractmethod
from prompt.component.prompt_component import PromptComponent
from prompt.prompt_priority import PromptPriority


class CompositePromptComponent(PromptComponent):
    """子コンポーネントを保持できる PromptComponent の基底クラス。"""
    priority = PromptPriority.COMPOSITE

    def __init__(self):
        self._children: list[PromptComponent] = []

    def add(self, component: PromptComponent) -> "CompositePromptComponent":
        """子コンポーネントを追加する。

        Args:
            component (PromptComponent): 追加する子コンポーネント
        """
        self._children.append(component)
        return self

    @property
    def children(self) -> tuple[PromptComponent, ...]:
        """子コンポーネントのタプルを返す。

        Returns:
            tuple[PromptComponent, ...]: 子コンポーネントのタプル
        """
        return tuple(self._children)

    @abstractmethod
    def render(self) -> str:
        pass
