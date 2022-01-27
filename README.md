# Reddit Bot
This is a small script Bot that will respond to certain comments in exact subreddit
## Requirements
1. Python (https://www.python.org/downloads/)
2. Praw (https://praw.readthedocs.io/en/stable/getting_started/installation.html)
## How to setup Bot?
1. Go to https://www.reddit.com/prefs/apps/
2. Click *are you a developer? create an app...*
3. *Name, description and about url* can be any
4. **Type** should be Script
5. **Redirect uri** should be *http://localhost*
6. Click **Create app**
7. Go to *reddit_bot.py* and you should change client_id, client_secret - outputted values from point 6.
Username and password of yours Reddit account.
8. In line 20 of *reddit_bot.py* instead of **word** insert a phrase that the bot will search for among various comments:
```python
if 'word' in comment_lower:
```
9. In line 23 type the phrase that Bot should answer to found comment:
```python
comment.reply('An example of how a bot should respond.')
```
## Usage
Navigate to your project directory.
Type to cmd: 
```sh
$ python reddit_bot.py name_of_subreddit
```
## Example:
```python
if 'cute' in comment_lower:
```
```python
comment.reply("Thats the cuttest think I've ever seen too!")
```
```sh
$ python reddit_bot.py cats
```
# Result
After setup you'll have ready small Bot that can answer to the comments in subreddits. It takes every 11 minutes to wait because if we wont Reddit will get mad about this :(
