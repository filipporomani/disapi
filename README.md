# DisAPI - Python-Based Discord API module

## Quickstart

  - [Import module](#importing)
- [Guilds](#guilds)
  - [Get guild](#get-guild)
  - [Channels](#channels)
    - [Get channel](#get-channel)

- [Messages](#messages)
  - [Send message](#send-message)

- [Embeds](#embeds)
  - [Create embed](#create-embed)
  - [Send embed](#send-embed)

- [API connection](#api-connection)
  - [Test connection](#test-connection)
     
<br><br>

# Importing

To import the module download the source, create a file and type `import disapi` inside of it.

To create a new bot instance use the `bot()` feature:
```py
# This is how a DisAPI file should look like
import disapi
bot = disapi.bot('YOUR_BOT_TOKEN')
```

<br><br><br>

# Guilds
### Get guild
The `guild().get()` method allows you to get detailed info about a guild. This method returns a dictionary object. The following code:
```py
import disapi
api = disapi.bot('YOUR_BOT_TOKEN')
channel = api.guild()

cha = channel.get(GUILD_ID) # GUILD_ID is an integer
print(cha)
```
will return a dictionary with all the information about the given guild id.
You can only get info about guilds where your bot is in.
<br><br>

## Guild channels
### Get channel
The `channel().get()` method allows you to get detailed info about a channel. This method returns a dictionary object. The following code:
```py
import disapi
api = disapi.bot('YOUR_BOT_TOKEN')
channel = api.channel()

cha = channel.get(CHANNEL_ID) # CHANNEL_ID is an integer
print(cha)
```
will return a dictionary with all the information about the given channel id.
You can only get info about channels where your bot is in.
<br><br><br>


# Messages
### Send message
To send a message you can use the `message().send()` method:
```py
import disapi
bot = disapi.bot('YOUR_BOT_TOKEN')
message = bot.message()

message.send("MESSAGE_BODY", CHANNEL_ID, TTS) # CHANNEL_ID is an integer and TTS is an optional boolean
```


<br><br><br>

# Embeds

### Create embed

To create an embeded message you can use the built-in `embed()` feature.

```py
import disapi
bot = disapi.bot('YOUR_BOT_TOKEN')
embed = bot.embed()

embed.new("EMBED_NAME", "EMBED_TITLE", "EMBED_BODY", "EMBED_FOOTER")
```

The `embed().new()` feature create an array and put the embed data in. You cannot send an embed before creating it.
<br><br>

### Send embed
To send an embed you can use the `embed().send()`  method:
```py
import disapi
bot = disapi.bot('YOUR_BOT_TOKEN')
embed = bot.embed()

embed.new("EMBED_NAME", "EMBED_TITLE", "EMBED_BODY", "EMBED_FOOTER")
embed.send("EMBED_NAME", CHANNEL_ID) # CHANNEL_ID is an integer
```
<br><br><br>

# API connection
To see the status code of your request to the Discord API, you can insert your action into a `print()` statement:

```py
import disapi
bot = disapi.bot('YOUR_BOT_TOKEN')
embed = bot.embed()

embed.new("EMBED_NAME", "EMBED_TITLE", "EMBED_BODY", "EMBED_FOOTER")
print(embed.send("EMBED_NAME", CHANNEL_ID)) # CHANNEL_ID is an integer
```
to get the status code back in this format:
`<Response [CODE]>` (CODE is the request code - 200 is success)
<br><br>

### Test connection
To test the status code of the API using a certain channel ID just use the `test()` function:

```py
import disapi
bot = disapi.bot('YOUR_BOT_TOKEN')

bot.test(CHANNEL_ID) # CHANNEL_ID is an integer
```
The upper code will just make a test call to the API and print the status code of the request in the console.