import os


def move_file(command: str) -> None:
    if len(command.split()) == 3:
        command_id, file_name, file_path = command.split()
        if command_id != "mv":
            raise ValueError("Command should be 'mv'")

        if "/" not in command:
            os.rename(file_name, file_path)
        else:
            os.makedirs(file_path, exist_ok=True)
            os.replace(file_name, file_path)

            with (open(f"{file_name}", "r") as file_in,
                  open(f"{file_path}", "w") as file_out):
                file_out.write(file_in.read())
            os.remove(file_name)
