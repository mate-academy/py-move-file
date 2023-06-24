import os


def move_file(command: str) -> None:
    split_command = command.split()

    if len(split_command) == 3 and split_command[0] == "mv":
        file_to_move = split_command[1]
        new_file_path = split_command[2]
        dirs = new_file_path.split("/")
        new_file_name = dirs[-1]

        if len(dirs) > 1:
            new_path = ""
            for directory in dirs[:-1]:
                new_path += directory

                if not os.path.exists(new_path):
                    os.mkdir(new_path)
                new_path += "/"

            new_path += new_file_name

            with (
                open(file_to_move, "r") as origin_file,
                open(new_path, "w") as new_file
            ):
                origin_content = origin_file.read()
                new_file.write(origin_content)

            os.remove(file_to_move)

        else:
            os.rename(file_to_move, new_file_name)
