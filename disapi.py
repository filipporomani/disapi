import requests
headers = {}
embedsjson = {}

class bot(object):
   def __init__(self, token):
      self.token = token
      global headers
      headers = {
            "Authorization": f"Bot {token}"

      }
   def test(self, channelid):
      global headers
      url = f"https://discord.com/api/v8/channels/{channelid}/messages"
      r = requests.post(url=url, headers=headers)
      print(r)
      return r
   class message():
      def send(self, body, channelid, tts: bool = None):
         global headers
         if tts is None:
            tts = False
         url = f"https://discord.com/api/v8/channels/{channelid}/messages"
         json = {
            "content": str(body),
            "tts": tts,
         }
         r = requests.post(url=url, headers=headers, json=json)
         return r
         
   class embed():  
      def new(self, name, title, body, footer):
         global embedsjson
         
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
                     "name": "newapi r. 21.0803"
                  }
            }
         }
         embedsjson[name] = embedjson

      def send(self, name, channelid):
         global embedsjson
         url = f"https://discord.com/api/v8/channels/{channelid}/messages"
         try:
            r = requests.post(url=url, headers=headers, json=embedsjson[name])
            return r
         except KeyError:
            raise KeyError('Bad embed name. Embed could be undefined or not created yet.')