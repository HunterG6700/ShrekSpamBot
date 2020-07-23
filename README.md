I did not create this bot all credit goes to **Matt Upham**. I just edited it to make it sync up to the shrek theme song and made it send sms messages using Twilio.
This repo goes along with [this YouTube video](https://youtu.be/wEkkZBY2Ja4). Copy and paste song lyrics, movie scripts, etc into the lyrics file. Add your friend's phone number to the num file, run, and watch as it sends texts one by one, for every word!



## Features / Specifications

- works with the iMessage client on Mac (feel free to substitute an SMS API)
- add any text to lyrics.txt

<br>

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Instructions
1. Download the song with marker data  [Here](https://mega.nz/file/M7hhXYZQ#JccvLYpBFHZnP1X945GXkO-M4_x8gAv4UqkmSsCZ0AI)
2. Watch this [Youtube Video](https://youtu.be/wEkkZBY2Ja4) first!
3. Add a phone number (as a string) to `num.py`
4.  Create an account at https://www.twilio.com/
5.Add your ACCOUNT SID to ACCOUNT SID in send.py
6. Add your AUTH TOKEN in send.py
7. Run the `send.py` file with Python
6. Improve this repo, and DM me on [Discord](https://discord.gg/9RGdMcF), [TikTok](https://www.tiktok.com/@mattupham), or [Instagram](https://instagram.com/mattupham), and I'll feature you in a future video!

<br>

### Prerequisites

Install [Python3](https://www.python.org/downloads/)

Install [Pip and virtualenv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments)

Install [Pipenv](https://pypi.org/project/pipenv/)

<br>

### Installing

In the project directory:

**Create virtual environment:**

On macOS and Linux:

```
python3 -m venv env
```

On Windows:

```
py -m venv env
```

**Activate virtual environment:**

On macOS and Linux:

```
source env/bin/activate
```

On Windows:

```
.\env\Scripts\activate
```

Install packages via Pipfile

```
pipenv install
```

<br>

## Built With

- [Python3](https://www.python.org/downloads/) - A programming language that lets you work more quickly and integrate your systems more effectively.
- [py-iMessage](https://pypi.org/project/py-iMessage/) - A library to send iMessages from your Mac computer (it does not work on Windows/Linux)

<br>

## Author

**Matt Upham**

- **YouTube** - [@mattupham](https://www.youtube.com/mattupham?sub_confirmation=1)
- **TikTok** - [@mattupham](https://www.tiktok.com/@mattupham)
- **Instagram** - [@mattupham](https://instagram.com/mattupham)
- **Github** - [@mattupham](https://github.com/mattupham)
- **Discord** - [community](https://discord.gg/9RGdMcF)
