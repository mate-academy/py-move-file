import os
import shutil

def move_file(command: str) -> bool:
    if len(command.split()) != 3:
        raise ValueError
    cmd, source_file, new_file = command.split()
    os.makedirs(os.path.dirname(os.path.abspath(new_file)),
                exist_ok=True)
    with open(source_file, "r") as file_in, open(new_file, "w") as file_out:
        file_out.write(file_in.read())
    os.remove(source_file)