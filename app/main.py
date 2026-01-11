import os
import shutil


def move_file(command: str) -> None:
    try:
        mv_command, file_in, file_out = command.split()
    except ValueError:
        print(
            "Argument must consist of: "
            "mv command, file name to move and destination"
        )
    else:
        if mv_command != "mv":
            return

        if not os.path.exists(file_in):
            raise FileNotFoundError("No such file you try to move")
        file_in_name = file_in

        if "/" not in file_out:
            file_out_name = file_out
            os.rename(file_in_name, file_out_name)
        else:
            directory_path, file_out_name = os.path.split(file_out)
            if not os.path.exists(directory_path):
                os.makedirs(directory_path)
            shutil.move(
                file_in_name,
                os.path.join(directory_path, file_out_name)
            )
