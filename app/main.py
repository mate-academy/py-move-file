import shutil
import os


def move_file(command: str) -> None:
    trace = command.split()
    file_name = "/".join(trace[2].split("/")[-1:])
    directory = trace[2].replace(file_name, "")
    if not os.path.exists(directory):
        os.makedirs(directory)
    shutil.copy2(trace[1], trace[2])
    os.remove(trace[1])
