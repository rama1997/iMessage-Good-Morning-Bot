# iMessage-Good-Morning-Bot
Bot that sends customizable good morning message through iMessage every morning.

Example message using default messages:

<img src="https://i.imgur.com/EDDUyPo.png" width="405" height="486" />

# Features
- Customizable good morning greeting
- Additional content included with each message:
	- Dog Picture - Gets a random dog pic from a selection of various dog subreddits
	- Rain Alert - Gets daily forecast of desired city and sends a rain alert message if it is expected to rain 
	- National Holiday Alert - Gets a national holiday on the current day and sends a custom message
	- Motivation Quote - Sends a random motivation quote

# Requirements 
- MacOS 
- Apple ID

# Setup
- Add required API key to `config.py` in order to use the additional content.
- Message customization can be done in `config.py`, where you can edit: 
	- Good morning greeting 
	- Rain alert message 
	- Subreddits to use as source for dog picture 
	- Path to Applescript
- Create your own profile python file in the `profiles` folder. Example profile provided in the folder. Each profile requires:
	- Name - User will be referred to as the provided name
	- Phone number - custom messages will be sent to the provided phone number
	- City - rain alert feature will search the forecast of the provided city
- Motivational quotes can be edited in `quotes.txt`

# Usage 
- Install dependencies: `pip install -r requirments.txt`
- Args:
	- `-n --name`: name of profile to use 
- Run: `python main.py -n name`
- Use crontab to schedule program to run every morning at desired time. 

# Dog Picture
- Uses Reddit API to search various dog related subreddits and randomly gets a recent popular dog picture from listed subreddits. 
- To use the Reddit API, requires your own reddit account and reddit API key.
- Only returns posts that contain a single picture since I found it easier and faster to view on iMessage. 
- Can edit list of subreddits or add more subreddits in `config.py`. 

Following subreddit used as sources for the dog picture:
- [corgi](https://www.reddit.com/r/corgi/) 
- [dogpictures](https://www.reddit.com/r/dogpictures/)
- [puppies](https://www.reddit.com/r/puppies/)
- [shiba](https://www.reddit.com/r/shiba) 
- [puppysmiles](https://www.reddit.com/r/puppysmiles)
- [lookatmydog](https://www.reddit.com/r/lookatmydog)
- [rarepuppers](https://www.reddit.com/r/rarepuppers) 


# Rain Alert
Uses the OpenWeather API to get daily forecast of a desired city and sends a custom rain alert message if it is expected to rain in the day.

Requires OpenWeather API Key.

# National Holiday Alert
Web scrapes https://nationaltoday.com to get the most popular daily "national" holiday and sends a customizable holiday alert message. Most of the holidays are going to end up being more fun holidays, for examples, National Unicorn Day.
