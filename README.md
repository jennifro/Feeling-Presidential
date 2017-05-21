# Feeling Presidential

Machine learning is a rising prodigal field, especially in terms of written language sentiment analysis. Politics is an old stalwart, with [old issues](http://www.washingtonpost.com/wp-srv/national/longterm/supcourt/stories/courtguns051095.htm) with [written language](https://www.theatlantic.com/international/archive/2015/06/magna-carta-800-anniversary/395753/) & sentiment analysis.

In the post-television era, other visual & audio factors are often at play in presidential speeches; eloquence, charm, etc. But considering Presidents are a relatively standard set, I thought it would be interesting to see what computer sentiment analysis could tell us about sentiment, and if it would match relative to historical events. 

#### Speeches
For data normalization, I decided to stick with analyzing speeches from presidents in the 'modern' era - from Kennedy to Obama - to eliminate natural changes in language and means of communication as a source of skewed results. Presidents give speeches for different reasons, so I stuck with speeches most common to all presidents; the inaugural address, first State of the Union, and last State of the Union. This itself isn't entirely consistent; history buffs will know/remember that Ford never gave an [inaugural address per se](http://millercenter.org/president/ford/speeches/speech-3390) and Johnson did a State of the Union before he did an inaugural address.

Using [Scrapy](https://docs.scrapy.org/en/latest/intro/tutorial.html), speeches were scraped from [the University of Virginia Miller Center's speech archive](http://millercenter.org/president/speeches) and parsed to remove low-information words like 'and', 'or', 'the' et al.

#### Sentiment Analysis
###### Supervised Machine Learning

I decided to use the [Naive Bayes Algorithm](https://en.wikipedia.org/wiki/Naive_Bayes_classifier) on a two sets of U.S. political speeches. For the tagging, I decided on positive and negative to represent overall favorability from the U.S. media. In the json files I have indicated the souce of the speech for reference. 

###### Training Set

This project is about understanding the mechanics of using machine learning for sentiment analysis. Most machine learning is done across multiple computers analyzing tens of thousands of texts. This project is very micro, using a training set of ___ texts.

To create the training set, I searched many different websites to find political speech texts that could be tagged as mostly positive or mostly negative, pulling not only from presidents but other political figures. Using NLTK's [Naive Bayes classifier](http://www.nltk.org/_modules/nltk/classify/naivebayes.html), feature dictionaries were created for the 1500 most common words in the positive and negative training sets and the classifier was trained on a sample of seven-eighths of each training set, tested on the remaining eighth.

The trained algorithm was then used to classify the set of 30 Inaugural and SotU speeches for two sets of results: overall speech sentiment, and most common phrase sentiment. The definition I use for most common phrase in this case is a bigram - a two word phrase - that was repeated at least 3 times. For the bigrams a "neutral" category had to be developed for bigrams with conflicting sentiment - one word shows as "positive" and the other as "negative".

###### Results

Accuracy for the Naive Bayes classifier is currently around 65%. The main reason for this is because a lot of the language in the 


Increasing the size of the training set would greatly improve accuracy, and if you would like to contribute to the training corpora, please email the link or full speech text to jen.dxon@gmail.com with 'Speech Analysis' in the subject line, or add to the appropriately tagged .json file and submit a pull request.
 


#### Visualization

This is a screenshot of the d3.js force layout displaying sentiment analysis of the most common phrases:
![bigrams](https://cloud.githubusercontent.com/assets/12589761/18492967/ffec32ee-79c2-11e6-9e71-953f7d8dd81b.png)

Here is a screenshot of the sentiment analysis of all speeches on a timeline:
![timeline](https://cloud.githubusercontent.com/assets/12589761/18492994/2184ed38-79c3-11e6-8b8e-93ae2ce4f346.png)

#### Special Thanks
This project could not have been done without [this amazing blog](http://streamhacker.com/2010/05/10/text-classification-sentiment-analysis-naive-bayes-classifier/) on using NLTK for sentiment analysis. 

Shout out to the supportive staff at [Hackbright Academy](https://hackbrightacademy.com/) who encouraged me to take on the challenge.
