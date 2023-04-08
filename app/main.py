import os


def move_file(command: str) -> None:
    comparison_list = command.split()
    if len(comparison_list) == 3:
        command_set = command.split()
        if command_set[0] != "mv":
            raise Exception(
                f"You are allowed to use only 'mv' command! "
                f"Meanwhile you have inputted {command_set[0]}!"
            )
    file_in_path = os.path.abspath(command_set[1])
    file_out_path = os.path.abspath(command_set[2])
    file_out_dir_path = os.path.split(file_out_path)[0]
    if not os.path.exists(file_out_dir_path):
        os.makedirs(file_out_dir_path, exist_ok=True)

    with (
        open(file_in_path, "r") as file_in,
        open(file_out_path, "w") as file_out
    ):
        file_out.write(file_in.read())

    os.remove(file_in_path)
