import os
import shutil
import datetime
import glob
from pathlib import Path


# Current day and month
today = datetime.date.today().strftime("%d-%m")
# User directory
user_dir = os.environ['USERPROFILE']
# Working Drive directory
src_dir = Path(user_dir + "/Desktop/Working Drive/")
# Location of GitHub backup
git_dir = Path(user_dir + "/OneDrive/GitHub - Backup/Project-Archive/2019/")
# Location of External backup
external_dir = r'D:\Code\2019'


language_menu_items = {
    1: 'C++',
    2: 'C#',
    3: 'Java',
    4: 'Python',
    5: 'Web',
    6: 'Flutter',
    7: 'Web'
}

lang_extensions = ['cpp', 'cs', 'java', 'py', 'html', 'iml', 'css']


# Checking for projects where the main project folder is not in a subdirectory
def get_project_lang(ext):
    return list(Path(src_dir, project_choice).glob(f'**/*.{ext}'))


def language_choice(project):
    while True:
        try:
            lang_choice = 0
            for index, lang in enumerate(lang_extensions):
                if len(get_project_lang(lang)) > 0:
                    lang_choice = index + 1
                    break

            if 0 < lang_choice < 8:
                # Give backup_language the value of whatever langauge was found
                backup_language = language_menu_items.get(lang_choice)
                # TODO - Show progress of backup in a progress bar.
                # Issue #5 on GitHub
                # Copies project to external drive
                copy_project(Path(external_dir, backup_language))
                # Moves project to git directory - OneDrive
                move_project(Path(git_dir, backup_language))
                # Break out of while loop to continue with project_choice()
                break
            else:
                general_error()
                print("Error is related to choosing a language for the project.")
        except ValueError as e:
            specific_error(e)


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

    while True:
        try:
            i = 0
            while i < total_items:
                project_choice = list_project_name[i]
                print(project_choice)
                os.chdir(src_dir)
                zip_project(f'{project_choice}--{today}',
                            os.path.join(src_dir, project_choice))
                language_choice(project_choice)
                i += 1
            break
        except ValueError as e:
            specific_error(e)


def general_error():
    # General error message, used when not handling specific error.
    print("An error has occured!")


def specific_error(err_msg):
    # err_msg is used to display the full error message
    print("An error has occured! Error details:\n %s" % err_msg)


def copy_project(backup_location):
    # Copy zip folder to backup location
    # Make sure the current directory is the src_dir
    os.chdir(src_dir)
    # Searches the directory for zip files to move.
    try:
        for project_zip_file in glob.glob(f'{project_choice}--{today}.zip'):
            # Check if the file exists in the directory before copying
            if os.path.isfile(os.path.join(backup_location, project_zip_file)):
                os.remove(os.path.join(backup_location, project_zip_file))

            # Copy zip file to external HDD -- backup_location
            shutil.copy(os.path.join(
                src_dir, project_zip_file), backup_location)
            print('Successfully copied the project to the backup location.')
    except OSError as e:
        specific_error(e)


def move_project(backup_location):
    # Make sure the current directory is the src_dir
    os.chdir(src_dir)
    # Searches the directory for zip files to move.
    try:
        for project_zip_file in glob.glob(f'{project_choice}--{today}.zip'):
            # Check if the file exists in the directory before copying
            if os.path.isfile(os.path.join(backup_location, project_zip_file)):
                os.remove(os.path.join(backup_location, project_zip_file))

            # Move zip file to backup location
            shutil.move(os.path.join(
                src_dir, project_zip_file), backup_location)
            print('Successfully moved the project to the backup location.')
    except OSError as e:
        specific_error(e)


def zip_project(output_name, project_src_dir):
    shutil.make_archive(output_name, 'zip', project_src_dir)
    print('Finished zipping')
