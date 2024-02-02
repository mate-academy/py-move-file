# write your code here
import os


def move_file(command: str) -> None:
    address_file = command.split()
    pathway_file = os.path.split(address_file[2])
    if os.path.exists(address_file[1]):
        if address_file[2].count("/") == 0:
            os.rename(address_file[1], address_file[2])
        else:
            if not os.path.isdir(pathway_file[0]):
                os.makedirs(pathway_file[0])
            with (open(address_file[1], "r") as file_in,
                  open(f"{os.path.join(address_file[2])}", "w") as file_out):
                file_out.write(file_in.read())
                os.remove(address_file[1])
