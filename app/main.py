import os


def move_file(name: str) -> None:
    command = name.split()
    if command[0] != "mv" or len(command) != 3:
        return

    source_file = command[1]
    target_file = command[2]
    target_path = os.path.dirname(target_file)

    if target_path != "" and not os.path.exists(target_path):
        os.makedirs(target_path, exist_ok=True)

        with (open(source_file, "r") as file_in,
              open(target_file, "w") as file_out):
            file_out.write(file_in.read())
        os.remove(source_file)

    else:
        if source_file != target_file:
            os.rename(source_file, target_file)
