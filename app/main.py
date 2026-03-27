import os


def move_file(command: str) -> None:
    print(command)
    if not isinstance(command, str):
        raise TypeError("Command must be str type")
    split_commnd = command.split()
    if len(split_commnd) != 3 or split_commnd[0] != "mv":
        raise ValueError(
            "Command should be like this:"
            " mv file.txt file2.txt"
        )

    file_name = split_commnd[1]
    dest_path = split_commnd[2]

    if file_name != dest_path:
        dirname = os.path.dirname(dest_path)
        if dirname:
            os.makedirs(dirname, exist_ok=True)

        with (
            open(file_name, "r") as first_file,
            open(dest_path, "w") as second_file
        ):
            second_file.write(first_file.read())
            os.remove(file_name)
