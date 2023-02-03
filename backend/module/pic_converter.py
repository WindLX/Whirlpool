from PIL import Image
from enum import Enum
import re


class PicType(Enum):
    png = ".png"
    jpg = ".jpg"
    jpeg = ".jpeg"
    ico = ".ico"


def pic_converter(raw_pic: str, target_type: PicType) -> str:
    image = Image.open(raw_pic)
    raw_name = re.match(r"(.+)\.", raw_pic).group()
    raw_type = PicType(re.match(r".+(\.\w+)", raw_pic).group())
    if raw_type == PicType.png:
        if target_type == PicType.ico:

            t.save(f"{raw_name}.ico")
            return raw_name + ".ico"


def png2jpg(raw_image: Image) -> Image:
    pass


def png2jpeg(raw_image: Image) -> Image:
    pass


def jpg2png(raw_image: Image) -> Image:
    pass


def jpg2jpeg(raw_image: Image) -> Image:
    pass


def jpg2ico(raw_image: Image) -> Image:
    pass


def jpeg2png(raw_image: Image) -> Image:
    pass


def jpeg2jpg(raw_image: Image) -> Image:
    pass


def jpeg2ico(raw_image: Image) -> Image:
    pass
