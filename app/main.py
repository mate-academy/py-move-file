import os


def move_file(command: str) -> None:
    sepp_command = command.split()

    source = sepp_command[1]
    destination = sepp_command[2]

    path_to_move = destination.split("/")

    new_dir = ""

    if path_to_move:
        for path in path_to_move[:-1]:
            new_dir += path + "/"
            if not os.path.exists(new_dir):
                os.mkdir(new_dir)

    with (open(source, "r") as file_out,
          open(destination, "w") as file_in):
        file_in.write(file_out.read())

    os.remove(source)
