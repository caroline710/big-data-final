import asyncio
import csv
import random
import datetime
from twscrape import API, gather
from twscrape.logger import set_log_level

async def main():
    api = API()
    year = '2020'
    months = range (1, 13)

    for month in months:
        days = random.sample(range(1,30), 10) # select 10 random days

        for day in days:
            start_date = datetime.date(int(year), month, day)
            end_date = start_date + datetime.timedelta(days=1) # next day
            q = f"Greta Thunberg OR climate change since:{start_date} until:{end_date}"
            # print(f"Querying: {q}")

            with open('tweets-2020-again.csv', mode='a', newline='', encoding='utf-8') as file:

                writer = csv.writer(file)
                if file.tell() == 0:
                    writer.writerow(['Tweet ID', 'Username', 'Content', 'Created At', 'User Location'])

                tweet_count = 0
                async for tweet in api.search(q, limit=1000): # sets limit to 1000 tweets per day
                    user_profile = await api.user_by_id(tweet.user.id)

                    user_location = user_profile.location

                    if user_location is not None and user_location != "": 

                        print(tweet.id, tweet.user.username, tweet.rawContent, tweet.date, user_location)

                        writer.writerow([tweet.id, tweet.user.username, tweet.rawContent, tweet.date, user_location])

                        tweet_count+=1
                        if tweet_count >= 1000:
                            break
                
                print(f"Number of tweets collected for {start_date}: {tweet_count}")

if __name__ == "__main__":
    asyncio.run(main())