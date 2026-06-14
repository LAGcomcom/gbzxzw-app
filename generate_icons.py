#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os
from PIL import Image, ImageDraw

def main():
    src = r"E:\新建文件夹 (40)\eddb85b578e457139f85ca698fc147bc.jpg"
    base = r"E:\新建文件夹 (40)\gbzxzw-app\app\src\main\res"

    img = Image.open(src).convert("RGBA")
    print(f"Source size: {img.size}")

    # Regular launcher icons
    sizes = {
        "mipmap-mdpi": 48,
        "mipmap-hdpi": 72,
        "mipmap-xhdpi": 96,
        "mipmap-xxhdpi": 144,
        "mipmap-xxxhdpi": 192,
    }

    for folder, size in sizes.items():
        resized = img.resize((size, size), Image.LANCZOS)
        path = os.path.join(base, folder, "ic_launcher.png")
        resized.save(path, "PNG")
        print(f"Saved {path} ({size}x{size})")

    # Adaptive icon foregrounds
    foreground_sizes = {
        "mipmap-mdpi": 108,
        "mipmap-hdpi": 162,
        "mipmap-xhdpi": 216,
        "mipmap-xxhdpi": 324,
        "mipmap-xxxhdpi": 432,
    }

    for folder, fg_size in foreground_sizes.items():
        canvas = Image.new("RGBA", (fg_size, fg_size), (0, 0, 0, 0))
        inner = int(fg_size * 0.6667)
        offset = (fg_size - inner) // 2
        resized = img.resize((inner, inner), Image.LANCZOS)
        canvas.paste(resized, (offset, offset))
        path = os.path.join(base, folder, "ic_launcher_foreground.png")
        canvas.save(path, "PNG")
        print(f"Saved foreground {path} ({fg_size}x{fg_size})")

    # Round icons
    for folder, size in sizes.items():
        mask = Image.new("L", (size, size), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, size, size), fill=255)
        resized = img.resize((size, size), Image.LANCZOS)
        round_icon = Image.new("RGBA", (size, size), (0, 0, 0, 0))
        round_icon.paste(resized, (0, 0), mask)
        path = os.path.join(base, folder, "ic_launcher_round.png")
        round_icon.save(path, "PNG")
        print(f"Saved round {path} ({size}x{size})")

    print("\nAll icons generated successfully!")

if __name__ == "__main__":
    main()
