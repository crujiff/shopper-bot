import requests
import json
import configparser as cfg

class telegram_chatbot():
  def __init__(self, config):
    self.token = self.read_token_from_config_file(config) #get the token id from config file
    self.base = "https://api.telegram.org/bot{}/".format(self.token) #this would be the starting https url

  def get_updates(self, offset=None):
    url = self.base + "getUpdates?timeout=100" 
    if offset:
      url= url + "&offset={}".format(offset+1) 
    r = requests.get(url) #i retrieve the message
    return json.loads(r.content)

  def send_message (self, msg, chat_id):
    url= self.base + "sendMessage?chat_id={}&text={}".format(chat_id,msg) #i prepere the message to send
    if msg is not None:
      requests.get(url)

  def read_token_from_config_file(self, config):
    parser = cfg.ConfigParser()
    parser.read(config)
    return parser.get('creds','token')

  def send_image(self, attachment, chat_id):
    files={'photo': open(attachment, 'rb')} #multipart/form-data
    url= self.base + "sendPhoto?chat_id={}".format(chat_id) #send images
    if attachment is not None:
      print(requests.get(url,files=files))
