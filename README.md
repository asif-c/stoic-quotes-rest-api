# stoic-quotes-rest-api
A REST API, when called, gives a randomly selected quote from one of the ancient Stoic philosophers.
The API URL is https://asifchoudhury.ca/StoicQuotesRESTAPI/?format=json

Example of calling the API:

From any internet-connected computer,via terminal or command-line interface, type:

curl https://asifchoudhury.ca/StoicQuotesRESTAPI/?format=json

The output should look like:

[{"philosophers_name":"Epictetus, Discourses, 2.6.25","quotes":"A podium and a prison is each a place, one high and the other low, but in either place your freedom of choice can be maintained if you so wish."}]

Each time the API is called, a new quote will appear.

Technical features:

-Built using Django REST framework, PostgreSQL

-Hosted in AWS
