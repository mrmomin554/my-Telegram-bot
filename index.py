!pip install pyTelegramBotAPI

import telebot
from telebot import types
import logging

# লগিং সেটআপ
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# বট টোকেন
TOKEN = "8349462752:AAEuj2YifbEWxmu_XH74ivlq_VU6zKMkcxg"

# বট ইনস্ট্যান্স তৈরি
bot = telebot.TeleBot(TOKEN)

# MR MOMIN ⚡ এর তথ্য
OWNER_NAME = "MR MOMIN ⚡"
OWNER_USERNAME = "@MRMOMIN112"

# ডিফল্ট ওয়েবসাইট URL
DEFAULT_WEBSITE = "https://zefoy.com"

# কমান্ড হ্যান্ডলার
@bot.message_handler(commands=['start'])
def send_welcome(message):
    try:
        user_id = message.from_user.id
        first_name = message.from_user.first_name
        
        # সুন্দর বক্স ডিজাইনের সাথে ওয়েলকাম মেসেজ
        welcome_text = f"""
╔══════════════════════╗
║   🚀 POWERFUL BOT    ║
║    by {OWNER_NAME}   ║
╚══════════════════════╝

✨ *স্বাগতম, {first_name}!* ✨

এটি একটি প্রিমিয়াম ওয়েব এক্সেস বট। 
নিচের বাটনে ক্লিক করে বিশেষ কন্টেন্ট অ্যাক্সেস করুন।

📅 তারিখ: September 20, 2024
⏰ সময়: 1:49 AM

*ডেভেলপার:* {OWNER_NAME}
*ইউজারনেম:* {OWNER_USERNAME}
        """
        
        # ইনলাইন কীবোর্ড তৈরি (ওপেন বাটন সহ)
        markup = types.InlineKeyboardMarkup()
        open_button = types.InlineKeyboardButton(
            "🌟 ওপেন করুন", 
            web_app=types.WebAppInfo(url=DEFAULT_WEBSITE)
        )
        markup.add(open_button)
        
        # ছবির মতো ডিজাইনে মেসেজ পাঠানো
        box_design = """
╔══════════════════════╗
║                      ║
║   📱 WEBSITE ACCESS  ║
║                      ║
║   নিচের বাটনে ক্লিক করে   ║
║   কন্টেন্ট অ্যাক্সেস করুন  ║
║                      ║
╚══════════════════════╝
        """
        
        # প্রথমে বক্স ডিজাইন পাঠানো
        bot.send_message(message.chat.id, box_design)
        
        # তারপর ওপেন বাটন সহ মেসেজ পাঠানো
        bot.send_message(
            message.chat.id, 
            welcome_text, 
            parse_mode='Markdown',
            reply_markup=markup
        )
        
    except Exception as e:
        logger.error(f"Error in /start command: {e}")

@bot.message_handler(commands=['open'])
def open_website(message):
    try:
        # ইনলাইন কীবোর্ড তৈরি (ওপেন বাটন সহ)
        markup = types.InlineKeyboardMarkup()
        open_button = types.InlineKeyboardButton(
            "🌟 ওপেন করুন", 
            web_app=types.WebAppInfo(url=DEFAULT_WEBSITE)
        )
        markup.add(open_button)
        
        # বক্স ডিজাইনের সাথে মেসেজ পাঠানো
        box_design = """
╔══════════════════════╗
║                      ║
║   🔒 PREMIUM ACCESS  ║
║                      ║
║   এক্সক্লুসিভ কন্টেন্ট   ║
║   অ্যাক্সেস করতে নিচের    ║
║   বাটনে ক্লিক করুন     ║
║                      ║
╚══════════════════════╝
        """
        
        bot.send_message(
            message.chat.id,
            box_design,
            reply_markup=markup
        )
        
    except Exception as e:
        logger.error(f"Error in /open command: {e}")

# টেক্সট মেসেজ হ্যান্ডলার
@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    try:
        text = message.text
        
        if text == '❓ সাহায্য':
            help_text = f"""
🤖 *সাহায্য কেন্দ্র*

*উপলব্ধ কমান্ড:*
/start - বট শুরু করুন
/open - ওয়েবসাইট ওপেন করুন

*বট মালিক:* {OWNER_NAME}
*ইউজারনেম:* {OWNER_USERNAME}

এই বটটি ব্যবহার করে আপনি প্রিমিয়াম কন্টেন্ট অ্যাক্সেস করতে পারবেন।
            """
            bot.send_message(message.chat.id, help_text, parse_mode='Markdown')
        else:
            bot.send_message(message.chat.id, "দুঃখিত, আমি এই কমান্ডটি বুঝতে পারিনি। /start টাইপ করে বট শুরু করুন।")
            
    except Exception as e:
        logger.error(f"Error handling message: {e}")

print("✅ বট সফলভাবে শুরু হয়েছে...")
print(f"👤 বট মালিক: {OWNER_NAME}")
print("🤖 বটটি এখনアクティブ এবং বার্তার জন্য অপেক্ষা করছে...")

bot.polling(none_stop=True)
