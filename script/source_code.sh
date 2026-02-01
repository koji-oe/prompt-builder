#!/usr/bin/env bash
set -euo pipefail

# カレントディレクトリ基準で .py ファイルを再帰的に取得
find . -type f -name "*.py" | sort | while read -r file; do
  # 先頭の ./ を除いた相対パス
  rel_path="${file#./}"

  echo "\`$rel_path\`"
  echo '```python'
  cat "$file"
  echo '```'
  echo
done