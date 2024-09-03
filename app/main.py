import os

from app.errors import (InvalidCommandError,
                        InvalidFileError,
                        InvalidFileCountError,
                        InvalidPathError)


def move_file(command: str) -> int:
    args_list = command.split()
    dirs_list = []

    if len(args_list) != 3:
        raise InvalidFileCountError("Invalid file count")
    elif args_list[0] != "mv":
        raise InvalidCommandError("Invalid command")
    elif args_list[1] == args_list[2]:
        raise InvalidPathError("Invalid path for moving file")
    elif not args_list[1].split("/")[-1]:
        raise InvalidFileError("Invalid file name")
    else:
        dirs_list.extend(args_list[2].split("/"))
        if dirs_list[-1]:
            new_file_name = dirs_list[-1]
            del dirs_list[-1]
        else:
            new_file_name = args_list[1].split("/")[-1]

        try:
            if dirs_list:
                os.makedirs(os.path.join(*dirs_list), exist_ok=True)
                dirs_list.append(new_file_name)
            else:
                dirs_list.append(new_file_name)
            with (open(os.path.join(args_list[1]), "r") as read_file,
                  open(os.path.join(*dirs_list) , "a") as write_file):
                for line in read_file:
                    write_file.write(line)
        except FileNotFoundError:
            os.removedirs(os.path.join(*dirs_list))
            raise
        else:
            os.remove(args_list[1])
            return 0
