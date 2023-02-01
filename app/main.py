from pathlib import Path
import os


def move_file(command: str) -> None:
    comm_list = command.split(" ")

    if comm_list[0] == "mv":
        created_dir = ""
        new_file_path = list(Path(comm_list[2]).parts)
        orig_file = comm_list[1]
        n_f_name = orig_file

        if "." in new_file_path[-1].strip():
            n_f_name = new_file_path[-1]
            new_file_path.pop()

        if len(new_file_path) > 1:
            for index in range(len(new_file_path)):
                created_dir = os.path.join(created_dir, new_file_path[index])
                if not os.path.isdir(created_dir):
                    os.mkdir(created_dir)

        with open(orig_file, "r") as f_orig, \
                open(os.path.join(created_dir, n_f_name), "w") as f_copy:
            f_copy.write(f_orig.read())

        os.remove(orig_file)

    return
