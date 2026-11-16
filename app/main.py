import os


def move_file(command: str) -> None:
    com = command.split()

    if len(com) == 3 and com[0] == "mv":
        _, second , third = com[0], com[1], com[2]

        current_path = ""
        if third.endswith("/"):
            third += second.split("/")[-1]
        if second == third:
            return
        folders = third.split("/")[:-1]
        for folder in folders:
            current_path = os.path.join(current_path, folder)
            if not os.path.exists(current_path):
                os.mkdir(current_path)
        with open(third, "w") as f:
            with open(second, "r") as p:
                f.write(p.read())
        os.remove(second)
