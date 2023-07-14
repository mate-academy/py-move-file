import os


def move_file(command: str) -> None:
    parts = command.split()
    cmd, source_path, destination_path = parts
    separate_variable = os.getcwd()
    if len(destination_path.split("/")) >= 2:
        destination_folder, destination_file = os.path.split(destination_path)
        os.makedirs(destination_folder, exist_ok=True)
        source_file_in = os.path.join(separate_variable, source_path)
        destination_file_ex = (
            os.path.join(separate_variable,
                         f"{destination_folder}\\{destination_file}")
        )
        os.rename(source_file_in, destination_file_ex)
    else:
        os.rename(source_path, destination_path)
