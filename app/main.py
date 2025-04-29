import os


def move_file(command: str) -> None:
    command_list = command.split()
    path = command_list[2]
    if command_list[0] == "mv":
        if not path:
            print("Рядок порожній")
        else:
            dir_name = os.path.dirname(path)
            if dir_name:
                os.makedirs(os.path.dirname(path), exist_ok=True)
            try:
                with (
                    open(command_list[1], "r") as file_in,
                    open(path, "w") as file_out
                ):
                    need_to_write = file_in.read()
                    file_out.write(need_to_write)
            except FileNotFoundError(
                f"[Errno 2] No such file or directory: {command_list[1]}"
            ):
                pass

            os.remove(command_list[1])
