import os


def move_file(command: str) -> None:
    ls_command = command.split(" ")
    if len(ls_command) != 3:
        raise RuntimeError("the command syntax is not valid")
    if ls_command[0] != "mv":
        raise NameError("not the expected command")

    file_name_in, file_name_out = ls_command[1:]
    ls_address = file_name_out.split("/")
    length_address = len(ls_address)
    ls_path = ls_address[:(length_address - 1)]

    last_catalog = ""
    for catalog in ls_path:
        path_join = os.path.join(last_catalog, catalog)
        if not os.path.exists(path_join):
            os.mkdir(path_join)
        last_catalog = path_join

    with (open(file_name_in, "r") as file_in,
          open(file_name_out, "w") as file_out):
        context = file_in.read()
        file_out.write(context)

    if os.path.exists(file_name_in):
        os.remove(file_name_in)
