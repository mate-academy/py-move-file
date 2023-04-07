import os


def move_file(command: str) -> None:
    if len(command.split()) == 3:
        command_name, source_file, directories_and_file = command.split()

        # prepare all child directories
        directories = directories_and_file[:directories_and_file.rfind("/")]
        os.makedirs(directories, exist_ok=True)

        # move file
        if command_name == "mv" and source_file != directories_and_file:
            with (
                open(source_file, "r") as file_in,
                open(directories_and_file, "w") as file_out
            ):
                file_out.write(file_in.read())
            os.remove(source_file)
