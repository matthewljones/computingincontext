###Computing in Context
##Social Science 
##HW #2

Due date: 24 April, 6pm. [note the earlier time]
Submit a `readme` file with your assignment, as you've done earlier in the course, concerning any challenges you encountered with or observations on the homework.

I hope everyone's got their platforms working like butter now!

##APIs for fun and profit

Let's do more with the SUNLIGHT APIs.

Today let's use http://tryit.sunlightfoundation.com/influenceexplorer on campaign finance

 recall the basic syntax of forming a query using `requests`:

	import requests

	SUNLIGHT_API_KEY = "REPLACE THIS WITH THE LONG API KEY YOU RECEIVED IN YOUR EMAIL"
	SUNLIGHT_API_URL = ## this will change now ##

	query_params = {#HERE YOU'LL PUT YOUR PARAMS as a dict#; 'apikey': SUNLIGHT_API_KEY}

	r = requests.get(SUNLIGHT_API_URL, params=query_params)
	responses = r.json()


Let's start with:

	query_params = {'city': "Las Vegas", 'apikey': sunlight_api}
	SUNLIGHT_API_URL="http://transparencydata.com/api/1.0/earmarks.json"  #note this has changed
	r = requests.get(SUNLIGHT_API_URL, params=query_params)
	responses = r.json() 

0) Look at the API documentation http://tryit.sunlightfoundation.com/influenceexplorer for earmarks. What parameters can you pass to earmarks.json?

1) Using a list comprehension, not a `for` loop, create two lists from these responses:
	a) all the final amounts of the earmarks in your results
	b) all the text of the "bill section" of the earmarks. What do you think this field is?

2) Do (1) again but for another city of your choice. You're best off with cities with powerful politicians....

3) Ok, now you'll need to figure our how to alter the URL and the query_params in the black box above using the API documentation.

	For 2012 and 2008, who are the top 30 "individuals by contributions given"?  

	Make a `dict` that has the 2012 individual's names as keys and their total contributions as values.

## We'll talk more about text mining in lecture before I give you a problem set on them.

##Looking ahead

Time to start thinking about some data for the final assignment. 
There are many places to start. For ideas, check out:

github.com/caesar0301/awesome-public-datasets/blob/master/README.rst 

but that's just the start.

At the bottom of your homework, just put what preliminary ideas you've had; if there's a particular format you're going to need help with, let us know too. 

