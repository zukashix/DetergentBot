# DetergentBot

This bot is a personal bot for my friend Lunoirex. The bot cannot be invited by other users but it has been made open source so you can use the code as you want to.
This branch has been configured to host the bot on heroku

## Running the bot

##### You must be using a version of python above 3.5.x (I used python 3.8.9)

Fork this repo using git and modify it as you want <br />

Change the `runtime.txt` file to the version of python you want to use (python 3.8.9 is recommended) <br />

Create a new python app on `dashboard.heroku.com` <br />

Setup the config vars on heroku, the ones you'll need to configure are present in `DetergentBot/keys.json` <br />

Connect to github on your app's deploy page and turn on your dynos, then finally deploy! <br />

## Credits

The bot uses [this](https://github.com/ZipBomb/spotify-song-suggestion/) repository's code to find random songs on spotify for the GuessTheMusic game. <br />
Big thanks to [Pablo Rey](https://github.com/ZipBomb/) for making this available!
