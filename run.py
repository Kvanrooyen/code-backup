import os
from backup import external_dir, project_choice
from git_command import run_git


def main():
    if os.path.isdir(external_dir):
        project_choice()
        run_git()
    else:
        print("External drive not found. Stopping backup.")


if __name__ == "__main__":
    main()
