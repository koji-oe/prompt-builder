from prompt.component.prompt_component import PromptComponent


class Prompt:
    """
    複数の PromptComponent から構成される最終的なプロンプト表現。

    内部的には PromptComponent の集合を保持し、
    priority に基づいて並び替えた上で文字列としてレンダリングする。

    このクラス自体は「どう組み立てるか」には関与せず、
    純粋に完成したプロンプトの表現を責務とする。
    """

    def __init__(self, components: list[PromptComponent]):
        self._components = tuple(components)

    def render(self) -> str:
        components = sorted(self._components, key=lambda c: c.priority)
        return "\n\n".join(c.render() for c in components)
