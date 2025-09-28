import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        return
    cmd, source_file_name, destination_file_name = parts

    if (destination_file_name.endswith(os.path.sep) or
            (os.path.altsep and destination_file_name.endswith(os.path.altsep))):
        destination_file_name = os.path.join(destination_file_name,
                                             os.path.basename(source_file_name))

    destination_file_name = os.path.normpath(destination_file_name)

    if os.path.dirname(destination_file_name) == "":
        os.rename(source_file_name, destination_file_name)
        return

    else:
        folder_path = os.path.dirname(destination_file_name)
        folder_path_list = folder_path.split(os.path.sep)
        name_patch = os.path.basename(destination_file_name)
        folder_result = ""
        for folder in folder_path_list:
            folder_result = os.path.join(folder_result, folder)
            if not os.path.exists(folder_result):
                os.mkdir(folder_result)

        path = os.path.join(folder_result, name_patch)

        try:
            with (open(source_file_name, "rb") as file_in,
                  open(path, "wb") as file_out):
                content = file_in.read()
                file_out.write(content)

            os.remove(source_file_name)
        except FileNotFoundError:
            return
