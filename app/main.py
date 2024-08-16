import os


def move_file(name: str) -> None:
    command = name.split()
    if command[0] != "mv":
        print("The command must have mv at the beginning")
        return
    target_file = command[2]
    target_path = target_file.split("/")
    print(target_path)
    source_file = command[1]
    if len(target_path) == 1:
        os.rename(source_file, target_file)
    else:
        path = ""
        for folder in target_path[:-1]:
            path += folder + "/"
            os.makedirs(path, exist_ok=True)

        with (open(source_file, "r") as file_in,
              open(target_file, "w") as file_out):
            file_out.write(file_in.read())
        os.remove(source_file)
