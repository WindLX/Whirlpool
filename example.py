import os
from PIL import Image

files = os.listdir(r"D:/Downloads")
size = (256, 256)

if not os.path.exists("D:/Downloads/res"):
    os.mkdir("D:/Downloads/res")

for f in files:
    tmp = os.path.splitext(f)
    print(f)
    if tmp[1] == ".png":
        r = tmp[0] + ".ico"
        im = Image.open("D:/Downloads/" + f).resize(size)
        try:
            path = os.path.join("D:/Downloads/res", r)
            im.save(path)
            print(f"{f} --> {r}")
        except IOError:
            print(f"Unvaild file: {f}")
