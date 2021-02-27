# TravelShopper
Almost every traveler shops for his/her travel. Once they plan their travel & book their tickets, they hit the stores or shop online for their travel needs. It invariably is at the minimum a two step hassle and comes with laborious searching & at times scampering for things at the last minute and could even spoil the travel/holiday mood.
TravelShopper's smart AI engine automatically detects travelers by partnering with travel booking sites/companies, immediately intelligently identifies the traveller's needs and guides them to their personalized Walmart shopping cart. 


For this we used 
#Content based filtering
Content based filtering was used to segregate important fields that was used for our application inorder to get the required fields by the application. In our case we have used the tags from the item and mapped it to the tags from the location. Item tags can be genrated by the description of an item or can be readily available as keywords in an item. 
Location can have tags related to the weather/culture/activities that are taking place at a particular city 


This project has 3 partts to it 
1. Extension(Chrome extension)
2. UI(Written over react)
3. recommendation system(Made on collaborative filtering)

How to use


travelshopper.ipynb exposes a rest endpoint which can be used by the ui for showing the recommendation based on location
use the extension folder to create the chrome extension
there is a basic ui to demo the piece


