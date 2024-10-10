import os


def move_file(command: str) -> None:
    split_command = command.split()
    mv, source_file, destination_file = split_command
    path = destination_file[0:destination_file.rfind("/")]
    if mv == "mv":
        if "/" in command:
            if not os.path.exists(os.path.join(path)):
                os.makedirs(os.path.join(path))
            with (open(source_file, "r") as file_in,
                  open(destination_file, "w") as file_out):
                file_out.write(file_in.read())
            os.remove(source_file)
        else:
            os.rename(source_file, destination_file)
