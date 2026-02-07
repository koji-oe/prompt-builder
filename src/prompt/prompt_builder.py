from collections.abc import Callable
from prompt.component.code_context_prompt import CodeContextPrompt
from prompt.component.output_format_prompt import OutputFormatPrompt
from prompt.component.prohibited_prompt import ProhibitedPrompt
from prompt.component.prompt_component import PromptComponent
from prompt.component.system_prompt import SystemPrompt
from prompt.component.instruction_prompt import InstructionPrompt
from prompt.component.context_prompt import ContextPrompt
from prompt.component.constraint_prompt import ConstraintPrompt
from prompt.component.task_prompt import TaskPrompt
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
        """
        空の PromptBuilder を生成する。
        """
        self._components: list[PromptComponent] = []

    def system(self, role: str) -> "PromptBuilder":
        """
        AI に与えるシステムロール（役割）を追加する。

        例:
            「熟練したJavaアーキテクト」
            「セキュリティ専門家」

        Args:
            role: AI に期待する役割や立場

        Returns:
            自身（メソッドチェーン用）
        """
        self._components.append(SystemPrompt(role))
        return self

    def instruction(self, text: str) -> "PromptBuilder":
        """
        AI に対する主指示（何をしてほしいか）を追加する。

        プロンプトの中核となる命令文を表す。

        Args:
            text: 実行してほしい指示内容

        Returns:
            自身（メソッドチェーン用）
        """
        self._components.append(InstructionPrompt(text))
        return self

    def context(self, text: str) -> "PromptBuilder":
        """
        AI が判断するための前提情報・背景情報を追加する。

        業務背景、システム構成、目的などを記述する用途を想定。

        Args:
            text: 前提情報や文脈説明

        Returns:
            自身（メソッドチェーン用）
        """
        self._components.append(ContextPrompt(text))
        return self

    def constraints(self, constraints: list[str]) -> "PromptBuilder":
        """
        AI が守るべき制約条件を追加する。

        技術要件や前提条件などを箇条書きで指定する。

        Args:
            constraints: 制約条件のリスト

        Returns:
            自身（メソッドチェーン用）
        """
        self._components.append(ConstraintPrompt(constraints))
        return self

    def output_format(self, format: str) -> "PromptBuilder":
        """
        AI の出力形式を指定する。

        例:
            - 箇条書き
            - diff 形式
            - ファイル単位で出力

        Args:
            format: 出力形式の説明

        Returns:
            自身（メソッドチェーン用）
        """
        self._components.append(OutputFormatPrompt(format))
        return self

    def prohibit(self, items: list[str]) -> "PromptBuilder":
        """
        AI が行ってはいけない禁止事項を追加する。

        制約とは別に、明示的に禁止したい振る舞いを指定する。

        Args:
            items: 禁止事項のリスト

        Returns:
            自身（メソッドチェーン用）
        """
        self._components.append(ProhibitedPrompt(items))
        return self

    def code(self, path: str, code: str) -> "PromptBuilder":
        """
        ファイルパスとコード内容を文脈情報として追加する。

        主にコードレビュー、修正指示、設計相談用途を想定。

        Args:
            path: ファイルの相対パスや識別名
            code: ファイルのコード内容

        Returns:
            自身（メソッドチェーン用）
        """
        self._components.append(CodeContextPrompt(path, code))
        return self

    def task(self, title: str, action: Callable[["TaskPrompt"], None]) -> "PromptBuilder":
        """
        タスク手順全体を表す TaskPrompt を追加する。

        Args:
            title: タスク手順のタイトル
            action: TaskPrompt に対する操作を行うコールバック関数

        Returns:
            自身（メソッドチェーン用）
        """
        task_prompt = TaskPrompt(title)
        action(task_prompt)
        self._components.append(task_prompt)
        return self

    def when(self, condition: bool, action: Callable[["PromptBuilder"], None]) -> "PromptBuilder":
        """
        条件が True の場合のみ、Builder に対する操作を実行する。

        条件分岐を Builder の外に漏らさず、
        fluent API を保ったまま動的なプロンプト構築を可能にする。

        Args:
            condition: 実行条件
            action: 条件成立時に実行される Builder 操作

        Returns:
            自身（メソッドチェーン用）
        """
        if condition:
            action(self)
        return self

    def build(self) -> Prompt:
        """
        追加された PromptComponent から Prompt を生成する。

        Returns:
            完成した Prompt オブジェクト
        """
        return Prompt(self._components)
