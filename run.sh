query_dir="./codeql-custom-queries-python"



codeql database create db --language python --source-root lambda --overwrite
codeql query run codeql-custom-queries-python/$1.ql --database ./db