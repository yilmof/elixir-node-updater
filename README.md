# Elixir-v3 Node Updater

Automatically updates Elixir-v3 testnet node when a new version is released in the [#validator-announcements](https://discord.com/channels/1059691738349977674/1262863354528272477) channel in the [Elixir Discord](https://discord.gg/elixirnetwork).

## Setup
Follow the [#validator-announcements](https://discord.com/channels/1059691738349977674/1262863354528272477) channel and connect it to a channel in your own Discord server. If you don't know how to do this, [Discord has a tutorial](https://support.discord.com/hc/en-us/articles/360028384531-Channel-Following-FAQ). Turn on developer mode (User Settings -> Advanced -> Developer mode) and right click and copy the channel ID of the channel you connected the announcements to.

If you aren't running an Elixir node yet, [first set it up](https://docs.elixir.xyz/running-an-elixir-validator).

Then, create a Discord bot and copy the bot token [(Guide)](https://discordpy.readthedocs.io/en/stable/discord.html).

## Installation

```bash
git clone https://github.com/yilmof/elixir-node-updater.git
cd elixir-node-updater
pip install -r requirements.txt
mv .env.example .env
```
Paste your Discord bot token and the channel ID in the `.env` file.

Get the path of `validator.env` (Use `pwd` command) and replace `/home/user/elixir/validator.env` in the following command and run it while in the elixir-node-updater folder:
```bash
sed -i 's|/path/to/validator.env|/home/user/elixir/validator.env|' update_elixir.sh
```
Run the bot to test it:
```
python3 updater_bot.py
```
If you something like `Bot has logged in as` with your bot's name and don't see errors, ctrl + c out of it.



## Usage
You can use screen or any other way you like to run the bot in the background but I like using PM2.

First install [NodeJS](https://www.digitalocean.com/community/tutorials/how-to-install-node-js-on-ubuntu-20-04), then install [PM2](https://pm2.io/docs/runtime/guide/installation/).

```
cd elixir-node-updater
pm2 start updater_bot.py
```

After an update, the bot will send a message in the channel if it was succesful or any errors if it failed.
### Logs
To check logs, `cat bot.log` or with PM2 `pm2 logs`
