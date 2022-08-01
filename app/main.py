import os


def move_file(command: str):
    s = command.split(" ")
    catalog = (s[2]).split("/")

    if len(catalog) > 1:
        catalog_ = catalog[:-1]
        os.makedirs(catalog_)
        with open("s[1]", "r") as f, open("s[2]", "w") as f_:
            information = f.read()
            f_.write(information)

        os.remove("s[1]")


if __name__ == "__main__":
    move_file()
