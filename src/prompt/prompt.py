from prompt.component.prompt_component import PromptComponent


class Prompt:
    def __init__(self, components: list[PromptComponent]):
        self._components = tuple(components)

    def render(self) -> str:
        return "\n\n".join(c.render() for c in self._components)
