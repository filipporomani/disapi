import disapi, os, time
from dotenv import load_dotenv
load_dotenv()
api = disapi.bot(os.environ.get('TOKEN'))
embed = api.embed()
message = api.message()
channel = api.guild()



# embed.new("newembed", "Filippo Romani", "This is my own Discord API Python-based module!", "I'm just building it!")


# print(embed.send("newembed", 802141032992604190))
print(channel.get(776086052284268556))