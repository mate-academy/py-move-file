import os


def move_file(command: str) -> str:
    if len(command.split()) != 3:
        return "Input correct path"
    cmd, input_file_path, destination_file_path = command.split()
    if cmd != "mv":
        return "Input correct command"
    if not os.path.exists(input_file_path):
        return f"No such file: {input_file_path}"

    new_dirs, new_file_name = os.path.split(destination_file_path)

    if new_dirs:
        os.makedirs(new_dirs, exist_ok=True)
        if os.path.exists(os.path.join(new_dirs, new_file_name)):
            return f"File with name {new_file_name} already exist"
        with open(input_file_path, "r") as source,\
                open(os.path.join(new_dirs, new_file_name), "w")\
                as destination_file:
            destination_file.write(source.read())
            os.remove(input_file_path)
    elif os.path.splitext(destination_file_path):
        os.rename(input_file_path, new_file_name)
