import os


def move_file(command: str) -> None:
    path_file = ""
    command_keyword, file, new_file = command.split(" ")
    if command_keyword == "mv":
        if "/" in new_file:
            route = new_file.split("/")
            for item in range(len(route) - 1):
                path_file += route[item]
                try:
                    os.mkdir(path_file)
                except FileExistsError:
                    pass
                path_file += "/"

            with open(file, "r") as file_in, open(new_file, "w") as file_out:
                file_out.write(file_in.read())
            os.remove(file)
        else:
            os.rename(file, new_file)
