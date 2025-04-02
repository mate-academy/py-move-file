import os

def move_file(command: str) -> bool | None:
    my_split = command.split()
    if my_split[0] != "mv":
        return
    if len(my_split) != 3:
        return
    if my_split[2].endswith("/"):
        os.makedirs(my_split[2], exist_ok=True)
        my_split[2] + os.path.basename(my_split[1])
    if not my_split[2].endswith("/"):
        os.rename(my_split[1], my_split[2])
