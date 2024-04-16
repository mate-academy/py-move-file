import os


def move_file(command: str) -> None:
    cmd, source_name, destination_name = "", "", ""
    try:
        cmd, source_name, destination_name = command.split()
    except Exception:
        print("Error in cmd!")
    print(cmd, source_name, destination_name)

    dir_str = ""

    if cmd == "mv":
        if "/" in destination_name:
            list_dir = destination_name.split("/")

            for i in range(len(list_dir) - 1):
                dir_str += list_dir[i] + "/"

                try:
                    print(dir_str)
                    os.mkdir(dir_str)
                except Exception:
                    print("Err_dir")

        with (open(source_name) as f_source,
              open(destination_name, "w") as f_destination):
            buff = f_source.read()
            f_destination.write(buff)

        os.remove(source_name)
