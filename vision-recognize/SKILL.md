---
name: vision-recognize
description: Recognize image content (not OCR) and return structured Markdown. MCP server auto-invoked when the model detects image paths. Falls back to CLI for manual use.
---

# Vision Recognize

Image recognition (not OCR) — understands diagrams, charts, photos, screenshots, UI layouts, handwritten notes. Returns structured Markdown.

## Primary: MCP Server (auto-invoked)

The `vision-recognize` MCP server is registered globally. When the model sees an image path, it automatically calls the `recognize_image` tool — no manual `/vision-recognize` needed.

```
# Claude Code auto-invokes this when you provide an image path:
recognize_image(image_path="path/to/image.png")
```

### MCP Registration

```bash
claude mcp add vision-recognize -s user -- ~/.claude/venv/Scripts/python ~/.claude/skills/vision-recognize/mcp_server.py
```

### Dependencies

- Python venv at `~/.claude/venv`
- Packages: `mcp[cli]`, `requests`, `Pillow`
- Vision API: `https://token-plan-cn.xiaomimimo.com/v1`, model `mimo-v2.5`

## Fallback: CLI Script

If MCP is unavailable, use the CLI directly:

```bash
~/.claude/venv/Scripts/python ~/.claude/skills/vision-recognize/vision_recognize.py "<image_path>"
```

## Configuration

| Env Variable | Default | Description |
|---|---|---|
| `VISION_API_BASE` | `https://token-plan-cn.xiaomimimo.com/v1` | Vision API base URL |
| `VISION_API_KEY` | (内置) | API 认证 token |
| `VISION_MODEL` | `mimo-v2.5` | 识图模型名称 |
