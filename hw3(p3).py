
def check_query(data_list,query):
    for word in query:
        #check of there exist any word in the query that is not present in the string
        if word not  in data_list:
            return False

        return  True
data_list="You can decide what you are going to think in any given situation. Your thoughts and feelings determine your actions and determine the results you get. It all starts with your thoughts – and I have found that inspirational words are a quick way to retune your thinking"
query = "thoughts and feeing"

query = query.split()
#calling the function to print output
print('ans',check_query(data_list,query))