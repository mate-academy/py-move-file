from os import makedirs, remove


def move_file(command: str) -> None:
    list_with_info = command.split(" ")
    file_in_name = list_with_info[1]
    dirs = list_with_info[2].split("/")

    if list_with_info[0] != "mv":
        return
    try:
        makedirs(f"{dirs[0]}/{dirs[1]}/{dirs[2]}")
    except OSError:
        pass

    with (
        open(file_in_name, "r") as file_in,
        open(list_with_info[-1], "w") as file_out
    ):
        file_out.write(file_in.read())
        file_in.close()
        file_out.close()
        remove(file_in_name)
