import os
from collections import namedtuple
from math import ceil
from time import time
from sys import argv, stdout
from PIL import Image

TargetFile = namedtuple("TargetFile", ["rawFileName", "targetFileName"])
IOType = [".jpg", ".png"]
start_time = time()

# Get argv

target_dir = argv[1]
ishidden = True if argv[2] == "True" else False
target_size = (int(argv[3]), int(argv[3]))

for i in range(2):
    if argv[4 + i] in ["png", "jpg", "ico"]:
        IOType[i] = "." + argv[4 + i]
    else:
        print(
            f"\033[31m[ERROR]\033[0m \033[33mUNVAILD TYPE\033[0m ({argv[3]}*{argv[3]})")
        exit()


# Search folder

try:
    files = os.listdir(target_dir)
    if not os.path.exists(f"{target_dir}/whirlpool_result"):
        print(
            "\033[34m[INFO]\033[0m \033[32mCREATE FOLDER\033[0m whirlpool_result")
        os.mkdir(f"{target_dir}/whirlpool_result")
except IOError:
    print(
        f"\033[31m[ERROR]\033[0m \033[33mUNVAILD PATH\033[0m {target_dir}")
    exit()


# Scan

progress_index = 0
target_files: list[TargetFile] = []

for f in files:
    tmp = os.path.splitext(f)
    progress_index = progress_index + 1
    if tmp[1] == IOType[0]:
        r = tmp[0] + IOType[1]
        target_files.append(TargetFile(f, r))
    print("\r", end="")
    print("\033[32m[SCAN] {:.1f}%:\033[0m".format(
        ceil(progress_index / len(files) * 100)), "\033[32m\u2593\033[0m" * ceil(progress_index / len(files) * 40), end="")
    stdout.flush()

print(f"\n\033[34m[INFO]\033[0m {len(target_files)} \033[32mFILES HAVE BEEN FOUND\033[0m\n")
progress_index = 0


# Work

for tf in target_files:
    im = Image.open(f"{target_dir}/" + tf.rawFileName)
    if IOType[1] == ".ico":
        im = im.resize(target_size)
    try:
        path = os.path.join(f"{target_dir}/whirlpool_result", tf.targetFileName)
        if (IOType[0] == ".png" or IOType[0] == ".ico" and IOType[1] == ".jpg"):
            im = im.convert("RGB")
            im.save(path, quality=95)
        elif (IOType[0] == ".jpg" and IOType[1] == ".ico" or IOType[0] == ".png"):
            im = im.convert("RGBA")
            im.save(path, quality=95)
        else:
            im.save(path, quality=95)
        if ishidden == False:
            print(f"\033[34m[INFO]\033[0m {tf.rawFileName} \033[32m-->\033[0m {tf.targetFileName}")
        else:
            print("\r", end="")
            print("\033[32m[WORK] {:.1f}%:\033[0m".format(
                ceil(progress_index / len(target_files) * 100)), "\033[32m\u2593\033[0m" * ceil(progress_index / len(target_files) * 40), end="")
            progress_index = progress_index + 1
            stdout.flush()
    except IOError:
        print(f"\033[33m[WARNING] [33mUNVAILD FILE\033[0m {tf.targetFileName}")
        continue



end_time = time()
run_time = end_time - start_time

if ishidden:
    print()

print(f"\033[34m[INFO]\033[0m \033[32mOUTPUT PATH\033[0m {target_dir}\\whirlpool_result")
if IOType[1] == "ico":
    print(f"\033[34m[INFO]\033[0m \033[32mSIZE\033[0m ({target_size[0]}*{target_size[1]})")
print(f"\033[34m[INFO]\033[0m {IOType[0]} \033[32m-->\033[0m {IOType[1]}")
print(f"\033[34m[INFO]\033[0m \033[32mFINISHED\033[0m {len(target_files)} \033[32mTASKS IN\033[0m {run_time:.4f} \033[32mSECONDS\033[0m")
