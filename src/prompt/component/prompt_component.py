from abc import ABC, abstractmethod

from prompt.prompt_priority import PromptPriority


class PromptComponent(ABC):
    """
    プロンプトを構成する各要素の基底クラス。

    PromptComponent は、システムロール・前提情報・制約・コード文脈など、
    プロンプトを構造化するための最小単位を表す。

    各コンポーネントは以下の責務を持つ：
    - 自身の内容を文字列としてレンダリングする
    - プロンプト全体における表示順序を priority で宣言する
    """

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
