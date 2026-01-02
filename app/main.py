from os import remove

from .file_utils import rename_file, copy_file, create_path


def move_file(command: str) -> None:

    cmd_parts = command.split()
    file_in_name = cmd_parts[1]
    file_out_name = cmd_parts[2]

    if (
            len(cmd_parts) != 3
            or cmd_parts[0] != "mv"
            or file_in_name == file_out_name
    ):
        return

    if "/" not in file_out_name:
        rename_file(file_in_name, file_out_name)
        return

    file_out_name_parts = file_out_name.split("/")

    if file_out_name[-1] != "/":
        file_out_name = file_out_name_parts[-1]
    else:
        file_out_name = f"new_{file_in_name}"

    file_out_name_parts = file_out_name_parts[:-1]
    create_path(file_out_name_parts)

    file_out_name_parts.append(file_out_name)
    file_out_name = "/".join(file_out_name_parts)

    copy_file(file_in_name, file_out_name)
    remove(file_in_name)
