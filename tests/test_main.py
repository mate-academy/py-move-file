import os
import shutil

import pytest

from app.main import move_file


def _to_posix(path: str) -> str:
    return path.replace(os.sep, "/")


@pytest.fixture
def create_file(filename: str = "file.txt") -> str:
    content = "This is some\n content for\n the file."

    with open(filename, "w") as created_file:
        created_file.write(content)

    return filename


def test_file_renamed(create_file: str) -> None:
    move_file(f"mv {create_file} file1.txt")

    assert os.path.exists(create_file) is False
    with open("file1.txt", "r") as file_with_content:
        assert file_with_content.read() == "This is some\n content for\n the file."

    os.remove("file1.txt")


def test_should_work_when_directory_exists(create_file: str) -> None:
    os.makedirs("dir")
    destination = os.path.join("dir", "file2.txt")
    move_file(f"mv {create_file} {_to_posix(destination)}")

    with open(destination, "r") as file_with_content:
        assert file_with_content.read() == "This is some\n content for\n the file."

    assert os.path.exists(create_file) is False

    shutil.rmtree("dir")


def test_should_create_multiple_directories(create_file: str) -> None:
    destination = os.path.join("first_dir", "second_dir", "file2.txt")
    move_file(f"mv {create_file} {_to_posix(destination)}")

    assert os.path.exists(destination) is True
    assert os.path.exists(create_file) is False

    with open(destination, "r") as file_with_content:
        assert file_with_content.read() == "This is some\n content for\n the file."

    shutil.rmtree("first_dir")


def test_should_create_multiple_directories_when_they_exist(create_file: str) -> None:
    os.makedirs("first_dir/second_dir")
    destination = os.path.join("first_dir", "second_dir", "third_dir", "file2.txt")
    move_file(f"mv {create_file} {_to_posix(destination)}")

    with open(destination, "r") as file_with_content:
        assert file_with_content.read() == "This is some\n content for\n the file."

    assert os.path.exists(create_file) is False

    shutil.rmtree("first_dir")


def test_destination_ending_with_slash_is_directory(create_file: str) -> None:
    destination_dir = "dir"
    move_file(f"mv {create_file} {_to_posix(os.path.join(destination_dir, ''))}")

    assert os.path.exists(create_file) is False
    destination = os.path.join(destination_dir, create_file)
    assert os.path.exists(destination) is True

    with open(destination, "r") as file_with_content:
        assert file_with_content.read() == "This is some\n content for\n the file."

    shutil.rmtree(destination_dir)
