def move_file(command: str) -> None:
    file_names = command.split()
    if len(file_names) != 3 or file_names[0] != "mv":
        return
    if file_names[2].endswith("/"):
        return
    try:
        with (open(file_names[1], "r")
              as file_in, open(file_names[2], "w") as file_out):
            file_out.write(file_in.read())
    except OSError:
        return