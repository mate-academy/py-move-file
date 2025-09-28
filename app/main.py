import os


def move_file(command: str) -> None:
    parts = (command_name, source_file_name,
             destination_file_name) = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        return
    cmd, source_file_name, destination_file_name = parts

    destination_file_name = os.path.normpath(destination_file_name)

    if os.path.sep not in destination_file_name:
        if os.path.altsep not in destination_file_name:
            os.rename(source_file_name, destination_file_name)
            return
    else:
        folder_path = os.path.dirname(destination_file_name)
        name_patch = os.path.basename(destination_file_name)
        os.makedirs(folder_path, exist_ok=True)
        path = os.path.join(folder_path, name_patch)

        try:
            with (open(source_file_name, "r") as file_in,
                  open(path, "w") as file_out):
                content = file_in.read()
                file_out.write(content)

            os.remove(source_file_name)
        except FileNotFoundError:
            raise FileNotFoundError
