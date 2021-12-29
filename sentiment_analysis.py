def compute_tweets(tweet_file, keyword_file):
    try:

        a = open(tweet_file, "r", encoding="utf-8")
        b = open(keyword_file, "r", encoding="utf-8")

        #Step 1: WORD PROCESSING FOR THE TWEETS

        list_of_tweets = a.readlines() #split each line into an element in a list
        raw_list = [] #include numbers
        i=0
        for line in list_of_tweets:
            line = line.rstrip("\n")
            line = line.split(" ")
            raw_list.append(line)

        tweet_list =[]
        for item in raw_list:
            tweet_list.append(item[5:])

        #Step 2: WORD PROCESSING FOR THE KEYWORD ARTICLE

        list_of_keywords = b.readlines() #split each line into an element in a list
        list_of_processed_keywords = []
        for line in list_of_keywords:
            line = line.rstrip("\n")
            line = line.split(",")
            list_of_processed_keywords.append(line)
        word_list = []
        for i in range(len(list_of_processed_keywords)):
            word_list.append(list_of_processed_keywords[i][0])
        score_of_sentiment_values = []
        for i in range(len(list_of_processed_keywords)):
            score_of_sentiment_values.append(list_of_processed_keywords[i][1])





        #Step 3: LOCATION COORDINATES PROCESSING FOR THE TWEETS
        #Creating a list of longtitude and latitude points for all tweets

        latitude_coordinates_list =[]
        longtitude_coordinates_list =[]
        for i in range(0, len(raw_list)):
            latitudepoint = raw_list[i][0]
            latitudepoint = latitudepoint.lstrip("[")
            latitudepoint = latitudepoint.rstrip(",")
            latitudepoint = float(latitudepoint)
            longitudepoint = raw_list[i][1]
            longitudepoint = longitudepoint.rstrip("]")
            longitudepoint = float(longitudepoint)
            latitude_coordinates_list.append(latitudepoint)
            longtitude_coordinates_list.append(longitudepoint)



        #Step 4A): STRIPPING AWAY PUNCTUATION FROM THE BEGINNING OF THE TWEET
        punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
        individualtweet = []
        newtweet =[]
        list_without_beginning_punc =[]
        for line in tweet_list:
            letterstart = 0
            individualtweet =[]
            for word in line:
                letterstart = 0
                word = word.lower()
                for letter in word:
                    if letter in punc:
                        letterstart +=1
                    else:
                        break
                newword = word[letterstart:]
                individualtweet.append(newword)
            list_without_beginning_punc.append(individualtweet)


       #Step 4B): STRIPPING AWAY PUNCTUATION FROM THE END OF THE TWEET
        list_without_any_punc =[]
        for line in list_without_beginning_punc:
            individual_tweet_without_punc =[]
            for word in line:
                if len(word)>1:
                    letterend = len(word)-1
                    for i in range(len(word)-1,0,-1):
                        if word[i] in punc:
                            letterend = letterend -1
                        else:
                            break
                    newword = word[0:letterend+1]
                    individual_tweet_without_punc.append(newword)
                else:
                    newword = word
                    individual_tweet_without_punc.append(newword)
            list_without_any_punc.append(individual_tweet_without_punc)

        #Step 5: USING LONGTITUDE AND LATITUDE POINTS TO CREATE A LIST OF INDEXES ON THE LIST ARE WITHIN THE SPECIFIED BOUNDS
        index=0
        latitude_index_specified_list = []
        for elem in latitude_coordinates_list:
            if elem <=49.189787 and elem >=24.660845:
                latitude_index_specified_list.append(index)
            index+=1
        longtitude_index_specified_list = []
        index = 0
        for elem in (longtitude_coordinates_list):
            if elem <=-67.444574 and elem >=-125.242264:
                longtitude_index_specified_list.append(index)
            index+=1
        cumulative_index_list =[]
        for elem in latitude_index_specified_list:
            if elem in longtitude_index_specified_list:
                cumulative_index_list.append(elem)
        cumulative_index_list_without_duplicates = []
        for elem in cumulative_index_list:
            if elem not in cumulative_index_list_without_duplicates:
                cumulative_index_list_without_duplicates.append(elem)

        #Step 6: CREATING A LIST OF LOCATIONS AND TWEETS WITHIN THE SPECIFIED GEOGRAPHICAL BOUNDS
        list_of_locations_within_bounds = []
        for elem in cumulative_index_list_without_duplicates:
            list_of_locations_within_bounds.append(longtitude_coordinates_list[elem])
        list_of_tweets_in_geographical_bounds = []
        indexoftweet = 0
        for i in range(len(list_without_any_punc)):
            if indexoftweet in cumulative_index_list_without_duplicates:
                list_of_tweets_in_geographical_bounds.append(list_without_any_punc[indexoftweet])
            indexoftweet +=1

        #Step 7: COMPUTING THE AVERAGE SCORE OF EACH TWEET WITHIN GEOGRAPHICAL BOUNDS AND APPENDING THEM TO AN AVERAGE SCORE LIST
        average_score_list = []
        for line in list_of_tweets_in_geographical_bounds:
            score_for_line =0
            number_of_keywords_in_line = 0
            average_score = 0
            for word in word_list:
                for elem in line:
                    if elem == word:
                        number_index = word_list.index(word)
                        score_of_each_word = score_of_sentiment_values[number_index]
                        score_of_each_word = int(score_of_each_word)
                        score_for_line += score_of_each_word
                        number_of_keywords_in_line +=1
            if score_for_line == 0:
                average_score == 0
            else:
                average_score = score_for_line/number_of_keywords_in_line
            average_score_list.append(average_score)

        #Step 8: APPEND THE AVERAGE SCORES TO A LIST FOR EACH LOCATION
        eastern_list =[]
        central_list =[]
        mountain_list =[]
        pacific_list =[]

        index =0
        for i in range (len(average_score_list)):
            item = list_of_locations_within_bounds[index]
            if item>= -87.518395 and item<=-67.444574:
                eastern_list.append(average_score_list[i])
            elif item>=-101.998892 and item<-87.518395: ####
                central_list.append(average_score_list[i])
            elif item>=-115.236428 and item<-101.998892:
                mountain_list.append(average_score_list[i])
            elif item>=-125.242264 and item<-115.236428:
                pacific_list.append(average_score_list[i])
            index +=1

        #Step 9: COMPUTE THE HAPPINESS SCORE FOR EACH REGION
        total_happiness_score_eastern = 0
        eastern_happiness_score =0
        count_of_keywords_tweets_eastern=0
        count_of_tweets_eastern = len(eastern_list)
        if len(eastern_list)!= 0:
            for elem in eastern_list:
                total_happiness_score_eastern+= elem
                if elem>0:
                    count_of_keywords_tweets_eastern +=1
            if count_of_keywords_tweets_eastern>0:
                eastern_happiness_score = total_happiness_score_eastern/count_of_keywords_tweets_eastern


        total_happiness_score_central = 0
        central_happiness_score =0
        count_of_keywords_tweets_central=0
        count_of_tweets_central = len(central_list)
        if len(central_list)!= 0:
            for elem in central_list:
                total_happiness_score_central+= elem
                if elem>0:
                    count_of_keywords_tweets_central +=1
            if count_of_keywords_tweets_central>0:
                central_happiness_score = total_happiness_score_central/count_of_keywords_tweets_central

        total_happiness_score_mountain = 0
        mountain_happiness_score =0
        count_of_keywords_tweets_mountain=0
        count_of_tweets_mountain = len(mountain_list)
        if len(mountain_list)!= 0:
            for elem in mountain_list:
                total_happiness_score_mountain+= elem
                if elem>0:
                    count_of_keywords_tweets_mountain +=1
            if count_of_keywords_tweets_mountain>0:
                mountain_happiness_score = total_happiness_score_mountain/count_of_keywords_tweets_mountain

        total_happiness_score_pacific = 0
        pacific_happiness_score =0
        count_of_keywords_tweets_pacific=0
        count_of_tweets_pacific = len(pacific_list)
        if len(pacific_list)!= 0:
            for elem in pacific_list:
                total_happiness_score_pacific+= elem
                if elem>0:
                    count_of_keywords_tweets_pacific +=1
            if count_of_keywords_tweets_pacific>0:
                pacific_happiness_score = total_happiness_score_pacific/count_of_keywords_tweets_pacific



        eastern_info_list = (round(eastern_happiness_score,2), count_of_keywords_tweets_eastern,count_of_tweets_eastern)
        central_info_list = (round(central_happiness_score,2), count_of_keywords_tweets_central,count_of_tweets_central)
        mountain_info_list = (round(mountain_happiness_score,2),count_of_keywords_tweets_mountain,count_of_tweets_mountain)
        pacific_info_list = (round(pacific_happiness_score,2), count_of_keywords_tweets_pacific, count_of_tweets_pacific)
        return [eastern_info_list, central_info_list, mountain_info_list, pacific_info_list]
    except:
        empty_list=[]
        return empty_list







