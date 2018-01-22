# Feeling Presidential

When a politician makes a speech, what are they trying to tell us? 

  - Vote for me.
  - I am not a crook.
  - Donate to my campaign.

Seriously though, the intent behind a speech and the actual meaning conveyed can differ in any human speech. Using machine learning to perform sentiment analysis, Feeling Presidential provides visualization of the phrases most commonly repeated in speeches given from U.S. Presidents and overall sentiment.

#### Speeches
For data normalization, I decided to stick with analyzing speeches from presidents in the 'modern' era - from Kennedy to Obama - to eliminate natural changes in language and means of communication as a source of skewed results. Presidents give speeches for different reasons, so I stuck with speeches most common to all presidents; the inaugural address, first State of the Union, and last State of the Union. This itself isn't entirely consistent; history buffs will know/remember that Ford never gave an [inaugural address per se](http://millercenter.org/president/ford/speeches/speech-3390) and Johnson did a State of the Union before he did an inaugural address.

Speeches were scraped from [the University of Virginia Miller Center's speech archive](http://millercenter.org/president/speeches) and parsed to remove low-information words like 'and', 'or', 'the' et al.

#### Sentiment Analysis
In order to do train the algorithm, a training set needed to be created. I searched many different websites to find political speech texts that could be tagged as mostly positive or mostly negative, pulling not only from presidents but other political figures. Using NLTK's [Naive Bayes classifier](https://en.wikipedia.org/wiki/Naive_Bayes_classifier), feature dictionaries were created for the 1500 most common words in the positive and negative training sets and the classifier was trained on a sample of seven-eighths of each training set, tested on the remaining eighth.

Accuracy for the Naive Bayes classifier is currently around 65%. Increasing the size of the training set would greatly improve accuracy, and if you would like to contribute to the training corpora, please email the link or full speech text to jen.dxon@gmail.com with 'Speech Analysis' in the subject line, or add to the appropriately tagged .json file and submit a pull request.

The set of 30 Inaugural and SotU speeches were analyzed using the trained classifier and given a rating of either positive or negative. 

In the dataset, if a bigram (set of 2 words) was repeated at least 3 times, I considered it a 'common' phrase to that speech. The most common bigrams were also analyzed for sentiment with Naive Bayes, and given a rating of either 'positive', 'negative', or 'neutral'. Neutral ratings were assigned to bigrams with conflicting sentiment - one word shows as positive and the other as negative.

#### Visualization

This is a screenshot of the d3.js force layout displaying sentiment analysis of the most common phrases:
![bigrams](https://cloud.githubusercontent.com/assets/12589761/18492967/ffec32ee-79c2-11e6-9e71-953f7d8dd81b.png)

Here is a screenshot of the sentiment analysis of all speeches on a timeline:
![timeline](https://cloud.githubusercontent.com/assets/12589761/18492994/2184ed38-79c3-11e6-8b8e-93ae2ce4f346.png)

#### Special Thanks
This project could not have been done without [this amazing blog](http://streamhacker.com/2010/05/10/text-classification-sentiment-analysis-naive-bayes-classifier/) on using NLTK for sentiment analysis. 

Shout out to the supportive staff at [Hackbright Academy](https://hackbrightacademy.com/) who encouraged me to take on the challenge.
