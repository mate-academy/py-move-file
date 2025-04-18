import os
import shutil
import pytest

from app.main import move_file  # Переконайтеся, що шлях до вашої функції move_file правильний

create_file = 'file.txt'

@pytest.fixture
def create_file(tmp_path):
    file_path = tmp_path / "file.txt"
    file_path.write_text("Some content")
    return str(file_path)

def test_should_rename_file(create_file):
    source = create_file
    destination = "file2.txt"
    move_file(f"mv {source} {destination}")
    assert os.path.exists(destination)
    assert not os.path.exists(source)
    with open(destination, "r") as f:
        assert f.read() == "Some content"
    os.remove(destination)

def test_should_move_file_to_existing_directory(create_file, tmp_path):
    os.makedirs(tmp_path / "dir", exist_ok=True)
    source = create_file
    destination = str(tmp_path / "dir" / "file2.txt")
    move_file(f"mv {source} {destination}")
    assert os.path.exists(destination)
    assert not os.path.exists(source)
    with open(destination, "r") as f:
        assert f.read() == "Some content"
    os.remove(destination)

def test_should_create_and_move_file_to_new_directories(create_file):
    source = create_file
    destination = "first_dir/second_dir/file2.txt"
    move_file(f"mv {source} {destination}")
    assert os.path.exists(destination)
    assert not os.path.exists(source)
    with open(destination, "r") as f:
        assert f.read() == "Some content"
    shutil.rmtree("first_dir")

def test_should_work_when_directory_exists(create_file):
    if not os.path.exists("dir"):
        os.makedirs("dir")
    source = create_file
    destination = "dir/file2.txt"
    move_file(f"mv {source} {destination}")
    assert os.path.exists(destination)
    assert not os.path.exists(source)
    with open(destination, "r") as f:
        assert f.read() == "Some content"
    shutil.rmtree("dir", ignore_errors=True)
