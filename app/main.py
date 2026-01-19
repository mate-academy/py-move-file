import os


def move_file(command_line: str) -> None:
    command = command_line.split()
    if command[0] != "mv" or len(command) != 3:
        return

    source_file, target = command[1], command[2].split(os.sep)
    target_name = target[-1]
    target_path = ""
    target.pop(-1)
    for dir_name in target:
        target_path = os.path.join(target_path, dir_name)
        if not os.path.exists(target_path):
            os.mkdir(target_path)

    with open(source_file, "r") as file:
        files_content = file.read()
        os.remove(source_file)

    target_path = os.path.join(target_path, target_name)
    with open(target_path, "w") as file:
        file.write(files_content)
