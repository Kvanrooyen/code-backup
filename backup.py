import os
import shutil
import datetime
import time
import sys
import glob

# Current day and month
today = datetime.date.today().strftime("%d-%m")
# Working Drive directory
src_dir = r'C:\Users\kvanr\Desktop\Working Drive\\'
# Location of External backup
external_dir = r'D:\Code\2019\\'


def title():
    print(r"   _____ ____  _____  ______      ____          _____ _  ___    _ _____    ")
    print(r"  / ____/ __ \|  __ \|  ____|    |  _ \   /\   / ____| |/ / |  | |  __ \   ")
    print(r" | |   | |  | | |  | | |__       | |_) | /  \ | |    | ' /| |  | | |__) |  ")
    print(r" | |   | |  | | |  | |  __|      |  _ < / /\ \| |    |  < | |  | |  ___/   ")
    print(r" | |___| |__| | |__| | |____     | |_) / ____ \ |____| . \| |__| | |       ")
    print(r"  \_____\____/|_____/|______|    |____/_/    \_\_____|_|\_/\____/|_|       ")
    print('\n')


language_menu_items = {
    1: 'C++',
    2: 'C#',
    3: 'Java',
    4: 'Python',
    5: 'Web'
}


def language_menu():
    # Creating backup_language as global allows it to be used outside the function
    global backup_language
    while True:
        print('Choose the language of the project. Type only the number.\n')
        print('[1] C++\n[2] C#\n[3] Java\n[4] Pyhon\n[5] Web')
        try:
            lang_choice = int(input('language menu >> '))
            if 0 < lang_choice < 6:
                print(
                    f'\n{language_menu_items.get(lang_choice)} is the selected langauge. Proceeding to next step.')
                backup_language = language_menu_items.get(lang_choice)
            else:
                unknown_command()
                continue
        except ValueError:
            unknown_command()
            continue
        else:
            break


def project_menu():
    os.system('cls')
    title()  # Show the title permanently
    # Creating backup_project as a global allows it to be used outside the function
    global backup_project
    # A pair of lists for storing the projectNo and projectName
    list_project_num = []
    list_project_name = []

    # Count the number of folder in the directory
    count = len(os.listdir(src_dir))
    total_items = len(os.listdir(src_dir)) + 1

    for item in range(0, count):
        # Number the items in the lsit based of number of projects in src
        # NOTE Int value. Same as language_menu_items
        list_project_num.append(item + 1)

    for item in range(0, count):
        # Seperate each item and add it to corresponding number value from previous for loop
        elt = (os.listdir(src_dir))[item]
        # NOTE String value. Same as language_menu_items
        list_project_name.append(elt)

    # Convert the lists to a dictionary
    src_dir_items = dict(zip(list_project_num, list_project_name))

    while True:
        print('What project do you want to backup.\n')
        # NOTE https://www.techbeamers.com/python-program-convert-lists-dictionary/
        for item in range(0, count):
            print(f'[{list_project_num[item]}] {list_project_name[item]}')
        try:
            project_choice = int(input('project menu >> '))
            if 0 < project_choice < total_items:
                # User entered valid project
                # NOTE [project_choice - 1] the - 1 is used to give the correct list number.
                # When creating list_project_num the +1 gets rid of the 0, when displaying
                # it does not do so when selecting the number, hence the -1
                print(
                    f'\n{list_project_name[project_choice - 1]}, has been selected to be backed up. Proceeding to next step.')
                backup_project = src_dir_items.get(project_choice)
            else:
                unknown_command()
                continue
        except ValueError:
            unknown_command()
            continue
        else:
            break


def unknown_command():
    print('\nThat command is unknown.  Please try again.\n\n')


def git_backup():
    # NOTE Project is chosen first, then the project langauge, then the project is zipped
    # after being zipped it gets moved to the backup location
    project_menu()
    language_menu()
    zip_project(f'{backup_project}--{today}',
                os.path.join(src_dir + backup_project))
    print('Proceeding to move project to GitHub backup location.')


def external_backup():
    # NOTE Project is chosen first, then the project langauge, then the project is zipped
    # after being zipped it gets moved to the backup location
    project_menu()
    language_menu()
    zip_project(f'{backup_project}--{today}',
                os.path.join(src_dir + backup_project))
    print('Proceeding to move project to External Drive backup location.')


def move_project(backup_location):
    # NOTE Move zip folder to backup location
    # Make sure the current directory is the src_dir
    os.chdir(src_dir)
    # Searches the directory for zip files to move.
    try:
        for file in glob.glob(backup_project + '.zip'):
            shutil.move(src_dir + file, backup_location)
        print('\nSuccesfully moved the project to the backup location.')
    except OSError as e:
        print(f'Error has occured.\n{e}')


def zip_project(output_name, project_src_dir):
    shutil.make_archive(output_name, 'zip', project_src_dir)
    print('Finished zipping')


menu = {
    "0": sys.exit,
    "1": external_backup,
    "2": git_backup
}

while True:
    # Set the current working directory to the src_dir
    os.chdir(src_dir)
    print('\nChoose a backup option. Type only the number.')
    print('[0] Exit\n[1] External Drive\n[2] Git\n')
    choice = input('main menu >> ')
    # FIXME Throws error when exiting with sys.exit
    menu.get(choice, unknown_command)()
