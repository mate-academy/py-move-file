import os


def move_file(command: str) -> None:
    name = command.split(" ")

    if len(name) == 3 and name[0] == "mv" and not name[1] == name[2]:
        if "/" not in name[2]:
            os.rename(name[1], name[2])
        else:
            dir_way = name[2].split("/")
            file_name = dir_way[-1]
            directories = dir_way[:-1]

            os.makedirs("/".join(directories), exist_ok=True)

            way_to_file = f"{'/'.join(directories)}/{file_name}"

            os.replace(name[1], way_to_file)
