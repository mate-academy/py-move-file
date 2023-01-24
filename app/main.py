import os


def move_file(command: str) -> None:
    if len(command.split(" ")) == 3:
        cmd, source, target = command.split(" ")
        if cmd == "mv":
            if "/" not in target:
                with (
                    open(source, "r") as src_file,
                    open(target, "w") as tg_file
                ):
                    tg_file.write(src_file.read())
                os.remove(source)
            else:
                target = target.split("/")
                path = ""
                target_file = target[2]
                for i in range(len(target) - 1):
                    path += target[i] + "/"
                target = os.path.join(path, target_file)
                os.mkdir(path)
                with (
                    open(source, "r") as src_file,
                    open(target[len(target) - 1], "w") as tg_file
                ):
                    tg_file.write(src_file.read())

                os.remove(source)


# move_file("mv test.txt new_test.txt")
move_file("mv test.txt D:/pt_prj/new_test2.txt")
