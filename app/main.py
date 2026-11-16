import os


def move_file(command: str) -> None:
    """ розділяємо команду на частини """
    split_command = command.split(" ")
    """ Якщо не вся команда, нічого не робимо """
    if len(split_command) == 3:
        split_dir = split_command[2].split("/")
        """ Якщо не вся команда, нічого не робимо """
        if len(split_dir) != 1:
            full_path = split_dir[0]
            # print(full_path)
            if not os.path.exists(full_path):
                os.mkdir(full_path)
            for dir_file in range(1, (len(split_dir) - 1)):
                full_path = full_path + "/" + split_dir[dir_file]
                # print(full_path)
                if not os.path.exists(full_path):
                    os.mkdir(full_path)
        with (open(split_command[1], "r") as file,
              open(split_command[2], "w") as file2):
            file2.write(file.read())
        os.remove(split_command[1])
