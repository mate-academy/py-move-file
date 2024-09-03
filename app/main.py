import os

from app.errors import (InvalidCommandError,
                        InvalidFileError,
                        InvalidFileCountError,
                        InvalidPathError)


def move_file(command: str) -> int:
    args_list = command.split()

    if len(args_list) != 3:
        raise InvalidFileCountError("Invalid file count")
    elif args_list[0] != "mv":
        raise InvalidCommandError("Invalid command")
    elif args_list[1] == args_list[2]:
        raise InvalidPathError("Invalid path for moving file")
    elif not args_list[1].split("/")[-1]:
        raise InvalidFileError("Invalid file name")
    else:
        path_dirs = os.path.dirname(args_list[2])
        file_name_in_source_path = os.path.basename(args_list[1])
        file_name_in_dest_path = os.path.basename(args_list[2])
        if file_name_in_dest_path:
            file_name = file_name_in_dest_path
        else:
            file_name = file_name_in_source_path
        try:
            if path_dirs:
                os.makedirs(path_dirs, exist_ok=True)
            with (open(os.path.join(args_list[1]), "r") as s_file,
                  open(os.path.join(path_dirs, file_name) , "a") as d_file):
                for line in s_file:
                    d_file.write(line)
        except FileNotFoundError:
            os.removedirs(os.path.join(path_dirs))
            raise
        else:
            os.remove(args_list[1])
            return 0
