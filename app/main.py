import os


def move_file(line: str) -> None:
    if line == "":
        return

    line_list = line.strip().split()

    if len(line_list) != 3 and line_list[0] != "mv":
        return
    file1 = line_list[1]
    file2 = line_list[2]
    dest_dir = os.path.dirname(file2)

    if dest_dir and not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    try:
        with open(file1, "r") as file_in:
            content = file_in.read()

        with open(file2, "w") as file_out:
            file_out.write(content)

        os.remove(file1)
    except FileNotFoundError:
        return
