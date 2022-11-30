from os import makedirs, remove


def move_file(command: str) -> None:
    list_with_info = command.split(" ")
    file_in_name = list_with_info[1]
    dirs_name = ""

    if list_with_info[0] != "mv":
        return
    try:
        for string in list_with_info[2].split("/"):
            if "txt" in string:
                break
            dirs_name += string + "/"
        makedirs(dirs_name)
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
