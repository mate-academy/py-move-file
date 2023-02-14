# write your code here
import os


def move_file(command: str) -> None:
    input_command, source_file_path, destination_file_path = command.split()

    if input_command != "mv":
        raise NameError("You`ve entered wrong command")

    if input_command == "mv" and len(command.split()) == 3:
        if "/" in destination_file_path:
            os.makedirs(os.path.dirname(destination_file_path))
            with open(f"{source_file_path}", "r") as file_in, \
                    open(f"{destination_file_path}", "w") as file_out:
                file_out.write(file_in.read())
            os.remove(source_file_path)
        else:
            os.rename(source_file_path, destination_file_path)
