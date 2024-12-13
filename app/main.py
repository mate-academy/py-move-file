import os


def move_file(command: str) -> None:
    command_call, file_to_copy, result_file, *redundant = command.split(" ")
    if redundant or command_call != "mv" or file_to_copy == result_file:
        return
    if "/" not in result_file:
        os.rename(file_to_copy, result_file)
        return
    directories = result_file.split("/")
    path = ""
    for folder in directories[:-1]:
        path = os.path.join(path, folder)
        try:
            os.mkdir(path)
        except FileExistsError:
            pass
    with open(file_to_copy, "r") as file_in, open(
        result_file, "w"
    ) as file_out:
        file_out.write(file_in.read())
    os.remove(file_to_copy)
