import os


def move_file(command: str) -> None:
    command_split_arr = command.split()

    if len(command_split_arr) != 3:
        raise ValueError(
            f"Expected 3 arguments, got: {len(command_split_arr)}"
        )
    if command_split_arr[0] != "mv":
        raise ValueError(f"There is not '{command_split_arr[0]}' command!")

    os.makedirs(command_split_arr[2][:-1], exist_ok=True)

    with (
        open(command_split_arr[1], "r") as file_with_content,
        open(command_split_arr[2], "w") as new_file
    ):
        new_file.write(file_with_content.read())
        os.remove(command_split_arr[1])
