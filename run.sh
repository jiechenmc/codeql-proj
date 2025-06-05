: "${1:?First argument is required; Supply Query Name}"

query_dir="./codeql-custom-queries-python"

if [[ ! -f "$query_dir/$1.ql" ]]; then
  echo "Error: File '$query_dir/$1.ql' not found." >&2
  exit 1
fi

codeql database create db --language python --source-root lambda --overwrite
codeql query run $query_dir/$1.ql --database ./db