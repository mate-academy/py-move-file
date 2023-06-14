import re
import os


def move_file(command: str) -> None:
    words = re.split(r"[ ]", command)
    if words[0] == "mv":
        path_words = re.split(r"[/]", words[2])
        current_path = ""
        for folder in path_words[: -1]:
            current_path += folder
            if not os.path.exists(current_path):
                os.mkdir(current_path)
                print("else", current_path)
            current_path += "/"
            print("FIN", current_path)

        with open(words[1], "r") as file_in, open(words[2], "w") as file_out:
            file_out.write(file_in.read())
            print("===", words[2])
            os.remove(words[1])
