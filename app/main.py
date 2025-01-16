import os


def move_file(command: str) -> None:
    our_list = command.split()
    if len(our_list) == 3:
        if our_list[0] == "mv":
            if our_list[2][-1] != "/":
                destination_path = ""
                if "/" in our_list[2]:
                    our_dir_list = our_list[2].split("/")
                    counter = 0
                    while counter < len(our_dir_list) - 1:
                        if counter == 0:
                            destination_path += our_dir_list[counter]
                        else:
                            destination_path = os.path.join(
                                destination_path,
                                our_dir_list[counter]
                            )
                        if not os.path.exists(destination_path):
                            os.mkdir(destination_path)
                        else:
                            pass
                        if counter == len(our_dir_list) - 2:
                            destination_path = os.path.join(
                                destination_path,
                                our_dir_list[counter + 1]
                            )
                        counter += 1
                else:
                    destination_path += our_list[2]
                with (open(our_list[1], "r") as read_file,
                      open(destination_path, "w") as write_file):
                    write_file.write(read_file.read())
                os.remove(our_list[1])
