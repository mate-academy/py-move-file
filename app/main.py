import os


def move_file(command: str) -> None:
    splited_command = command.split()
    if len(splited_command) == 3:
        command, file_source, file_destination = splited_command
        if command == "mv":
            if file_destination.endswith("/"):
                file_destination += file_source.split("/")[-1]
            destination_dirs = file_destination.split("/")
            if len(destination_dirs) > 1:
                temporary_directory = ""
                for folder_name in destination_dirs[:-1]:
                    temporary_directory = os.path.join(temporary_directory, folder_name)
                    if not os.path.exists(temporary_directory):
                        os.mkdir(temporary_directory)
            with open(file_source, "r") as input_file, \
                    open(file_destination, "w") as output_file:
                output_file.write(input_file.read())
            os.remove(file_source)
