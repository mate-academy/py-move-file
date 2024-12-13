import os
import re
from shutil import move


def move_file(command: str) -> None:
    if not re.match(r"^mv\s+\S+\s+\S+$", command):
        print("Invalid command format. "
              "Use 'mv <source_file> <destination_file>'")
        return

    command, file_in, file_out = command.split()
    folder_out_path = os.path.dirname(file_out)
    folder_in_path = os.path.dirname(file_in)
    if command == "mv":
        if folder_in_path == folder_out_path:
            os.rename(file_in, file_out)
        else:
            if not os.path.exists(folder_out_path):
                os.makedirs(folder_out_path)
            move(file_in, file_out)
