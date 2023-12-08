# big-data-final

## Task Outline
### 
1. Intro/Motivation: Why are you doing what you’re doing, what is your research question?
2. Data: How/where did you get your data? Explanation of the data (features), potentially accompanied by visualisations
3. Method: What kind of tools for data analysis are you using? How does it work? Potentially accompanied by code snippets
4. Results: What did you find out? Any cool insights? Accompanied by plots, visualizing your insights.
5. Conclusion: What worked, what didn’t? What would you do if you had to improve the project?

## Final Report and Specifications
###

**Intro/Motivation:**
Greta Thunberg’s activism has played a leading role in the global discourse of climate change. Since her first solitary school strike in August 2018, Thunberg has managed to galvanize millions and influence people who had not previously been interested in her agenda. This “Greta Thunberg Effect” has contributed to a surge in climate change conversations on social media and drawn in a diverse array of voices, especially on Twitter.

Motivated by this significant shift, we wanted to examine climate change related tweets during the height of Thunberg’s influence (2018-2020) and interpret the impact of her activism on public sentiment. What shifts in sentiment can be observed in climate change discourse during this period and how do these shifts correlate with key moments in Thunberg’s activism?

In this project, we scraped approximately 100,000 tweets from both the United States and European Union and analyzed sentiment separately to understand the nuances of public opinion in two different geopolitical regions.


**Scraping our Data:** 

For our data we used TWScrape to scrape search results; we used it to acquire Tweets with the keyword 'climate change' across 2018, 2019, and 2020. Twscrape is a python library created in May 2023, and it utilizes Twitter's API to interact with their platform and retrieve the desired data. We had to create a Twitter account to get valid API credentials. We managed to achieve the following-

1. We managed to scrape 500-800 tweets for 10 randomly selected days/months between 2018-2020.
2. Our search query was "climate change". We debated using other key words like "Greta Thunberg" since it would result in tweets related to her political image and would affect the focus of our sentiment analysis away from climate change. We also realize that this limited our tweets from other languages and countries in the EU where English is not very widespread.

**Method:**
*VADER* (Vibha)

*Climate analysis model* (Caroline)

*Data vizualization* (Maryam)

**Results:** (All)

**Conclusion:** (Maryam) 

