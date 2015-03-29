
#computing in context
#social sciences 
#first assignment
#a little practice with pandas and with lists+dicts

Prelude 1

Get ipython and pandas working on your computer. The easiest way is to install Anaconda python.


Prelude 2

Go to http://sunlightfoundation.com/api/ and "Get a Key"! You'll need to sign up for an account and get a API Key, which is a long string of numbers and letters. This key will allow you to request data about the US Congress and elections. It's really awesome. Copy this API key somewhere. You'll need it.


Part I. 


For now, I'll give you a black box to get some data; I'll unpack this a bit soon.

Use this code to get started. We're going to ask for a bunch of speeches in Congress about Cyber Security.

#blackbox begins here

	import requests

    SUNLIGHT_API_KEY = "REPLACE THIS WITH THE LONG API KEY YOU RECEIVED IN YOUR EMAIL"
    SUNLIGHT_API_URL = "http://capitolwords.org/api/1/text.json"

    search_phrase = "cyber security" 
    query_params = {'phrase': search_phrase, 'apikey': SUNLIGHT_API_KEY}

    r = requests.get(SUNLIGHT_API_URL, params=query_params)
    responses = r.json().get('results')

#blackbox ends here

1) How many responses are there in `responses`? What is the datatype of each response?

2) Who is speaking in each response?

	a) Create a list of the last names of all the speakers? Hint: use a list comprehension!

	b) Print the last name of each speaker and then his/her political affiliation.

3) Look through your results until you find a speech of more than one line.

	What is the data format of more lengthy speeches?

4) Now for something new.

	" ".join(#PUT_ANY_LIST_HERE) will concatenate a list of strings into one string. 

	So `" ".join(["how", "now", "brown", "cow"])` will yield `'how now brown cow'`

	a) Use this to combine the broken up parts of one speech.

	b) Use this to combine the broken up parts of all the speeches

5) the splits

The `split()` method breaks up a string into a list of strings--the words (more or less). 
So: `"hi there".split() yields ["hi", "there"]`

How many words are there in each speech? (Do this as a list comprehension.)

6) go back to the blackbox above. Pick a phrase Congress is likely to have have talked above of late. Modify the blackbox code to search for that phrase. Explain what you changed.


Part II. `pandas` practice

Get the EdX data we used in class from courseworks; it's a 70MB file. 

1) Import the csv file using pandas like in class.

Using pandas, use indexing to pick out:

    1) a dataframe with only the User Id column

    2) a dataframe with the grade column

    3) a dataframe with the User ID *and* grade columns. 

    Hint: pass a list of column names rather than just one column name

    4) rows 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, first individually, then all at once

    You can get a single row using the .ix method. E.g. df.ix[200] 
    will get the 200th row of a dataframe named df. You can pass a list to df.ix to get more.

2) Pick something to graph: that is, find something to use the `.plot()` method on. (Look at the example from class). Play around with this. You don't need to include the plot, only the code you used to plot.

We'll play more with the data set next week.


