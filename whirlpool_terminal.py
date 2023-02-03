import os
from re import match
from math import ceil
from datetime import datetime
from sys import argv, stdout
from PIL import Image

start_time = datetime.now()

my_argv = argv

size = (256, 256)
ishidden = False

if (len(argv) > 3):
    print(
        f"\033[33m[WARNING] TOO MUCH ARGUMENTS\033[0m")

try:
    ishidden = True if any(
        list(map(lambda ih: ih == "-h", my_argv))) else False
    if ishidden:
        my_argv.remove("-h")
except IndexError:
    ishidden = False

try:
    target_dir = my_argv[1]
except IndexError:
    target_dir = r"./"

try:
    target_size = (int(my_argv[2]), int(my_argv[2]))
except IndexError:
    target_size = (256, 256)
except ValueError:
    print(
        f"\033[31m[ERROR]\033[0m \033[33mUNVAILD SIZE\033[0m ({argv[2]}*{argv[2]})")
    exit()

try:
    files = os.listdir(target_dir)
    if not os.path.exists(f"{target_dir}/whirlpool_result"):
        print(
            "\033[34m[INFO]\033[0m \033[32mCREATE FOLDER\033[0m whirlpool_result\n")
        os.mkdir(f"{target_dir}/whirlpool_result")
except IOError:
    print(
        f"\033[31m[ERROR]\033[0m \033[33mUNVAILD PATH\033[0m {target_dir}")
    exit()

number = len(files)
progress_index = 0

for f in files:
    tmp = os.path.splitext(f)
    if tmp[1] in [".png", ".jpg", ".ico"]:
        r = tmp[0] + ".ico"
        im = Image.open(f"{target_dir}/" + f).resize(size)
        try:
            path = os.path.join(f"{target_dir}/whirlpool_result", r)
            im.save(path)
            if ishidden == False:
                print(f"\033[34m[INFO]\033[0m {f} \033[32m-->\033[0m {r}")
            else:
                print("\r", end="")
                print("\033[32m[PROGRESS] {:.1f}%:\033[0m".format(
                    ceil(progress_index / number * 100)), "\033[32m\u2593\033[0m" * ceil(progress_index / number * 40), end="")
                progress_index = progress_index + 1
                stdout.flush()
        except IOError:
            print(f"\033[33m[WARNING] [33mUNVAILD FILE\033[0m {f}")
            continue

end_time = datetime.now()
run_time = (end_time - start_time).seconds

if number != 0:
    print()

print(
    f"\033[34m[INFO]\033[0m \033[32mOUTPUT PATH\033[0m {target_dir}\\whirlpool_result\n" +
    f"\033[34m[INFO]\033[0m \033[32mSIZE\033[0m ({target_size[0]}*{target_size[1]})" +
    f"\n\033[34m[INFO]\033[0m \033[32mFINISHED\033[0m {number} \033[32mTASKS IN\033[0m {run_time} \033[32mSECONDS\033[0m")
