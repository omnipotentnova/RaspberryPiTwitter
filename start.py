# This script will pull a feed from Twitter from the users unblocked users.
# Blocking a user in Twitter will not pull their tweets.

from feedrenderer import *
from twitterrepository import *
from APIProperties import *


renderer = FeedRenderer(2, 5)

twitterRepository = TwitterRepository(consumerKey, consumerSecret, apiKey, apiSecret)

def Draw():
    tweets = twitterRepository.GetTweetsFromUnblockedUsers('#StartupInst OR from:StartupInst OR #LearnToDo OR @StartupInst OR to:StartupInst', 20)
    renderer.DrawFeed(tweets)
    renderer.root.after(100000, Draw)

Draw()
renderer.Draw()
