import os


def move_file(command: str) -> None:
    if len(command.split()) == 3:
        command, file, new_file = command.split()
        if command == "mv":
            if "/" not in new_file:
                with open(file, "r") as f1, open(new_file, "w") as f2:
                    f2.write(f1.read())
                    f1.close()
                    f2.close()
                os.remove(os.path.abspath(file))
            else:
                dirs = new_file.split("/")
                dirs.pop()
                os.makedirs("/".join(dirs), exist_ok=True)
                with open(file, "r") as f1, open(new_file, "w") as f2:
                    f2.write(f1.read())
                    f1.close()
                    f2.close()
                os.remove(os.path.abspath(file))
