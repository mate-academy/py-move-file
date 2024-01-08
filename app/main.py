import os


# def move_file(command: str) -> None:
#     command_name, old_file, path = command.split()
#     path_dirs = path.split("/")
#     new_file = path_dirs.pop(-1)
#
#     with open(old_file, "r") as file_out:
#         content = file_out.read()
#         new_path = ""
#         for directory in path_dirs:
#             new_path += directory + "/"
#             if not os.path.exists(new_path):
#                 os.mkdir(new_path)
#         with open(new_path + new_file, "w") as file_in:
#             file_in.write(content)
#     os.remove(old_file)


def move_file(command: str) -> None:
    command_name, old_file, path, *_ = command.split()

    if command_name == "mv" and old_file != path:
        last_slash_index = path.rfind("/")
        path_dirs = path[:last_slash_index]
        os.makedirs(path_dirs, exist_ok=True)
        with open(old_file, "r") as file_out, open(path, "w") as file_in:
            content = file_out.read()
            file_in.write(content)
        os.remove(old_file)
