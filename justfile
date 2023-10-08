set shell := ["cmd.exe", "/c"]

test:
    @pytest

@clean:
    echo Cleaning the directory
    IF EXIST __pycache__ (rmdir /s /q __pycache__)
    IF EXIST db\\__pycache__ (rmdir /s /q db\\__pycache__)
    IF EXIST tests\\__pycache__ (rmdir /s /q tests\\__pycache__)
    IF EXIST .pytest_cache (rmdir /s /q .pytest_cache)
    echo Directory cleaned