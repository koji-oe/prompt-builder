from prompt.prompt_builder import PromptBuilder


class RefactorJavaPreset:

    @staticmethod
    def get_preset() -> PromptBuilder:
        return (
            PromptBuilder()
            .system("熟練したJavaアーキテクト")
            .constraints([
                "Java8",
                "既存仕様を維持すること",
                "SOLID原則に従うこと",
                "デザインパターンを適用すること",
                "コードの可読性と保守性を向上させること",
            ])
            .instruction("以下のJavaコードをリファクタリングしてください。")
            .output_format("diff形式で出力")
        )
