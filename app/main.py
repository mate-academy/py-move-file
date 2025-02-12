import os


def move_file(command: str) -> None:
    command_list = command.split()
    catalog_list = command_list[2].split("/")

    source = ""
    for catalog in catalog_list:
        if "." not in catalog:
            source += catalog
            try:
                if not os.path.exists(source):
                    os.mkdir(source)
            except FileExistsError:
                pass
            source += "/"

    with (open(command_list[1], "r") as origin_file,
          open(command_list[2], "w") as new_file):
        new_file.write(origin_file.read())
        os.remove(command_list[1])
