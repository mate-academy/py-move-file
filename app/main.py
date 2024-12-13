from os import remove, makedirs


def move_file(command: str) -> None:
    command_name, file_in_name, file_out_name = command.split()
    file_out_path = file_out_name.split("/")
    if command_name != "mv":
        return print("Wrong command!")
    if len(file_out_path) > 1:
        path = "/".join(file_out_path[:-1])
        makedirs(path, exist_ok=True)
    with (open(file_in_name, "r") as file_in,
          open(file_out_name, "w") as file_out):
        content = file_in.read()
        file_out.write(content)
    remove(file_in_name)
