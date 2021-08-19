import os
import shutil
import time


def main():
    path = "/PATH_TO_DELETE"
    days = 30
    seconds = time.time() - (days * 24 * 60 * 60)

    if os.path.exists(path):
        for root_folder, folders, files in os.walk(path):
            if seconds >= getAge(root_folder):
                remove_folder(root_folder)
                break
            else:
                for folder in folders:
                    folder_path = os.path.join(root_folder, folder)
                    if seconds >= getAge(folder_path):
                        remove_folder(folder_path)

                for file in files:
                    file_path = os.path.join(root_folder, file)

                    if seconds >= getAge(file_path):
                        remove_file(file_path)

        else:
            if seconds >= getAge(path):
                remove_file(path)

    else:
        print(f'"{path}" is not found')


def remove_folder(path):
    if not shutil.rmtree(path):
        print(f"{path} is removed successfully")

    else:
        print(f"Unable To delete the " + path)


def remove_file(path):
    if not os.remove(path):
        print(f"{path} is rmeoved successfully")

    else:
        print("Unable to the delete the" + path)


def getAge(path):
    ctime = os.stat(path).st_time

    return ctime


if __name__ == "_main_":
    main()
