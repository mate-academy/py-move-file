import os


def move_file(command: str) -> None:
    mv, source_file, destination_file = command.split()
    path = destination_file[0:destination_file.rfind("/")]
    if mv == "mv" and "/" in command:
        if not os.path.exists(path):
            os.makedirs(path)
        with (open(source_file, "r") as file_in,
              open(destination_file, "w") as file_out):
            file_out.write(file_in.read())
        os.remove(source_file)
    else:
        os.rename(source_file, destination_file)
