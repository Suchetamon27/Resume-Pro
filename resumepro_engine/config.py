"""
RESUMEPRO AI POSTER ENGINE.
"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

# Output Paths
SCREENSHOT_PATH = str(OUTPUT_DIR / "resumepro_snapshot.png")
POSTER_OUTPUT_PATH = str(OUTPUT_DIR / "resumepro_promo_poster.jpg")

# 1. TARGET WEBSITE / REPOSITORY LINK
WEBSITE_URL = os.getenv("WEBSITE_URL", "https://github.com/Suchetamon27/Resume-Pro")

# 2. BRAND THEME & COLORS (Matched to attached index.html: Indigo #6366F1 & Dark Slate #0F172A)
BRAND_NAME = "RESUMEPRO"
BRAND_PRIMARY_COLOR = (15, 23, 42)      # Dark Slate RGB (#0F172A)
BRAND_ACCENT_COLOR = (99, 102, 241)     # Indigo RGB (#6366F1)
BRAND_SECONDARY_COLOR = (236, 72, 153)  # Pink Accent RGB (#EC4899)

# 3. CREDENTIALS
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "YOUR_GEMINI_API_KEY")
WHATSAPP_GROUP_ID = os.getenv("WHATSAPP_GROUP_ID", "Job_Seekers_VIP_Group")
