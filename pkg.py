import os


def main():
    pip_pkg = ["pynput"]
    for i in pip_pkg:
        if (os.system(f"pip show {i}")) == 0:
            print(f"{i} is Installed")
        else:
            os.system(f"pip install {i}")
            print(f"{i} Finish Installation")

__name__ == '__main__':
    main()