import os


def move_file(command: str) -> None:
    use_params(make_params(command))


def make_params(command: str) -> list:
    try:
        command = command.split(" ")
        action = command[0]
        path = [command[1], command[2]]

        if action != "mv":
            print(f"There in no copy command! {action} != mv")

    except AttributeError:
        print("Not correct attribute in 'command'")
    else:
        return path


def use_params(path: list) -> None:
    try:
        if not os.path.exists(path[0]):
            print(f"Unable to access: {path[0]}")
            return

        directory_depth = path[1].split("/")
        current_path = ""
        for folder in range(len(directory_depth) - 1):
            current_path += str(directory_depth[folder]) + "/"
            if not os.path.exists(current_path):
                os.mkdir(current_path)

        with open(path[0], "r") as star_file, open(path[1], "w") as end_file:

            end_file.write(star_file.read())
            star_file.close()
            end_file.close()

    except FileNotFoundError:
        print("Copying is impossible!")
    else:
        os.remove(path[0])
        print("copying was successful")
