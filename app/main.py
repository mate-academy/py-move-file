import os


def move_file(command: str) -> None:
    if "mv" in command:
        comm_list = command.split()
        if len(comm_list) == 3:
            file_to_copy = comm_list[1]
            path_to = comm_list[2]
            if path_to.endswith(".txt"):
                if "/" in path_to:
                    os.makedirs(os.path.dirname(path_to), exist_ok=True)
                try:
                    with (open(file_to_copy) as file_from,
                          open(path_to, "w") as file_to):
                        file_to.write(file_from.read())
                except FileNotFoundError:
                    print(f"File {file_to_copy} not found")
                    return
                os.remove(file_to_copy)
                return
            os.makedirs(path_to, exist_ok=True)
            try:
                with (open(file_to_copy)
                      as file_from,
                      open(os.path.join(path_to, file_to_copy), "w")
                      as file_to):
                    file_to.write(file_from.read())
            except FileNotFoundError:
                print(f"File {file_to_copy} not found")
                return
            os.remove(file_to_copy)
