import os


def move_file(command: str) -> None:
    action, file_origin, option = command.split()

    if "/" not in option:
        os.rename(file_origin, option)
        return

    elif "/" in option:
        current_path = ""
        if option[-1] == "/":
            option += file_origin
        for step in option.split("/")[:-1]:
            current_path += step + "/"
            try:
                os.mkdir(current_path)
            except FileExistsError:
                continue
        with open(file_origin, "r") as source_file_object:
            origin_content = source_file_object.readlines()
        with open(option, "w") as new_file_object:
            new_file_object.writelines(origin_content)
        os.remove(file_origin)
