DisAPI - Python-Based Discord API module
========================================

Quickstart
----------

-  `Import module <#importing>`__

-  `Messages <#messages>`__
-  `Send message <#send-message>`__

-  `Embeds <#embeds>`__
-  `Create embed <#create-embed>`__
-  `Send embed <#send-embed>`__

-  `API connection <#api-connection>`__
-  `Test connection <#test-connection>`__

Importing
=========

To import the module download the source, create a file and type
``import disapi`` inside of it.

To create a new bot instance use the ``bot()`` feature:

.. code:: py

    # This is how a DisAPI file should look like
    import disapi
    bot = disapi.bot('YOUR_BOT_TOKEN')

Messages
========

Send message
------------

To send a message you can use the ``message().send()`` method:

.. code:: py

    import disapi
    bot = disapi.bot('YOUR_BOT_TOKEN')
    message = bot.message()

    message.send("MESSAGE_BODY", CHANNEL_ID, TTS) # CHANNEL_ID is an integer and TTS is an optional boolean

Embeds
======

Create embed
------------

To create an embeded message you can use the built-in ``embed()``
feature.

.. code:: py

    import disapi
    bot = disapi.bot('YOUR_BOT_TOKEN')
    embed = bot.embed()

    embed.new("EMBED_NAME", "EMBED_TITLE", "EMBED_BODY", "EMBED_FOOTER")

The ``embed().new()`` feature create an array and put the embed data in.
You cannot send an embed before creating it.

Send embed
----------

To send an embed you can use the ``embed().send()`` method:

.. code:: py

    import disapi
    bot = disapi.bot('YOUR_BOT_TOKEN')
    embed = bot.embed()

    embed.new("EMBED_NAME", "EMBED_TITLE", "EMBED_BODY", "EMBED_FOOTER")
    embed.send("EMBED_NAME", CHANNEL_ID) # CHANNEL_ID is an integer

API connection
==============

To see the status code of your request to the Discord API, you can
insert your action into a ``print()`` statement:

.. code:: py

    import disapi
    bot = disapi.bot('YOUR_BOT_TOKEN')
    embed = bot.embed()

    embed.new("EMBED_NAME", "EMBED_TITLE", "EMBED_BODY", "EMBED_FOOTER")
    print(embed.send("EMBED_NAME", CHANNEL_ID)) # CHANNEL_ID is an integer

to get the status code back in this format: ``<Response [CODE]>`` (CODE
is the request code - 200 is success)

Test connection
---------------

To test the status code of the API using a certain channel ID just use
the ``test()`` function:

.. code:: py

    import disapi
    bot = disapi.bot('YOUR_BOT_TOKEN')

    bot.test(CHANNEL_ID) # CHANNEL_ID is an integer

The upper code will just make a test call to the API and print the
status code of the request in the console.
