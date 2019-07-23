import os
import shutil
import datetime
import glob
import subprocess
from pathlib import Path


# Current day and month
today = datetime.date.today().strftime("%d-%m")
# User directory
user_dir = os.environ['USERPROFILE']
# Working Drive directory
src_dir = os.path.join(user_dir, "Desktop", "Working Drive")
# Location of GitHub backup
git_dir = os.path.join(user_dir, "OneDrive",
                       "GitHub - Backup", "Project-Archive", "2019")
# Location of External backup
external_dir = r'D:\Code\2019'


language_menu_items = {
    1: 'C++',
    2: 'C#',
    3: 'Java',
    4: 'Python',
    5: 'Web',
    6: 'Flutter'
}

lang_extensions = ['cpp', 'cs', 'java', 'py', 'html', 'iml']


# Checking for projects where the main project folder is not in a subdirectory
def get_project_lang(ext):
    return list(Path(src_dir, project_choice).glob(f'*.{ext}'))


# Checking for projects where the main project folder is in a subdirectory
def get_project_lang_alt(ext):
    return list(Path(src_dir, project_choice).glob(f'{project_choice}/*.{ext}'))


def language_choice(project):
    while True:
        try:
            lang_choice = 0
            for index, lang in enumerate(lang_extensions):
                if len(get_project_lang(lang)) > 0:
                    lang_choice = index + 1
                    break
                elif len(get_project_lang_alt(lang)) > 0:
                    lang_choice = index + 1
                    break

            if 0 < lang_choice < 7:
                # Give backup_language the value of whatever langauge was found
                backup_language = language_menu_items.get(lang_choice)
                # Copies project to external drive
                copy_project(os.path.join(external_dir, backup_language))
                # Moves project to git directory - OneDrive
                move_project(os.path.join(git_dir, backup_language))
            else:
                unknown_command()
                continue
        except ValueError:
            unknown_command()
            continue
        else:
            break


def project_choice():
    global project_choice
    # A pair of lists for storing the projectNo and projectName
    list_project_num = []
    list_project_name = []

    # Count the number of folder in the directory
    count = len(os.listdir(src_dir))
    total_items = len(os.listdir(src_dir))

    for item in range(0, count):
        # Number the items in the list based of number of projects in src
        list_project_num.append(item + 1)

    for item in range(0, count):
        # Separate each item and add it to corresponding number value
        # from previous for loop
        elt = (os.listdir(src_dir))[item]
        list_project_name.append(elt)

    # Convert the lists to a dictionary
    src_dir_items = dict(zip(list_project_num, list_project_name))
    while True:
        try:
            i = 0
            while i < total_items:
                project_choice = list_project_name[i]
                backup_project = src_dir_items.get(project_choice)
                print(project_choice)
                os.chdir(src_dir)
                zip_project(f'{project_choice}--{today}',
                            os.path.join(src_dir, project_choice))
                language_choice(project_choice)
                i += 1
            break
        except ValueError:
            unknown_command()
            continue


def unknown_command():
    print('\nThat command is unknown.  Please try again.\n\n')


def copy_project(backup_location):
    # Copy zip folder to backup location
    # Make sure the current directory is the src_dir
    os.chdir(src_dir)
    # Searches the directory for zip files to move.
    try:
        for file in glob.glob(f'{project_choice}--{today}.zip'):
            shutil.copy(os.path.join(src_dir, file), backup_location)
        print('Successfully copied the project to the backup location.')
    except OSError as e:
        print(f'Error has occurred.\n{e}')


def move_project(backup_location):
    # Make sure the current directory is the src_dir
    os.chdir(src_dir)
    # Searches the directory for zip files to move.
    try:
        for file in glob.glob(f'{project_choice}--{today}.zip'):
            # Move zip folder to backup location
            shutil.move(os.path.join(src_dir, file), backup_location)
        print('Successfully moved the project to the backup location.')
    except OSError as e:
        print('Error has occurred.\n %s' % e)


def zip_project(output_name, project_src_dir):
    shutil.make_archive(output_name, 'zip', project_src_dir)
    print('Finished zipping')


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


project_choice()
# run_git()
