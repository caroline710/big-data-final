# big-data-final

## Task Outline
### 
1. Intro/Motivation: Why are you doing what you’re doing, what is your research question?
2. Data: How/where did you get your data? Explanation of the data (features), potentially accompanied by visualisations
3. Method: What kind of tools for data analysis are you using? How does it work? Potentially accompanied by code snippets
4. Results: What did you find out? Any cool insights? Accompanied by plots, visualizing your insights.
5. Conclusion: What worked, what didn’t? What would you do if you had to improve the project?

## Final Report and Specifications

### A Sentiment Analysis of Climate Change Tweets: EU vs US
In recent years, the conversation about climate change has heated up, with discussions about our planet’s future intensifying. The increasingly visible impact of extreme weather events and activism from figures like Greta Thunberg have played a leading role in mobilizing global communities.

Motivated by this apparent shift in public discourse, we wanted to examine climate change related tweets during the height of Thunberg’s influence between 2018-2020. What changes in sentiment can be observed in climate change discourse during this period and how does this vary among and between the EU and U.S?

In this project, we scraped approximately 110,000 tweets from both the EU and US and analyzed sentiment separately to understand the nuances of public opinion in these two different geopolitical regions. 

**Getting the Tweets** 

For our data we used TWScrape to scrape search results; we used it to acquire Tweets with the keyword 'climate change' across 2018, 2019, and 2020. Twscrape is a python library created in May 2023, and it utilizes Twitter's API to interact with their platform and retrieve the desired data. We had to create a Twitter account to get valid API credentials. We managed to achieve the following-

1. We managed to scrape 500-800 tweets for 10 randomly selected days/months between 2018-2020.
2. Our search query was "climate change". We debated using other key words like "Greta Thunberg" since it would result in tweets related to her political image and would affect the focus of our sentiment analysis away from climate change. We also realize that this limited our tweets from other languages and countries in the EU where English is not very widespread.
3. We noticed that the data was extremely strated 
   
**Data Wrangling**

We had to do a considerable amount of data wrangling for our project, especially with regards to the user location, which we would later use for geoplotting. Since we could not access the geolocation of the tweets from Twitter API without payment, it was importance to standardize the self-reported user location and remove spam locations like "Purgatory". We also had to organize the tweets by states for the US and by country for the EU for the visualizations of nation-based sentiment.

After gathering the tweet data, we performed an initial exploratory analysis to examine the distribution of tweets across U.S. states and EU countries.

![Number of Tweets per US State](graphs/us-num-tweets.png)
![Number of Tweets per US State](graphs/eu-num-tweets.png)

These barplots highlight the regional differences of Twitter usage between the U.S. and EU. This is likely attributed to the much higher Twitter user base in the U.S, leading to more contribution to discussions on topics like climate change.

**Time for Sentiment Analysis**

