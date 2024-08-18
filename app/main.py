import os


def move_file(command: str) -> None:
    [part0, part1, part2] = command.split(" ")
    if part0 == "mv":
        path = part2.split("/")
        new_file = path[-1]
        direction = "/".join(path[:-1])

        if direction:
            path_with_dot = f"./{direction}"

            if not os.path.exists(path_with_dot):
                os.makedirs(path_with_dot)

            with (open(part1, "r") as first_file,
                  open(f"{path_with_dot}/{new_file}", "w") as second_file):
                for line in first_file:
                    second_file.write(line)
                first_file.close()
                second_file.close()
                os.remove(part1)
        else:
            os.rename(part1, new_file)
