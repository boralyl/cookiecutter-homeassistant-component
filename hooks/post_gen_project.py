import os

# Rename root repo directory to use `-` instead of `_`.
repo_dir = "{{cookiecutter.domain}}"
new_repo_dir = repo_dir.replace("_", "-")
os.rename(os.path.join("..", repo_dir), os.path.join("..", new_repo_dir))
