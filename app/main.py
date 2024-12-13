import os


def move_file(command: str) -> None:

    user_command, source_file, full_path = command.split()
    if full_path.endswith("/"):
        full_path += source_file

    if user_command != "mv":
        return

    result_dir = os.path.dirname(full_path)
    if result_dir and not os.path.exists(result_dir):
        os.makedirs(result_dir)

    with (open(source_file, "r") as file_out,
          open(full_path, "w") as file_to):
        file_to.write(file_out.read())

    os.remove(source_file)
