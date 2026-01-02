from os import mkdir, remove


def copy_file(file_in_name: str, file_out_name: str) -> None:
    if file_in_name == file_out_name:
        return

    with open(file_in_name) as file_in, open(file_out_name, "w") as file_out:
        file_out.write(file_in.read())


def rename_file(file_in_name: str, file_out_name: str) -> None:
    file_out_name_parts = file_out_name.split("/")
    if (
            len(file_out_name_parts) != 1
            or file_in_name == file_out_name
    ):
        return

    copy_file(file_in_name, file_out_name)
    remove(file_in_name)


def create_path(path: list[str]) -> None:
    if not path:
        return

    existing_path = "./"

    for directory in path:
        try:
            mkdir(existing_path + directory)
        except FileExistsError:
            pass
        existing_path += directory + "/"
