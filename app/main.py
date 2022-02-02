import os
import shutil


def move_file(command):
    main_command, old_file, new_file = command.split()
    if not os.path.exists(old_file):
        with open(old_file, "w") as f:
            f.write("Hello")
    if main_command != "mv" or old_file == new_file:
        exit()
    if len(new_file.split("/")) == 1:
        os.rename(old_file, new_file)
    else:
        new_path = "/".join(new_file.split("/")[:-1])
        if not os.path.exists(new_path):
            os.makedirs(new_path)
        shutil.move(old_file, new_file)


if __name__ == "__main__":
    move_file(input("Enter command: "))
