import os


def move_file(mv_command: str) -> None:

    file_list = mv_command.strip().split()

    if len(file_list) == 3 and file_list[0] == "mv":
        src = file_list[1]
        dest = file_list[2]

        if not os.path.exists(src):
            return

        with open(src, "r") as file_in:
            content = file_in.read()

        dest_dir = os.path.dirname(dest)

        if dest_dir:
            os.makedirs(dest_dir, exist_ok=True)

        with open(dest, "w") as file_out:
            file_out.write(content)

        os.remove(file_list[1])
