import os
import shutil


def move_file(command: str):
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command format. Expected \"mv source_path "
                         "destination_path\".")

    source_path_input = parts[1]
    destination_path_input = parts[2]

    if not os.path.exists(source_path_input):
        raise FileNotFoundError(f"No such file or directory: "
                                f'"{source_path_input}"')
    if not os.path.isfile(source_path_input):
        raise IsADirectoryError(f"Is a directory: \"{source_path_input}\". "
                                "Only files can be moved.")

    final_target_path = ""
    if destination_path_input.endswith("/") or \
       destination_path_input.endswith("\\"):
        file_name = os.path.basename(source_path_input)
        final_target_path = os.path.join(destination_path_input, file_name)
    else:
        final_target_path = destination_path_input

    source_abs_path = os.path.abspath(source_path_input)
    final_target_abs_path = os.path.abspath(final_target_path)

    if source_abs_path == final_target_abs_path:
        return

    target_dir = os.path.dirname(final_target_abs_path)
    if target_dir and not os.path.exists(target_dir):
        os.makedirs(target_dir)

    try:
        shutil.copy2(source_path_input, final_target_abs_path)
    except Exception as e:
        if os.path.exists(final_target_abs_path):
            os.remove(final_target_abs_path)
        raise OSError(f"Error moving file from \"{source_path_input}\" "
                      f"to \"{final_target_abs_path}\": {e}") from e
    else:
        os.remove(source_path_input)


if __name__ == "__main__":
    if os.path.exists("file.txt"):
        os.remove("file.txt")
    if os.path.exists("file2.txt"):
        os.remove("file2.txt")
    if os.path.exists("first_dir"):
        shutil.rmtree("first_dir")
    if os.path.exists("source_dir"):
        shutil.rmtree("source_dir")
    if os.path.exists("dest_dir"):
        shutil.rmtree("dest_dir")
    if os.path.exists("my_file.txt"):
        os.remove("my_file.txt")
    if os.path.exists("non_existent_file.txt"):
        os.remove("non_existent_file.txt")
    if os.path.exists("existing_file_for_self_move.txt"):
        os.remove("existing_file_for_self_move.txt")

    print("--- Test Case 1: Simple rename ---")
    with open("file.txt", "w") as f:
        f.write("Original content of file.txt\n")
    print(f"Content of file.txt before move:\n{open('file.txt').read()}")

    move_file("mv file.txt file2.txt")

    print(f"Content of file2.txt after move:\n{open('file2.txt').read()}")
    try:
        open("file.txt")
    except FileNotFoundError as e:
        print(f"Verified: {e}")
    print("-" * 30)

    if os.path.exists("file.txt"):
        os.remove("file.txt")
    if os.path.exists("file2.txt"):
        os.remove("file2.txt")

    print("--- Test Case 2: Move to nested directory, creating directories ---")
    with open("file.txt", "w") as f:
        f.write("Some\nText")
    print(f"Content of file.txt before move:\n{open('file.txt').read()}")

    move_file("mv file.txt first_dir/second_dir/third_dir/file2.txt")

    print("Content of first_dir/second_dir/third_dir/file2.txt after move:")
    print(open("first_dir/second_dir/third_dir/file2.txt").read())
    try:
        open("file.txt")
    except FileNotFoundError as e:
        print(f"Verified: {e}")
    print("-" * 30)

    if os.path.exists("file.txt"):
        os.remove("file.txt")
    if os.path.exists("first_dir"):
        shutil.rmtree("first_dir")

    print("--- Test Case 3: Move into an existing directory (ends with /) ---")
    os.makedirs("dest_dir")
    with open("my_file.txt", "w") as f:
        f.write("This is my file.\n")
    print(f"Content of my_file.txt before move:\n{open('my_file.txt').read()}")

    move_file("mv my_file.txt dest_dir/")

    print(f"Content of dest_dir/my_file.txt after move:\n"
          f"{open('dest_dir/my_file.txt').read()}")
    try:
        open("my_file.txt")
    except FileNotFoundError as e:
        print(f"Verified: {e}")
    print("-" * 30)

    if os.path.exists("my_file.txt"):
        os.remove("my_file.txt")
    if os.path.exists("dest_dir"):
        shutil.rmtree("dest_dir")

    print("--- Test Case 4: Source file does not exist ---")
    try:
        move_file("mv non_existent_file.txt some_dir/new_file.txt")
    except FileNotFoundError as e:
        print(f"Caught expected error: {e}")
    print("-" * 30)

    print("--- Test Case 5: Source is a directory "
          "(should raise IsADirectoryError) ---")
    os.makedirs("source_dir_to_move")
    try:
        move_file("mv source_dir_to_move/ destination/some_file.txt")
    except IsADirectoryError as e:
        print(f"Caught expected error: {e}")
    shutil.rmtree("source_dir_to_move")
    print("-" * 30)

    print("--- Test Case 6: Invalid command format ---")
    try:
        move_file("mv file.txt")
    except ValueError as e:
        print(f"Caught expected error: {e}")
    try:
        move_file("cp file.txt new_file.txt")
    except ValueError as e:
        print(f"Caught expected error: {e}")
    print("-" * 30)

    print("--- Test Case 7: Self-move (should do nothing) ---")
    with open("existing_file_for_self_move.txt", "w") as f:
        f.write("Self-move content.\n")
    initial_content = open("existing_file_for_self_move.txt").read()
    print(f"Initial content:\n{initial_content}")
    move_file("mv existing_file_for_self_move.txt "
              "existing_file_for_self_move.txt")
    final_content = open("existing_file_for_self_move.txt").read()
    print(f"Content after self-move (should be same):\n{final_content}")
    if initial_content == final_content:
        print("Verified: Self-move did not alter content.")
    else:
        print("Error: Self-move altered content.")
    print("-" * 30)

    print("--- All tests completed. ---")
