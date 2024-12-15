import os


def move_file(command: str) -> None:
    command_list = command.split(" ")
    index_new_directories = command_list[2].rfind("/")
    new_directories = command_list[2][:index_new_directories]
    if command_list[0] == "mv":
        os.makedirs(new_directories, exist_ok=True)

        with (
            open(command_list[1], "r") as file_riad,
            open(command_list[2], "w") as file_write,
        ):
            reader = file_riad.read()
            file_write.write(reader)

        os.remove(command_list[1])
