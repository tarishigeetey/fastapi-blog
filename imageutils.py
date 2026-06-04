import uuid
from io import BytesIO
from pathlib import Path
from PIL import Image, ImageOps

PROFILE_PICS_DIR = Path("media/profile_pics")


def process_profile_image(content: bytes) -> str:  # type: ignore
    with Image.open(BytesIO(content)) as original:
        img = ImageOps.exif_transpose(original)
        img = ImageOps.fit(img, (300, 300), method=Image.Resampling.LANCZOS)

        if img.mode in ("RGBA", "LA", "P"):
            img = img.convert("RGB")

        filename = f"{uuid.uuid4().hex}.jpg"
        file_path = PROFILE_PICS_DIR / filename

        PROFILE_PICS_DIR.mkdir(parents=True, exist_ok=True)
        img.save(file_path, format="JPEG", quality=85, optimize=True)
    return filename


def delete_profile_image(filename: str | None) -> None:
    if filename is None:
        return
    file_path = PROFILE_PICS_DIR / filename
    if file_path.exists():
        file_path.unlink()
