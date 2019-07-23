import subprocess
import os

# User directory
user_dir = os.environ['USERPROFILE']
# Location of GitHub backup
git_dir = os.path.join(user_dir, "OneDrive",
                       "GitHub - Backup", "Project-Archive", "2019")


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
