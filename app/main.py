def move_file(command: str) -> None:

    if not command:
        return

    splitted = command.split()

    if splitted[0] != "mv":
        return

    if len(splitted) != 3:
        return
    
    source_file = splitted[1]

    full_destination = splitted[2].split("/")

    dirs = full_destination[:-1]

    new_file_name = full_destination[-1]

    if splitted[2].endswith("/"):
        new_file_name = source_file
