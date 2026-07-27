"""
RESUMEPRO WHATSAPP BROADCAST DISPATCHER
Sends generated poster image and change summary to WhatsApp groups.
"""
import sys
import pywhatkit as pwk
from config import WHATSAPP_GROUP_ID, POSTER_OUTPUT_PATH, WEBSITE_URL, BRAND_NAME

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def dispatch_resumepro_whatsapp(poster_path: str = POSTER_OUTPUT_PATH, group_id: str = WHATSAPP_GROUP_ID):
    print(f"[*] Preparing WhatsApp payload for group '{group_id}'...")
    
    caption = (
        f"🚀 *{BRAND_NAME} - NEW RELEASE LAUNCH* 🚀\n\n"
        f"A new feature update was just pushed to *Suchetamon27/Resume-Pro*!\n\n"
        f"✨ *Key Highlights:*\n"
        f"• Gemini AI Professional Summary Generator\n"
        f"• 1-Click Instant High-Res PDF Export\n"
        f"• 99% ATS Pass Rate & Modern Templates\n\n"
        f"🔗 *Explore Code & Demo:* {WEBSITE_URL}\n"
        "_Unsubscribe: Reply STOP_"
    )
    
    try:
        pwk.sendwhats_image_to_group(group_id=group_id, image_path=poster_path, caption=caption, wait_time=15)
        print("[+] WhatsApp broadcast sent successfully!")
    except Exception as e:
        print(f"[!] WhatsApp dispatch notice: {e}")

if __name__ == "__main__":
    dispatch_resumepro_whatsapp()
