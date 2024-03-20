import os


def move_file(command: str) -> None:

    command_list = command.split()

    if len(command_list) != 3:
        raise ValueError(f"Expected 3 arguements, {len(command_list)} "
                         f"were given!")
    if command_list[0] != "mv":
        raise ValueError(f"Expected 'mv' as the first argument, "
                         f"{command_list[0]} was given!")

    source = command_list[1]
    destination = command_list[2]
    dirname = os.path.dirname(destination)

    if dirname and not os.path.exists(dirname):
        os.makedirs(dirname)

    with (open(source, "r") as orig_f,
            open(destination, "w") as copy_f):
        copy_f.write(orig_f.read())
    os.remove(source)
