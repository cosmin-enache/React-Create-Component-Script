import sys
import os


def make_component_dir(name):
    os.mkdir(".\components\\" + name)

def split_cap(name):
    arr = name.split("-")
    res = ""

    for v in arr:
        res += v.capitalize()
    
    return res

def write_component(name):
    with open(".\components\\" + name + "\\" + name + ".component.jsx", "w") as file:
        cap_name = split_cap(name)
        file.write(
            "import styled from \"styled-components\"\n\n" + "const " + cap_name + " = () => {\n\treturn(\n\t\t\n\t)\n};\n\nexport default " + cap_name + ";"
        )


if not len(sys.argv) > 0:
    print("No arguments passed!")
    exit(-1)

name = sys.argv[1]
make_component_dir(name)
write_component(name)
