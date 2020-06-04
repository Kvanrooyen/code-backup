import os
from backup import external_dir, project_choice
from git_command import run_git

filename = "wd-path"


def main():
    # Check whether or not the External Drive is connected/available
    if os.path.isdir(external_dir):
        project_choice()
        run_git()
    else:
        print("External drive not found. Stopping backup.")


if __name__ == "__main__":
    main()
