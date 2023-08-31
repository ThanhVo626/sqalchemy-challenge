# sqalchemy-challenge
Created and engine to pull info from sqlite file then set up the information into a database.
We then created a link between python and the DB
Then we started querying the information we needed
In addition we had to learn how to properly use datetime in order to go back 365 days back instead of manually do the math ourselves to filter the information.
Had to use dir to find out what information was in our db to find precipitation and temperature.
Then we plotted the information that was need.

In terms of the next part the beginning setup was the same.
After did the standard Flask setup with creating an app then made routes to whatever we needed.
Most functions were copy and paste from the previous parts with minor editing.
One problem I ran into was that the sessions were closing after each URL use.
So in each function I had to add a new open and close session.

Last week I had a lot of things going on so I could't finish this assignment. So thats why I'm turning in late.
