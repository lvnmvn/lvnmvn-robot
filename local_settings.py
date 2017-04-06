'''
Local Settings for a heroku_ebooks account. #fill in the name of the account you're tweeting from here.
'''

#configuration
MY_CONSUMER_KEY = '4XOuCAYrikyijOam1LIJtdocf'
MY_CONSUMER_SECRET = 'qdISunrKmTNQewXrnoGq8IEId17Ee7T2nlMtGJkkQKlKeRKUAb'
MY_ACCESS_TOKEN_KEY = '769250294349914113-lx4kf4J9MtGGg1BrNyowCdyhsraptSL'
MY_ACCESS_TOKEN_SECRET = 'jcXtAQkO396tqmzFM6NwRxhK0b6onzXdC5z0iDhN8uvjf'

SOURCE_ACCOUNTS = ["ChomskyQuuotes”, ”AlanWattsDaily”, “TaoEssentials”, “lalisagoldrope”, “lbtmst93”, “shamanabots”] #A list of comma-separated, quote-enclosed Twitter handles of account that you'll generate tweets based on. It should look like ["account1", "account2"]. If you want just one account, no comma needed.
ODDS = 2 #How often do you want this to run? 1/8 times?
ORDER = 3 #how closely do you want this to hew to sensical? 1 is low and 3 is high.
DEBUG = True #Set this to False to start Tweeting live
STATIC_TEST = False #Set this to True if you want to test Markov generation from a static file instead of the API.
TEST_SOURCE = ".txt" #The name of a text file of a string-ified list for testing. To avoid unnecessarily hitting Twitter API. You can use the included testcorpus.txt, if needed.
TWEET_ACCOUNT = “lvnmvn” #The name of the account you're tweeting to.

