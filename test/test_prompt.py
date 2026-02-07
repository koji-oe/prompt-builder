from prompt.component.task_prompt import TaskPrompt
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
        .task("作業手順", lambda t: (
            t.add(TaskStepPrompt("現状把握")
                  .add(TaskStepPrompt("コード構成を整理する"))
                  .add(TaskStepPrompt("技術的負債を洗い出す"))
                  ),
            t.add(TaskStepPrompt("改善案検討")
                  .add(TaskStepPrompt("モジュール分割案を出す"))
                  .add(TaskStepPrompt("移行ステップを整理する"))
                  ),
        ))
        .build()
    )

    print(prompt.render())
