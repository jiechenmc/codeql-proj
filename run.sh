set -euo pipefail

# Assuming there's only 1 function called hello

query_dir="./codeql-custom-queries-python"
# handler_config=$(yq '.functions.hello.handler' lambda/serverless.yml)
# handler="${handler_config%%.*}"
# function="${handler_config#*.}"
# echo $handler $function

: "${1:?First argument is required; Supply Query Name}"

if [[ ! -f "$query_dir/$1.ql" ]]; then
  echo "Error: File '$query_dir/$1.ql' not found." >&2
  exit 1
fi


codeql database create db --language python --source-root lambda --overwrite -j "$(nproc)"
codeql query run "$query_dir/$1.ql" --database ./db -j "$(nproc)"
