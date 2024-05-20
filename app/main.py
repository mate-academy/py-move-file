import os


def move_file(command: str) -> str | None:
    command, source_file_name, new_path = command.split()
    if command != "mv":
        return "Incorrect command"
    new_file_name = new_path.split("/")[-1]
    new_path = os.path.join(os.getcwd(), new_path.replace(new_file_name, ""))
    os.makedirs(new_path, exist_ok=True)

    with (
        open(os.path.join(os.getcwd(), source_file_name), "r") as source_file,
        open(os.path.join(new_path, new_file_name), "w") as new_file
    ):
        new_file.write(source_file.read())
    os.remove(os.path.join(os.getcwd(), source_file_name))
