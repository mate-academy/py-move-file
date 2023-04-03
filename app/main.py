import os


def move_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) == 3:
        command_id, file_name, file_path = command_parts
        if command_id != "mv":
            raise ValueError("Command should be 'mv'")

        head, tail = os.path.split(file_path)
        if head and not os.path.exists(head):
            os.makedirs(head)

        os.replace(file_name, file_path)
