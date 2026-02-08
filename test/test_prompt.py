from prompt.component.task_step_prompt import TaskStepPrompt
from prompt.prompt_builder import PromptBuilder


def test_ベーシックな例():
    prompt = (
        PromptBuilder()
        .system("熟練したJavaアーキテクト")
        .context("既存のSpring Batchシステムをモダナイズしたい")
        .instruction("設計上の改善点を洗い出してください")
        .constraints([
            "Java 8以上を前提とする",
            "実務レベルの具体性を持たせる",
        ])
        .build()
    )

    print(prompt.render())


def test_条件付きコンポーネント追加():
    include_prohibited = True

    prompt = (
        PromptBuilder()
        .system("優秀なPython開発者")
        .instruction("コードレビューを行ってください")
        .when(
            include_prohibited,
            lambda builder: builder.prohibit([
                "グローバル変数の使用",
                "コメントのないコード",
            ])
        )
        .build()
    )

    rendered = prompt.render()
    print(rendered)
    if include_prohibited:
        assert "グローバル変数の使用" in rendered
        assert "コメントのないコード" in rendered
    else:
        assert "グローバル変数の使用" not in rendered
        assert "コメントのないコード" not in rendered


def test_階層構造コンポーネント():
    prompt = (
        PromptBuilder()
        .task("作業手順", lambda t: [
            t.add(
                TaskStepPrompt(
                    title="現状把握",
                    content="コード構成を整理する",
                )
            ),
            t.add(
                TaskStepPrompt(
                    title="コード構成を整理する",
                    content=(
                        """
Job / Step 一覧を抽出する
依存関係を図に起こす
"""
                    ),
                ).add(
                    TaskStepPrompt(
                        title="技術的負債を洗い出す",
                        content="""
古いライブラリや非推奨APIの使用箇所を特定する。
パフォーマンスボトルネックを特定する。
""",
                    )
                )
            ),
            t.add(
                TaskStepPrompt(
                    title="改善案検討",
                    content="将来的な保守性を見据えた改善案を検討する。",
                )
                .add(TaskStepPrompt(title="モジュール分割案を出す"))
                .add(TaskStepPrompt(title="移行ステップを整理する"))
            ),
        ])
        .build()
    )

    print(prompt.render())
