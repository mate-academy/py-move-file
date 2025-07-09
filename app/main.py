import os


def move_file(command: str) -> None:
    try:
        cmd, start_path, final_path = command.split(" ")
        if start_path == final_path or cmd != "mv":
            return
    except ValueError:
        return
    if "/" in final_path:
        path_parts = final_path.split("/")
        file_name = path_parts.pop()
        path = path_parts[0]

        if not os.path.exists(path):
            os.mkdir(path)

        for part in path_parts[1:]:
            path = f"{path}/{part}"
            if not os.path.exists(path):
                os.mkdir(path)
        final_path = f"{path}/{file_name}"

    with open(start_path) as curr_file, open(final_path, "w") as final_file:
        for line in curr_file:
            final_file.write(line)

    os.remove(start_path)
