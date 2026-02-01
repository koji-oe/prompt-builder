from prompt.component.code_context_prompt import CodeContextPrompt
from prompt.component.output_format_prompt import OutputFormatPrompt
from prompt.component.prohibited_prompt import ProhibitedPrompt
from prompt.component.prompt_component import PromptComponent
from prompt.component.system_prompt import SystemPrompt
from prompt.component.instruction_prompt import InstructionPrompt
from prompt.component.context_prompt import ContextPrompt
from prompt.component.constraint_prompt import ConstraintPrompt
from prompt.prompt import Prompt


class PromptBuilder():
    """
    Prompt オブジェクトを段階的に組み立てるためのビルダー。

    各メソッドは特定の PromptComponent を追加し、
    メソッドチェーンにより宣言的にプロンプト構造を記述できる。

    ビルダーは順序を保持するが、最終的な表示順序は
    Prompt 側で priority によって制御される。
    """

    def __init__(self):
        self._components: list[PromptComponent] = []

    def system(self, role: str) -> "PromptBuilder":
        self._components.append(SystemPrompt(role))
        return self

    def instruction(self, text: str) -> "PromptBuilder":
        self._components.append(InstructionPrompt(text))
        return self

    def context(self, text: str) -> "PromptBuilder":
        self._components.append(ContextPrompt(text))
        return self

    def constraints(self, constraints: list[str]) -> "PromptBuilder":
        self._components.append(ConstraintPrompt(constraints))
        return self

    def output_format(self, format: str) -> "PromptBuilder":
        self._components.append(OutputFormatPrompt(format))
        return self

    def prohibit(self, items: list[str]) -> "PromptBuilder":
        self._components.append(ProhibitedPrompt(items))
        return self

    def code(self, path: str, code: str) -> "PromptBuilder":
        self._components.append(CodeContextPrompt(path, code))
        return self

    def build(self) -> Prompt:
        return Prompt(self._components)
