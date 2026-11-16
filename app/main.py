import os


def move_file(command: str) -> None:
    """ розділяємо команду на частини """
    full_path = ""
    split_command = command.split(" ")
    """ Якщо не вся команда, нічого не робимо """
    if len(split_command) == 3 and split_command[0] == "mv":
        split_dir = split_command[2].split("/")
        """ Якщо не вся команда, нічого не робимо """
        if len(split_dir) != 1:
            full_path = split_dir[0]
            if not os.path.exists(full_path):
                os.mkdir(full_path)
            for dir_file in range(1, (len(split_dir) - 1)):
                full_path = os.path.join(full_path, split_dir[dir_file])
                # full_path = full_path + "/" + split_dir[dir_file]
                # print(full_path)
                if not os.path.exists(full_path):
                    os.mkdir(full_path)
        with (open(split_command[1], "r") as file,
              open(os.path.join(full_path, split_dir[-1]), "w") as file2):
            file2.write(file.read())
        os.remove(split_command[1])
