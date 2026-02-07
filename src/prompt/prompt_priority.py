from enum import IntEnum


class PromptPriority(IntEnum):
    """
    プロンプト構成要素の表示順序を定義する列挙型。

    数値が小さいほど、最終的なプロンプト内で先に出力される。

    priority は「実装都合の順序」ではなく、
    プロンプトとしての意味的な構造を表現するためのもの。
    """

    COMPOSITE = -1000
    SYSTEM = 100
    INSTRUCTION = 200
    TASK = 250
    CONTEXT = 300
    CODE_CONTEXT = 400
    CONSTRAINT = 500
    PROHIBITED = 600
    OUTPUT_FORMAT = 700
