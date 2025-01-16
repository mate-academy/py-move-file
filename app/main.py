import os


def move_file(command: str) -> None:
    our_list = command.split()
    if len(our_list) == 3:
        if our_list[0] == "mv":
            if our_list[2][-1] != "/":
                name = ""
                if "/" in our_list[2]:
                    our_dir_list = our_list[2].split("/")
                    counter = 0
                    while counter < len(our_dir_list) - 1:
                        if counter == 0:
                            name += our_dir_list[counter]
                        else:
                            name += ("/" + our_dir_list[counter])
                        if not os.path.exists(name):
                            os.mkdir(name)
                        if counter == len(our_dir_list) - 2:
                            name += ("/" + our_dir_list[counter + 1])
                        counter += 1
                else:
                    name += our_list[2]
                with (open(our_list[1], "r") as read_file,
                      open(name, "w") as write_file):
                    write_file.write(read_file.read())
                os.remove(our_list[1])
