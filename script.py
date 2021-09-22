import sys
import os


def make_component_dir(name):
    os.mkdir(".\components\\" + name)


def write_component(name):
    with open(".\components\\" + name + "\\" + name + ".component.jsx", "w") as file:
        file.write("")


def write_stylesheet(name):
    with open(".\components\\" + name + "\\" + name + ".styling.css", "w") as file:
        file.write("")


if not len(sys.argv) > 0:
    print("No arguments passed!")
    exit(-1)

name = sys.argv[1]
make_component_dir(name)
write_component(name)
write_stylesheet(name)
