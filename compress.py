# Сжимает фото в .webp для сайта.
# Установка: pip install pillow
# Запуск: положи исходники в папку raw/ рядом со скриптом и выполни: python compress.py
from pathlib import Path
from PIL import Image, ImageOps

SRC, OUT = Path("raw"), Path("img")
OUT.mkdir(exist_ok=True)
WIDTH = {"hero": 1920, "before": 1600, "after": 1600}  # остальные 900px

for f in SRC.iterdir():
    if f.suffix.lower() not in {".jpg", ".jpeg", ".png", ".webp", ".heic"}:
        continue
    img = ImageOps.exif_transpose(Image.open(f)).convert("RGB")
    w = WIDTH.get(f.stem, 900)
    if img.width > w:
        img = img.resize((w, round(img.height * w / img.width)), Image.LANCZOS)
    dst = OUT / f"{f.stem}.webp"
    img.save(dst, "WEBP", quality=72, method=6)
    print(f"{f.name} -> {dst} ({dst.stat().st_size // 1024} KB)")
