#Starting Data
customer_feedback = [
    "The service was excellent and the food was great!",
    "I love the design, but was disappointed with the battery life.",
    "The coffee is okay, nothing special.",
]
positive_keywords = ['excellent', 'great', 'love', 'amazing', 'satisfied']
negative_keywords = ['disappointed', 'bad', 'terrible', 'horrible', 'issue']

#define a analyze_feedback function , it's the main function in the program
def analyze_feedback(feedback_data):
    #intialize an empty array who holds latter a list of dictionaries of result
    analysis_results = []
    #loop through the comments
    for comment in feedback_data:
        score = 0
        keywords_found = []
        #transfer the comment to a version of the comment in lower case for correct comparaison
        comment_lower = comment.lower()

        #loop through the keywords to find the keywords the positive and negative ones  that are in the comment
        for keyword in positive_keywords:

            if keyword in comment_lower:
                score += 1
                keywords_found.append(keyword)
            else :
                continue


        for keyword in negative_keywords:
            if keyword in comment_lower:
                score -= 1
                keywords_found.append(keyword)

        #initialize a variable to store the final sentiment par rapport the score
        final_sentiment = ''
        if score > 0 :
            final_sentiment = 'positive'
        elif score < 0 :
            final_sentiment = 'negative'
        elif score == 0 and keywords_found:
            final_sentiment = 'mixed'
        else :
            final_sentiment = 'neutral'

        #create a dictionary that hold the final data
        result = {'original_comment' : comment , 'sentiment' : final_sentiment,
                  'score' : score , 'keywords_found': keywords_found}

        #add the result dictionary to the analysis_results array
        analysis_results.append(result)

    #return the final analysis_results after the loop has stopped
    return analysis_results

#create a variable to hold the return of the function
feedback_result = analyze_feedback(customer_feedback)

#print a report to display the data in a cohesive way
print("===== Detailed Sentiment Analysis Report =====")
for feedback in feedback_result:
    print(f"\nComment: \"{feedback['original_comment']}\"")
    print(f"- Sentiment: {feedback['sentiment']} (Score: {feedback['score']})")
    print(f"- Keywords Found: {feedback['keywords_found']}")
print("===============================================")