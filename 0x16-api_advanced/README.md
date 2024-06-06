0x16. API advanced
Python
Scripting
Back-end
API

Background Context
Questions involving APIs are common for interviews. Sometimes they’re as simple as ‘write a Python script that queries a given endpoint’, sometimes they require you to use recursive functions and format/sort the results.

A great API to use for some practice is the Reddit API. There’s a lot of endpoints available, many that don’t require any form of authentication, and there’s tons of information to be parsed out and presented. Getting comfortable with API calls now can save you some face during technical interviews and even outside of the job market, you might find personal use cases to make your life a little bit easier.

How to read API documentation to find the endpoints you’re looking for
How to use an API with pagination
How to parse JSON results from an API
How to make a recursive API call
How to sort a dictionary by value

# Reddit API Subscriber Count

This project contains a Python script that queries the Reddit API to return the number of subscribers for a given subreddit. If an invalid subreddit is provided, the script returns 0.

## Files

- `0-subs.py`: Contains the `number_of_subscribers` function.
- `0-main.py`: Script to test the `number_of_subscribers` function.
- `README.md`: Project documentation.

## Requirements

- Python 3.4.3 or higher
- Requests module

## Usage

Make sure all files are executable. Run the `0-main.py` script and pass the name of the subreddit as an argument:

```sh
$ python3 0-main.py programming
756024

$ python3 0-main.py this_is_a_fake_subreddit
0

