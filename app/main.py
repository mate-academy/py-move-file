import os


def move_file(command: str) -> None:
    list_files = command.split()
    if (len(list_files) == 3
            and list_files[0] == "mv"
            and list_files[1] != list_files[2]):
        head_tail = os.path.split(list_files[2])
        if head_tail[0] != "":
            os.makedirs(head_tail[0], exist_ok=True)
        with (open(list_files[1], "r") as file_in,
              open(list_files[2], "w") as file_out):
            file_out.write(file_in.read())
        os.remove(list_files[1])
