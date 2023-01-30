import os


def move_file(command: str) -> None:
    input_command, original_file_path, destination_file_path = command.split()
    if input_command == "mv":
        dir_path, file_name = os.path.split(destination_file_path)
        if os.path.isdir(dir_path):
            os.makedirs(dir_path)
            new_file = os.path.join(dir_path, file_name)
            with (
                open(original_file_path, "r") as file_in,
                open(new_file, "w") as file_out
            ):
                file_out.write(file_in.read())
            os.remove(original_file_path)
        else:
            os.rename(original_file_path, destination_file_path)