After our initial exploratory analysis, our data was ready to be run through a sentiment analysis model. We used [this](https://huggingface.co/XerOpred/twitter-climate-sentiment-model) Hugging Face model, a fine-tuned version of DistilBERT that has been tailored to evaluate sentiment within tweets related to climate change. DistilBERT is a streamlined version of the BERT model, designed to capture contextual understanding in a compact form which made it ideal for analyzing our large dataset of tweets.

**Wordclouds Analysis***

We generated 4 word clouds for positive and negative sentiments in US and EU to compare the top ten most common words in both regions.  We also chose to align the colorscheme for US and EU according to thier national colors/ thier flags for better understandability. For positive sentiments, the most common words in the US wordclouds  were "People", "Believe", "Make", "Fight", "real", "Need", "trump", "Science", "Time", "Now". In comparison, The top positive sentiment words from EU were "Climateaction", "Environment", "Energy", "Arctic", "Global", "Action", "World", "Time", "One" and "People". Just looking at the top words alone, we noticed that tweets on US were more hopeful and emotional regarding climate change, whereas Eu seemd to have an more action-oriented and related to practicality of the climtae crisis. We also noticed that the negative sentiments for the US were generally more passionate, with words like "hoax", "Global Warming", "money", "man-made", "believe", "Science", "year", "Now", "liberal" and "time left". EU was generally not that strong in negative sentiments and the words seemed pretty similar to the positive sentiment wordcloud- with additional words like "human", "lie" and "political" amongst others which could indicate that negative sentiments rose when politics and climate change were involved, although this was not a direct correlation. We also know from the geoplots that EU had generally a more unified distribution of sentiment, which could reflection the solidaity of the UN in climate policy and how unilateral climate targets shared by the EU might help in creating a more uniform sentiment distribution. Whereas just in the US, the sentiment variation was so much higher across the states, and the more "red" states were generally leaning towards negative sentiments, indicating just how integrated US politics are on a topic like climate change.

**A Geographic Perspective**

We then plotted the geographic distribution of average sentiment to show the variation in sentiment intensity across the states and EU. A higher average sentiment (lighter color) indicates a more positive sentiment.

![US Chloropleth](graphs/us-geoplot.png)
![EU Chloropleth](graphs/eu-geoplot.png)

While the average sentiment was positive across the board, we see a large amount of variation within between regions. The sentiment of the West Coast and Northeast, for example, was markedly more positive than the South. Comparatively, sentiment in the EU was much more affirmative, reflecting their higher concern about climate change and proactive stance in addressing it. The EU has historically been at the forefront of the Paris Agreement and pursuing ambitious climate intiiatives like the European Green Deal which underscores this sentiment. Meanwhile in the U.S., sentiment appears more divided along political lines, reflected in policy fluctations regarding climate change at the federal level.

**Data visualization**

We used `pandas`, `matplotlib`, and `seaborn` to create the graphs of the climate data. We loaded the data to a `pandas` data frame from a GitHub link to the .csv files. Our main considerations were the frequency distribution of sentiment as well as sentiment score over the course of the three years in our designated time period. We plotted histograms of the frequency of the sentiment score, using the data from the entire time period. For both countries, the data was negatively skewed, indicating overwhelming positive sentiment across the board. This was a bit unexpected, as we thought that such a divise topic might create a lot of negative sentiment. 

![hist-eu](https://github.com/caroline710/big-data-final/assets/136007158/567f987a-4cc3-431c-b868-b266ff851d34)
![hist-usa](https://github.com/caroline710/big-data-final/assets/136007158/09eb6195-0eaa-4662-bc5b-b01d60e3f5cc)


We also developed lineplots mapping the sentiment score across the months, and separated the graphs by year; both countries were included on each graph for comparative purposes. Once created, we looked for general trends, as well as the sentiment surrounding significant events related to climate policy and discourse. In general, sentiment scores decreased throughout the three year time period. Additionally, the EU countries had more positive sentiment than the USA.

![2018-graph](https://github.com/caroline710/big-data-final/assets/136007158/f4682133-5366-4940-b5b4-1f04e78bc1b4)
The most notable event in 2018 was the United Nations Climate Change Conference (COP24) in December. Around that time, sentiment was high, but fell in the following month, perhaps due to discourse surrounding the event.

![2019-graph](https://github.com/caroline710/big-data-final/assets/136007158/59bb38d5-f1f5-4dd4-9d93-fdc76cc318b4)
For the first half of 2019, there were various student protests going on around Europe, which could be the cause of the general downwards trend in the EU data.

![2020-graph](https://github.com/caroline710/big-data-final/assets/136007158/48e0f3aa-a8c6-4fa1-84c4-681c4dc1e38a)
Lastly, the COVID-19 pandemic starting in March 2020 produced an upwards trend in sentiment for a few months. Reflecting back on the time period, many people were discussing nature healing due to the lack of human pollution, as people worldwide were in quarantine. Both countries started to see a downward decline when the world started to reopen during the summer.

**Challenges and Future Directions**

Following our difficulties scraping, we faced difficulty with the type of data produced. Some Tweets were in foreign languages and could not be run through the model, so we opted to eliminate them. We also faced the aforementioned location data issues with user input. During the visualization step, the date data was formatted in a manner that was not readable by `seaborn`, so we had to turn the format into `datetime` objects.

If we had more time, we would try to expand our EU tweets dataset, and rerun the distilBERT model on those tweets. We would also try to expand the model to run sentiment analysis on tweets about Greta Thurberg and her impact on climate change. The difficulty to determine whether discourse about Greta is political or related to the environment would have to be differentiated in a future model. 

Additional future directions could be looking at other continents, using other political or activist figureheads as a timeline, and further integrating geopolitical data for multi-variable analysis. 

