import os


def move_file(command: str) -> None:
    if len(command.split()) != 3:
        return
    cp_command, current_file, future_file = command.split()
    if cp_command != "mv":
        return
    directories, file_name = os.path.split(future_file)

    if directories != "":
        os.makedirs(os.path.join(*directories.split("/")), exist_ok=True)

        with (
            open(current_file, "r") as source_file,
            open(f"{directories}/{file_name}", "w") as destination_file
        ):
            destination_file.write(source_file.read())
        os.remove(current_file)
    else:
        os.rename(current_file, file_name)
