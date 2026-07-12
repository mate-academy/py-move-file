import os


def move_file(command: str) -> None:
    command = command.split()
    if len(command) == 3 and command[0] == "mv":
        action, file_origin, option = command
    else:
        return

    if "/" not in option:
        os.rename(file_origin, option)
        return
    elif "/" in option:
        last_element = os.path.basename(option)
        if last_element:
            new_file = last_element
            current_path = option.replace(last_element, "")
        elif not last_element:
            new_file = file_origin
            current_path = option

    if not os.path.exists(current_path):
        os.makedirs(current_path)

    with open(file_origin, "r") as origin_file_object:
        content = origin_file_object.readlines()
    with open(os.path.join(current_path, new_file), "w") as new_file_object:
        new_file_object.writelines(content)

    os.remove(file_origin)
