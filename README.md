# iMessage-Good-Morning-Bot
A customizable automated bot that sends personalized morning messages through iMessage, featuring daily rain updates, NBA schedules, and more.

<img src="https://i.imgur.com/EDDUyPo.png" width="405" height="486" />

## Features
- **Personalized Morning Greeting**: Fully customizable good morning message
- **Dynamic Content**:
  - 🐕 **Dog Pictures**: Daily photos from popular dog-focused subreddits
  - 🌧️ **Rain Alerts**: Automatic rain notifications for your city
  - 🎉 **Holiday Updates**: Daily notable "national holiday" notifications
  - 💪 **Motivation Quotes**: Random inspirational messages
  - 🏀 **NBA Schedule**: Daily game schedules
- **Flexible Configuration**: Enable/disable any module
- **Profile System**: Support for multiple users with different preferences

## Feature Details

### 🐕 Dog Picture

- Sources images from popular dog subreddits including:
  - r/corgi
  - r/dogpictures
  - r/puppies
  - r/shiba
  - r/puppysmiles
  - r/lookatmydog
  - r/rarepuppers
- Filters for single-image posts
- Requires Reddit API credentials

### 🌧️ Rain Alert

- Powered by OpenWeather API
- Provides daily rain forecasts
- Customizable alert messages

### 🎉 Holiday Alert

- Scrapes nationaltoday.com
- Features popular daily "national" holidays
- Fun and lighthearted updates

### 🏀 NBA Schedule

- Uses Sportsdata.io API
- Displays daily game schedule, game time, and broadcast channels


# Getting Started

## Prerequisites
- MacOS device
- Active Apple ID
- Python 3.x

## Installation

1. Clone the repository:
```bash
git clone https://github.com/rama1997/iMessage-Good-Morning-Bot.git
cd iMessage-Good-Morning-Bot
```

2. Install dependencies (preferably in a virtual environment):
```bash
pip install -r requirements.txt
```

## Configuration

### API Setup

1. Add required API keys to `config.py`:
   - Reddit API credentials (for dog pictures)
   - OpenWeather API key (for weather alerts)
   - SportsData.IO API Key (for daily NBA game schedule)

### Message Customization

Edit `config.py` to:

- Customize message templates
- Add new message types
- Configure dog picture subreddit sources
- Set Applescript path

### User Profiles

1. Create a new profile in the `profiles` folder (see example profile)
2. Required profile settings:
   - Name: User's preferred name
   - Phone number: Target iMessage number
   - City: Location for weather alerts
   - Feature toggles: Enable/disable specific features

### Quotes

Edit `quotes.txt` to customize the motivation quote collection

## Usage

Run the bot for a specific profile:

```bash
python main.py -n profile_name
```

For automated daily messages, set up a crontab schedule.

## Roadmap

- [ ] Traffic and commute time alerts
- [ ] Additional weather alert types
- [ ] More customization options

## Contributing

Contributions are welcome! Feel free to submit issues and pull requests.
