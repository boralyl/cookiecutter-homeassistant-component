import os
import platform


# Skipping this operation on windows since this is more cosmetic and
# causes a PermissionError on that platform.
if platform.system() != "Windows":
    # Rename root repo directory to use `-` instead of `_`.
    repo_dir = "{{cookiecutter.domain}}"
    new_repo_dir = repo_dir.replace("_", "-")
    os.rename(os.path.join("..", repo_dir), os.path.join("..", new_repo_dir))
