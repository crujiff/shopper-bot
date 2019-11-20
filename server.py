from bot import telegram_chatbot
from datetime import datetime
import pytz

bot=telegram_chatbot("config.cfg")
update_id = None
admin_users = []
queue=None
news=None
last_update=None
update_time=["0","15","30","45","60"]
utc = pytz.timezone("UTC")
italy = pytz.timezone("Europe/Rome")



#defining function user_reply and admin_user_reply

def user_reply(name,message):
        if message=="/queue":
                if coda is not None:
                        reply = "Hello , actually you've to wait " + str(queue) + " minutes. Last update time:" + last_update
                else:
                        reply= "Hello, actually there aren't queue information"
        elif message=="/news":
                if news is not None:
                        reply = "Hello, actually there are this news: " + (news)
                else:
                        reply = "Hello, actually there aren't any news"
        else:
                reply="Incorrect command"
        return reply

def admin_user_reply(name,message):
        if message in update_time:
                global coda
                global last_update
                coda=int(message)
                reply = "Hello, queue information updated"
                last_update=datetime.now().astimezone(italy).strftime("%H:%M %d/%m/%Y")
        else:
                reply = user_reply(name,message)
        return reply

while True:
        updates= bot.get_updates(offset=update_id)
        updates = updates["result"] 
        if updates:
                for item in updates:
                        update_id = item ["update_id"] 
                        try:
                                message = item["message"]["text"]
                        except:
                                message = None
                        from_ = item["message"]["from"]["id"]
                        fname=item["message"]["from"]["first_name"]
                        if from_ in admin_users:
                                reply= admin_user_reply(fname,message)
                        else:
                                reply = user_reply(fname,message)
                        bot.send_message(reply,from_)
