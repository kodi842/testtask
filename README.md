# testtask
# Image Generation API for Telegram Bot

This API provides image generation using DeepAI and Hugging Face Stable Diffusion.

## How to use

POST `/generate`

**Body:**
```json
{
  "prompt": "cat in sunglasses",
  "model": "deepai" // or "sd"
}
