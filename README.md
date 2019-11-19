# shopper-bot
A telegram bot for your shop, if you want to include queue information and news
The python prerequisites are:
- `pip install requests`
- `pip install json`
- `pip install configparser`
- `pip install datetime`
- `pip install pytz`

# How to use the bot
For using the bot, you have to edit the file config.cfg inserting the token of your bot
Then, you've to modify your UTC, in my example is Italy.
After this, you've to choose which user can manipulate information in the list "admin_users"
Finally, your admin can update queue information and news information and you customers can query queue information and news
After that you made this modification, you can run the script
- `python3 server.py`
