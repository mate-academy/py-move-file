import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        return
    old_file = parts[1]
    new_file = parts[2]
    if parts[0] == "mv":
        try:
            with open(old_file, "r") as file_in:
                content = file_in.read()
                if new_file[-1] == "/":
                    result_file = os.path.join(new_file,
                                               os.path.basename(old_file))
                    result_dir = os.path.dirname(result_file)
                else:
                    result_file = new_file
                    result_dir = os.path.dirname(new_file)

                if result_dir:
                    os.makedirs(result_dir, exist_ok=True)
                with open(result_file, "w") as file_out:
                    file_out.write(content)
            os.remove(old_file)
        except FileNotFoundError:
            return
