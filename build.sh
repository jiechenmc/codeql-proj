codeql database create db --language python --source-root lambda --overwrite
codeql query run codeql-custom-queries-python/example.ql --database ./db