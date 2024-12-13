import os


def move_file(command: str) -> None:
    ls_command = command.split()
    if len(ls_command) != 3:
        raise RuntimeError("the command syntax is not valid")
    if ls_command[0] != "mv":
        raise NameError("not the expected command")

    file_name_in, file_name_out = ls_command[1:]
    path_, _ = os.path.split(file_name_out)

    if path_ != "" and not os.path.exists(path_):
        os.makedirs(path_)

    with (open(file_name_in, "r") as file_in,
          open(file_name_out, "w") as file_out):
        context = file_in.read()
        file_out.write(context)

    if os.path.exists(file_name_in):
        os.remove(file_name_in)
