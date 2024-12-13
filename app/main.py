import os


def move_file(command: str) -> None:
    if len(command.split()) != 3:
        raise ValueError("The command must be 'mv file.txt dir/new.txt'")
    input_command, source_path, move_path = command.split()
    if input_command != "mv":
        raise ValueError("The command should be 'mv'")
    head_tail = os.path.split(move_path)
    if head_tail[0] != "":
        os.makedirs(head_tail[0], exist_ok=True)
    os.replace(source_path, move_path)
