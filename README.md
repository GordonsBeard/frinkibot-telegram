# frinkibot-telegram
A Frinkiac/Morbotron bot for Telegram.

**Usage**

`/simp` - Random screenshot

![Random screenshot](http://i.imgur.com/4N0RX8U.png)

`/simp search terms` - Searches for a screenshot using "search terms"

![Search with no quotations](http://i.imgur.com/LiW4Rwt.png)

`/simp "search terms"` - Searches for a screenshot AND captions the image using "search terms"

![Search with qutoations](http://i.imgur.com/9dyBcha.png)

*You can use /fut instead of /simp to get Futurama screenshots in the same way*

**Requires**

- The stuff in [requirements.txt](requirements.txt) and [frinkiac.py](https://github.com/GordonsBeard/frinkiac.py)
- A `config.py`  file that contains:

```bot_token = 'YOUR_BOT_TOKEN'```