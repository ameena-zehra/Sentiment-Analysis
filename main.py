#Assignment #3 CSC1026
#Ameena Naqvi

#Import sentiment analysis module
import sentiment_analysis
#PROMPTING USER FOR TWO FILES
tweet_file = input("Enter tweet file:")
keyword_file = input("Enter keyword file:")

#Call the compute_tweets function in Sentiment Analysis Module using user entered input
print()

results = sentiment_analysis.compute_tweets(tweet_file, keyword_file)
print()
print("Results for:", tweet_file, keyword_file)
print()
index=0
if len(results) >0:
    for line in results:
        if index == 0:
            print("EASTERN:     ", end =" ")
            index_of_elem =0
            for elem in line:
                if index_of_elem==0:
                    print("Average Happiness Score: {:.2f}".format(elem))
                formatter = "EASTERN:     "
                if index_of_elem==1:
                    print(" "*len(formatter), "Number of Keyword Tweets:", elem)
                if index_of_elem==2:
                    print(" "*len(formatter),"Number of Tweets:", elem)
                index_of_elem+=1
        if index == 1:
            print("CENTRAL:     ", end=" ")
            index_of_elem =0
            for elem in line:
                if index_of_elem==0:
                    print("Average Happiness Score: {:.2f}".format(elem))
                formatter = "CENTRAL:     "
                if index_of_elem==1:
                    print(" "*len(formatter),"Number of Keyword Tweets:", elem)
                if index_of_elem==2:
                    print(" "*len(formatter),"Number of Tweets:", elem)
                index_of_elem+=1
        if index == 2:
            print("MOUNTAIN:    ", end=" ")
            index_of_elem =0
            for elem in line:
                if index_of_elem==0:
                    print("Average Happiness Score: {:.2f}".format(elem))
                formatter= "MOUNTAIN:    "
                if index_of_elem==1:
                    print(" "*len(formatter), "Number of Keyword Tweets:", elem)
                if index_of_elem==2:
                    print(" "*len(formatter), "Number of Tweets:", elem)
                index_of_elem+=1
        if index ==3:
            print("PACIFIC:     ", end=" ")
            index_of_elem =0
            for elem in line:
                if index_of_elem==0:
                    print("Average Happiness Score: {:.2f}".format(elem))
                formatter= "PACIFIC      "
                if index_of_elem==1:
                    print(" "*len(formatter),"Number of Keyword Tweets:", elem)
                if index_of_elem==2:
                    print(" "*len(formatter), "Number of Tweets:", elem)
                index_of_elem+=1
        index+=1
        print()
else:
    print(results)
