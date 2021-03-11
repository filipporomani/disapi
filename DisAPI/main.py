import disapi, os, time, requests
from dotenv import load_dotenv
load_dotenv()
api = disapi.bot(os.environ.get('TOKEN'))
embed = api.embed()
message = api.message()
guild = api.guild()
member = guild.member()
