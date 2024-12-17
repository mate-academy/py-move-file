import os


class CommandError(Exception):
    pass


def move_file(command: str) -> None | str:
    command_list = command.split(" ")
    if "/" in command_list[2]:
        index_new_directories = command_list[2].rfind("/")
        new_directories = command_list[2][:index_new_directories]
        os.makedirs(new_directories, exist_ok=True)

    if command_list[0] == "mv":
        try:
            with (
                open(command_list[1], "r") as file_read,
                open(command_list[2], "w") as file_write,
            ):
                reader = file_read.read()
                file_write.write(reader)

            os.remove(command_list[1])
        except FileNotFoundError:
            return f"No such file: {command_list[1]}"
    else:
        raise CommandError
