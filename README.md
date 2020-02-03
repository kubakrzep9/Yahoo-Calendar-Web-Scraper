# Yahoo-Calendar-Web-Scraper

[DISCONTINUED]
Note: I was able to successfully pull sets of stocks and relevant information (price, volume, etc). I was able to filter through this data set to identify a set of stocks that fit my criteria however, the front end aspect was a challenge for me. I used Tkinter to build a GUI to display the information but, I could not finish it. I decided to move onto more pressing projects, namely my <a href="https://github.com/kubakrzep9/Robotic-Arm-Interface">Robotic Arm Interface</a>, that I believed would be more beneficial. I intend on returning to this program concept, however I will most likely write it in Java and incorporate it into my <a href="https://github.com/kubakrzep9/Trader-Tools">Trader-Tools app</a>. 



Project Description

This a work in progress. I have currently been able to scrape the Yahoo Finance Calendar for Earnings Reports being released the following day under a specified price range. I have also begun building the GUI, which I have already sketched out and designed. This is all a learning process for me as I have had to learn how to use Beautiful Soup (to web scrape) and tkinter (to build the GUI). 

The web scraper will allow the user to select a specific event: earnings report release, stock split or IPO. The user will then be able to specify certain conditions to filter through the companies releasing the event the following day. The current planned conditions will be to filter based on: price, volume, average volume and float. I have no doubt more conditions will be added to allow the user to customize their scan to their desire. 

The user will be able to add as many conditions as they would like (as many as there are conditions). The GUI will have a condition box where the user can add or delete conditions. The condition box will be made up of condition rows. Each condition row will have a drop down menu to select a condition, and min and max input fields to filter their condition. 

Once the user is satisfied with their conditions, they may scan and their results will be displayed in the display box. The display box will be made up of display rows that presents each company's: ticker, name, current price and event release time (pre-market, after-hours or unknown). I may add price change information as well to give the user a better understanding of the stock. I would also like to add a feature where if the user right clicks on a row a menu would drop down and would allow the user to do a number of actions. One of which would be to visit the Yahoo Finance page of the specified company.

Though this is all new to me, I am excited about the learning process. There have definetely been frustrating moments, but the satisfaction of finally making something work is worth the while. 
