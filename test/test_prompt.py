from prompt.prompt_builder import PromptBuilder


def test_one():
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
