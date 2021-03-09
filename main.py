import disapi

api = disapi.bot('NzgyOTQ4MTU2ODIzOTYxNjEw.X8TnSw.AJ1zBaF_tckJDfiRqSo8RL9rolQ')
embed = api.embed()
message = api.message()



# embed.new("newembed", "Filippo Romani", "This is my own Discord API Python-based module!", "I'm just building it!")


# print(embed.send("newembed", 802141032992604190))

# print(message.send("Hello, testing DisAPI 21.0309", 802141032992604190))

api.test(802141032992604190)