#!/usr/bin/env python3
"""Vision-Recognize MCP Server — image recognition via mimo-v2.5 vision API."""

import base64
import io
import os
import sys
from pathlib import Path

try:
    from PIL import Image
    import requests
except ImportError:
    print(
        "ERROR: Missing dependencies. Run: pip install requests Pillow",
        file=sys.stderr,
    )
    sys.exit(1)

from mcp.server.fastmcp import FastMCP

# ---------------------------------------------------------------------------
# Config (overridable via env vars)
# ---------------------------------------------------------------------------
MAX_LONG_SIDE = 1280
DEFAULT_PROMPT = "识别图片里所有信息，使用 markdown 输出全部内容，并保持排版的一致"

API_BASE = os.environ.get(
    "VISION_API_BASE", "https://token-plan-cn.xiaomimimo.com/v1"
)
API_KEY = os.environ.get(
    "VISION_API_KEY", "tp-cb6w5uxun0mi2q9un0cls4fqanqy4mxsplvxwsr5qpc01y4x"
)
MODEL = os.environ.get("VISION_MODEL", "mimo-v2.5")

# ---------------------------------------------------------------------------
# Vision helpers (from vision_recognize.py)
# ---------------------------------------------------------------------------


def resize_image(image_path: str) -> bytes:
    img = Image.open(image_path)
    w, h = img.size
    if max(w, h) > MAX_LONG_SIDE:
        scale = MAX_LONG_SIDE / max(w, h)
        img = img.resize((int(w * scale), int(h * scale)), Image.LANCZOS)
    buf = io.BytesIO()
    fmt = img.format or "PNG"
    if fmt.upper() == "JPG":
        fmt = "JPEG"
    img.save(buf, format=fmt)
    return buf.getvalue()


def encode_image(image_bytes: bytes) -> str:
    return base64.b64encode(image_bytes).decode("utf-8")


def get_mime_type(image_path: str) -> str:
    ext = Path(image_path).suffix.lower()
    mime_map = {
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".gif": "image/gif",
        ".webp": "image/webp",
        ".bmp": "image/bmp",
    }
    return mime_map.get(ext, "image/png")


def call_vision_api(image_path: str, prompt: str) -> str:
    url = f"{API_BASE.rstrip('/')}/chat/completions"

    image_bytes = resize_image(image_path)
    b64 = encode_image(image_bytes)
    mime = get_mime_type(image_path)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }

    payload = {
        "model": MODEL,
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:{mime};base64,{b64}"},
                    },
                ],
            }
        ],
        "max_tokens": 4096,
    }

    resp = requests.post(url, json=payload, headers=headers, timeout=120)
    resp.raise_for_status()
    data = resp.json()
    return data["choices"][0]["message"]["content"]


# ---------------------------------------------------------------------------
# MCP Server
# ---------------------------------------------------------------------------

mcp = FastMCP("vision-recognize")


@mcp.tool()
def recognize_image(image_path: str, prompt: str = DEFAULT_PROMPT) -> str:
    """Recognize visual content in an image and return structured Markdown.

    Args:
        image_path: Absolute path to an image file (.png, .jpg, .jpeg, .gif, .webp, .bmp).
        prompt: Custom recognition prompt (optional, defaults to full-content extraction).

    Returns:
        Markdown text describing all recognized content in the image.
    """
    if not os.path.isfile(image_path):
        return f"ERROR: File not found: {image_path}"

    try:
        return call_vision_api(image_path, prompt)
    except requests.exceptions.RequestException as e:
        return f"ERROR: Vision API request failed — {e}"
    except Exception as e:
        return f"ERROR: {e}"


if __name__ == "__main__":
    mcp.run(transport="stdio")
