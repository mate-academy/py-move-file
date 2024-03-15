import os


def move_file(command: str) -> None:
    parts = command.split(" ")
    try:
        if len(parts) == 3:
            com, first_file, second_file = parts
            if com == "mv":
                parts_dir = second_file
                if "/" in parts_dir:
                    parts_dir = second_file.split("/")
                for directory in range(1, len(parts_dir)):
                    path_to_file = "/".join(parts_dir[:directory])
                    if not os.path.exists(path_to_file):
                        os.mkdir(path_to_file)
                with (
                    open(first_file, "r") as file_in,
                    open(second_file, "w") as file_out
                ):
                    file_out.write(file_in.read())
                os.remove(first_file)
    except FileNotFoundError:
        pass
