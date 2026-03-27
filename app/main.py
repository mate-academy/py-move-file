import os


def move_file(command: str) -> None:
    if command.split()[0] == "mv":
        files_list = command.split()[1:]
        dirs = []
        second_file = files_list[1]

        if "/" in files_list[1]:
            dirs = files_list[1].split("/")[:-1]
            second_file = files_list[1].split("/")[-1]

        with open(files_list[0], "r") as first_file:
            content = first_file.read()

        if len(dirs) == 0:
            with open(second_file, "w") as file:
                file.write(content)
        else:
            os.makedirs("/".join(dirs), exist_ok=True)

            with open("/".join(dirs) + "/" + second_file, "w") as file:
                file.write(content)

        os.remove(files_list[0])
