import os


def move_file(command: str) -> None:
    cmd, input_f, output_f = command.split()

    if cmd == "mv" and not command.endswith("/"):
        location_segments = output_f.split("/")

        if len(location_segments) > 1:
            for i in range(len(location_segments) - 1):
                dir_path = "/".join(location_segments[0:i + 1])

                if not os.path.exists(dir_path):
                    os.makedirs(dir_path)

        with (open(input_f, "r") as input_file,
              open(output_f, "w") as output_file):
            output_file.write(input_file.read())

        os.remove(input_f)
