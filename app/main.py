import os


def move_file(command: str) -> None:
    if command == "":
        return
    list_of_files = command.strip().split()
    if len(list_of_files) != 3 or list_of_files[0] != "mv":
        return
    mv, source, path_to_file = list_of_files
    new_file = path_to_file.split("/")[-1]
    path = "/".join(path_to_file.split("/")[:-1])
    if "/" not in path_to_file:
        os.rename(source, path_to_file)
        return
    os.makedirs(path, exist_ok=True)
    dest_path = os.path.join(path, new_file)
    if os.path.exists(dest_path):
        os.remove(dest_path)

    os.rename(source, dest_path)
