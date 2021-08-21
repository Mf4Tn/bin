import telebot , requests , json  , random , time
from telebot import types

token = "1869953546:AAGOQKD2U6VIblP9alc1SMIxCPiCqp0H1E0"
sudo = 906630665
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start(message):
    abt = types.InlineKeyboardMarkup(row_width=2)
    ab = types.InlineKeyboardButton(message.chat.first_name,callback_data="F")
    ab1 = types.InlineKeyboardButton(message.from_user.id,callback_data="LL")
    ab2 = types.InlineKeyboardButton("Username : " + message.from_user.username,url=f"https://t.me/{message.from_user.username}")
    abt.add(ab)
    abt.add(ab1)
    abt.add(ab2)
    bot.send_message(sudo,"New One Join Our Bot Boss 😉",reply_markup=abt)
    with open("id.txt","a")as idmt3k:idmt3k.write(str(message.from_user.id)+"\n")
    global iii 
    iii = 0
    k = 0
    w = str(k)
    g = 0
    x = types.InlineKeyboardMarkup(row_width=2)
    b = types.InlineKeyboardButton(f"Good ✅ : {w}",callback_data="F1")
    x.add(b)
    c = types.InlineKeyboardButton(f"Bad ⚠  : {g}️",callback_data="F2")
    x.add(c)
    bot.send_message(message.chat.id,"*Checking Bins ...*",parse_mode="markdown",reply_markup=x)
    for i in range(31):
        iii +=1
        if iii != 31:
            id_msg = message.message_id +2
            idk = str("".join(random.choice("1234567890")for m in range(8)))
            try :
                bin = "3"+idk
                
                url = f"https://bin-checker.net/api/{bin}"
                r = requests.get(url)
                url1 = f"https://lookup.binlist.net/{bin}"
                r1 = requests.get(url1)
                bins = str(bin)
                #time.sleep(2)
                if "emoji" in r1.text and "CREDIT" in r.text:
                    url1 = f"https://lookup.binlist.net/{bin}"
                    r1 = requests.get(url1)
                    coun1 = r1.json()["country"]["emoji"]
                    coun = r.json()["country"]["code"]
                    mf = types.InlineKeyboardMarkup(row_width=2)
                    c1 = types.InlineKeyboardButton("Bot Déveloper 👨‍💻",url="https://t.me/crackwon")
                    mf.add(c1)       
                    k +=1
                    w = str(k)
                    x = types.InlineKeyboardMarkup(row_width=2)
                    b = types.InlineKeyboardButton(f"Good ✅ : {w}",callback_data="F1")
                    x.add(b)
                    c = types.InlineKeyboardButton(f"Bad ⚠  : {g}️",callback_data="F2")
                    x.add(c)
                    bot.edit_message_text(chat_id=message.chat.id,message_id=id_msg,text="*Checking Bins ...*",parse_mode="markdown",reply_markup=x)
                    bot.send_message(message.chat.id,f"*New Bin ✅ \nBin : *`{bins}`*\nCountry : {coun} {coun1}*",reply_markup=mf,parse_mode="markdown")
                else:
                    g +=1
                    x = types.InlineKeyboardMarkup(row_width=2)
                    b = types.InlineKeyboardButton(f"Good ✅ : {w}",callback_data="F1")
                    x.add(b)
                    c = types.InlineKeyboardButton(f"Bad ⚠  : {g}️",callback_data="F2")
                    x.add(c)
                    bot.edit_message_text(chat_id=message.chat.id,message_id=id_msg,text="*Checking Bins ...*",parse_mode="markdown",reply_markup=x)
            except Exception as mf:
                g +=1
                x = types.InlineKeyboardMarkup(row_width=2)
                b = types.InlineKeyboardButton(f"Good ✅ : {w}",callback_data="F1")
                x.add(b)
                c = types.InlineKeyboardButton(f"Bad ⚠  : {g}️",callback_data="F2")
                x.add(c)
                bot.edit_message_text(chat_id=message.chat.id,message_id=id_msg,text="*Checking Bins ...*",parse_mode="markdown",reply_markup=x)
        else:
            mf = types.InlineKeyboardMarkup(row_width=2)
            c1 = types.InlineKeyboardButton("Bot Déveloper 👨‍💻",url="https://t.me/crackwon")
            mf.add(c1)      
            bot.send_message(message.chat.id,"*Check Finished !*",parse_mode="markdown",reply_markup=mf)    
            
	
bot.polling()