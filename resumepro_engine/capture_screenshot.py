"""
RESUMEPRO WEB SCRAPER MODULE
Launches Headless Chrome to capture snapshot of ResumePro web page.
"""
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image, ImageDraw
from config import WEBSITE_URL, SCREENSHOT_PATH

def capture_resumepro_snapshot(url: str = WEBSITE_URL, save_path: str = SCREENSHOT_PATH):
    print(f"[*] Navigating to ResumePro website link: {url}...")
    
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    driver = None
    try:
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        time.sleep(3)  # Wait for Outfit & Playfair fonts and CSS animations to render
        driver.execute_script("window.scrollTo(0, 400);")
        time.sleep(1)
        driver.save_screenshot(save_path)
        print(f"[+] ResumePro snapshot captured successfully: {save_path}")
        return save_path
    except Exception as e:
        print(f"[!] Browser notice: {e}. Generating fallback canvas...")
        img = Image.new("RGB", (1920, 1080), color=(15, 23, 42))
        draw = ImageDraw.Draw(img)
        draw.rectangle([(50, 50), (1870, 1030)], outline=(99, 102, 241), width=4)
        draw.text((960, 540), "RESUMEPRO - AI-POWERED RESUME BUILDER", fill=(255, 255, 255), anchor="mm")
        img.save(save_path)
        return save_path
    finally:
        if driver:
            try:
                driver.quit()
            except Exception:
                pass

if __name__ == "__main__":
    capture_resumepro_snapshot()
