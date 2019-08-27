import subprocess
import os
from backup import git_dir, user_dir


def run_git():
    # NOTE
    # After moving project zips to backup locations run the following:
    # git add .
    # git commit -m <commit message>
    # os.chdir(git_dir)
    subprocess.call(["git"] + ["add", "."], cwd=git_dir)
    print('Type your commit message: ')
    commit_msg = input('> ')
    subprocess.call(["git"] + ["commit", "-m"] + [commit_msg], cwd=git_dir)
