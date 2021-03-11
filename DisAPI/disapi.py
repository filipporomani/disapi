import requests
from datetime import date


headers = {}
embedsjson = {}

class bot(object):
   def __init__(self, token):
      self.token = token
      global headers
      headers = {
            "Authorization": f"Bot {token}"

      }
   def regionids(self):
      global headers
      url = f"https://discord.com/api/v8/voice/regions"
      ids = requests.get(url=url, headers=headers).text
      return ids
      
   def test(self, channelid):
      global headers
      url = f"https://discord.com/api/v8/channels/{channelid}/messages"
      r = requests.post(url=url, headers=headers)
      if str(r) == '<Response [400]>':
         r1 = '<Response [200]>'
      else:
         r1 = r
      print(r1)
      return r1
   class channel():
      def get(self, channelid):
         global headers
         url = f'https://discord.com/api/v8/channels/{channelid}'
         return requests.get(url=url, headers=headers).text
   class guild():
      def set(self, guildid, dictionary):
         global headers
         url = f'https://discord.com/api/v8/guilds/{guildid}'
         json = dictionary
         return requests.patch(url=url, headers=headers, json=json).text
      class member():
         def set(self, guildid, memberid, dictionary):
            global headers
            url = f'https://discord.com/api/v8/guilds/{guildid}/members/{memberid}'
            json = dictionary
            return requests.patch(url=url, headers=headers, json=json).text
      def get(self, guildid):
         global headers
         url = f'https://discord.com/api/v8/guilds/{guildid}'
         return requests.get(url=url, headers=headers).text
   class message():
      def send(self, body: str = None, channelid: int = None, tts: bool = None):
         global headers
         if tts is None:
            tts = False
         url = f"https://discord.com/api/v8/channels/{channelid}/messages"
         json = {
            "content": str(body),
            "tts": tts,
         }
 
         return requests.post(url=url, headers=headers, json=json)
         
   class embed():  
      def new(self, name: str = None, title: str = None, body: str = None, footer: str = None):
         global embedsjson
         today = date.today()
         def get_last_digits(num, last_digits_count=2):
            return int(str(num)[-last_digits_count:])
         
         dtg = today.strftime('%Y')
         dp = get_last_digits(dtg)
         d1 = today.strftime(f"{dp}.%d%m")
         embedjson = {
            "content": None,
            "tts": False,
            "embed": {
                  "title": str(title),
                  "description": body,
                  "type": "rich",
                  "footer": {
                     "text": footer
                  },
                  "provider": {
                     "name": f"newapi {d1}"
                  }
            }
         }
         
         embedsjson[name] = embedjson

      def send(self, name, channelid):
         global embedsjson
         url = f"https://discord.com/api/v8/channels/{channelid}/messages"
         try:
            return requests.post(url=url, headers=headers, json=embedsjson[name])
         except KeyError:
            raise KeyError('Bad embed name. Embed could be undefined or not created yet.')