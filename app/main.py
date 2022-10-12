import os


BUFFER_SIZE = 2048


def move_file(user_command: str) -> None:
    character_separator = "/"

    class FileInfo:
        def __init__(self, file_name: str) -> None:
            self.path = []
            self.full_path = ""
            self.path_only = False
            self.filename = ""
            self.full_filename = ""

            if file_name[-1] == character_separator:
                self.path = file_name[:-1].split(character_separator)
                self.full_path = file_name.rstrip(character_separator)
                self.path_only = True
            else:
                self.full_filename = file_name
                temp = file_name.split(character_separator)
                self.filename = temp[-1]
                self.path = temp[:-1]
                self.full_path = character_separator.join(self.path)

        def path_add_filename(self, filename: str) -> str:
            if self.path and self.path_only:
                return character_separator.join((self.full_path, filename))
            return self.full_filename

    command = user_command.split()
    if len(command) != 3 or \
            command[0].lower() != "mv" or \
            command[1] == command[2]:
        return

    fileinfo1 = FileInfo(command[1])
    if not os.path.isfile(fileinfo1.full_filename) \
            or fileinfo1.path_only is True:
        return

    fileinfo2 = FileInfo(command[2])
    if fileinfo1.full_path == fileinfo2.full_path:
        os.rename(fileinfo1.full_filename, fileinfo2.full_filename)
    else:
        path_traverse = ""
        for path in fileinfo2.path:
            path_traverse += \
                (character_separator if path_traverse else "") + path
            if not os.path.isdir(path_traverse):
                os.mkdir(path_traverse)

        full_filename2 = fileinfo2.path_add_filename(fileinfo1.filename)
        with open(fileinfo1.full_filename, "rb") as src_obj, \
                open(full_filename2, "wb") as dest_obj:
            buffer = src_obj.read(BUFFER_SIZE)
            while buffer:
                dest_obj.write(buffer)
                buffer = src_obj.read()

        if os.path.isfile(full_filename2):
            os.remove(fileinfo1.full_filename)


if __name__ == "__main__":
    move_file("mv file1.txt file2.txt")
    input("file2.txt")
    move_file("mv file2.txt file1.txt")
    input("file1.txt")
    move_file("mv file1.txt first_dir/second_dir/third_dir/")
    input("first_dir/second_dir/third_dir/file1.txt")
    move_file("mv first_dir/second_dir/third_dir/file1.txt "
              "first_dir/second_dir/third_dir/file2.txt")
    input("first_dir/second_dir/third_dir/file2.txt")
    move_file("mv first_dir/second_dir/third_dir/file2.txt file1.txt")
    input("file1.txt")
