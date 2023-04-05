import os


def move_file(command: str) -> None:
    if len(command.split()) == 3:
        command_name, source_file, directories_and_file = command.split()

        # prepare all child directories
        file_destination = directories_and_file.split("/")
        directories_number = 1
        while directories_number < len(file_destination):
            directory = "/".join(file_destination[:directories_number])
            if not os.path.exists(directory):
                os.mkdir(directory)
            directories_number += 1

        # move file
        if command_name == "mv" and source_file != directories_and_file:
            with (
                open(source_file, "r") as file_in,
                open(directories_and_file, "w") as file_out
            ):
                file_out.write(file_in.read())
            os.remove(source_file)
