# stock-sentiment-analysis

This project is an attempt at performing a simple periodic sentiment analysis of given stock symbol on reddit.

<div style="text-align:center"><img src="docs/img/web_interface_mockup.png"/></div>

## Requirements

- FastAPI

## Project architecture

A scheme of the whole project architecture can be found at on [figma](https://www.figma.com/file/hohoKkCm2DAsNAORkCqbGg/Untitled?node-id=0%3A1)

In short, the main process are:
- Every 4 hours, a script scrape the latest posts and comments associated with a stock
- The script send the data to a sentiment analysis API that analysis the text
- The sentiment analysis API send the data to store it in a NoSQL database
- A static web interface that fetch the data through the FastAPI DB 


## Data processing

### The reddit API

The reddit posts are fetched from the API with the format `http://www.reddit.com/r/{subreddit}/new.json?`

Other useful options that can be used in the queries are:
- `limit={limit_number}` (note that the upper limit is 100)
- `sort={sorting_option}`


## Additional ressources

In the building of the project, the following ressources are providing usefull informations:
- [Deploy a ML model with FastAPI](https://blockgeni.com/guide-to-fastapi-with-machine-learning-deployment/) guide
- [Deploy FastAPI as a Vercel serverless application](https://github.com/paul121/fastapi-zeit-now)
- [Sentiment analysis with python](https://medium.com/swlh/sentiment-analysis-using-python-and-nltk-library-d68caba27e1d)
- [Use FastAPI with MongoDB](https://medium.com/python-in-plain-english/how-to-use-fastapi-with-mongodb-75b43c8e541d)
- [Create A Reddit app](https://www.reddit.com/prefs/apps)
- [How to scrape reddit with python](https://www.storybench.org/how-to-scrape-reddit-with-python/)
