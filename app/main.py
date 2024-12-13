# write your code here
import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        return
    pathway_file = os.path.split(parts[2])
    if os.path.exists(parts[1]):
        if len(pathway_file[0]) == 0:
            os.rename(parts[1], parts[2])
        else:
            if not os.path.isdir(pathway_file[0]):
                os.makedirs(pathway_file[0])
            with (open(parts[1], "r") as file_in,
                  open(parts[2], "w") as file_out):
                file_out.write(file_in.read())
                os.remove(parts[1])
