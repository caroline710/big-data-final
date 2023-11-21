import asyncio
import csv
from twscrape import API, gather
from twscrape.logger import set_log_level

async def main():
    api = API()
    
    q = "Greta Thunberg since:2019-01-01 until:2019-12-31"

    with open('tweets-2019.csv', mode='w', newline='', encoding='utf-8') as file:

        writer = csv.writer(file)
        writer.writerow(['Tweet ID', 'Username', 'Content', 'Created At', 'User Location'])

        async for tweet in api.search(q, limit=5000):
            #location = tweet.location if tweet.location else 'Unknown'
            user_profile = await api.user_by_id(tweet.user.id)

            user_location = user_profile.location if user_profile.location else 'Unknown'

            print(tweet.id, tweet.user.username, tweet.rawContent, tweet.date, user_location)

            writer.writerow([tweet.id, tweet.user.username, tweet.rawContent, tweet.date, user_location])

if __name__ == "__main__":
    asyncio.run(main())