# Scraping the FBI fugitive page
## Why
I’m currently a journalism senior at the University of Florida in [Professor McAdam’s]( https://github.com/macloo) advanced web apps course. As part of our curriculum, we put together a scraping project. I was bopping around on the internet for something I wished would be in a neat database, and thought the FBI fugitive page looked interesting. It has every active fugitive the FBI is seeking, and individual pages have more details.  
## General information
For this project, I used two python files. The first was to scroll to the bottom of the main [fugitive page]( https://www.fbi.gov/wanted/fugitives), scrape all the URLS and save them into a text file. The second file had a loop to open each URL, scrape the data for each individual, and then write that data into a CSV file. 
## Step one: Selenium infinite scroll
The first issue I had to confront was that the FBI main fugitive page uses an infinite scroll to see all the listed individuals. I knew I had to use Selenium, which operates out of a browser, but wasn’t sure how. With the code I found on [this blog post] (https://michaeljsanders.com/2017/05/12/scrapin-and-scrollin.html) I was able to get it to scroll to the bottom of the page. I put this code into my fbi2.py file. 
## Step two: Getting all the URLS
Once I had my page loaded thanks to Selenium, I was able to scrape for all the individual’s URLs. I did this with a loop that looked for where the links were saved. I saw by inspecting the HTML that they were in the p element tag with the class “name” so used a basic BeautifulSoup line to gather all of that. I then saved the URLS into a text file. I did this with a for loop (for person in people). This is the end of my first file. 
## Step three: Looping over all URLS
I then wrote a separate file for the next step, which would create a function that loops over every URL and gathers the data I want. This is my fbifinal.py file, and my fugitive_detail() function. 
First in this file, I import Selenium because it will need to be used on each individual page opened. The FBI’s website requires headers. Though I figured out how to open one individual web page at a time with headers, I couldn’t figure out how to get it in the loop. Instead I figured out how to use the loop with Selenium, which has headers because it is a browser. To do this, I just made my driver.get() take an argument, not a direct URL, within my loop. 
To loop over all the URLS, which are now saved in a text file from the first file, I had to first read them. I opened the file and stripped the extra tags off the URLS that came in when I read the file lines. 
In my function, I am searching for desired information on each page, which I found by examining the HTML tags. I know that every page, no matter what it is, has a name and summary of charges, so was able to find those easily using BeautifulSoup. However, other things I was seeking were not uniform on every page, like the tables or rewards.
I overcame this by using try/except code. I would have it try to find the path or write “N/A” if it didn’t exist. The N/A was saved into a variable so it could go into my list and then my CSV. 
### The tables
Most of the FBI fugitive pages have a table, but some do not. Those tables are uniform, but do not have separating class or id tags to demarcate the header from the value. To scrape the values in the table, also knowing that not every fugitive has the same values on their table and some have no tables at all, I first used a try/except code to make sure there was a table on the page. Then I used an if that first set the variables at an empty value. Then I used an if/elif code to search for each of the values I wanted by making it exactly equal the string I was looking for, like “Place of Birth.” Using next_sibling, I could find the value and store it in a variable that I fed into my CSV. 
## Step four: Writing into a CSV file
Before writing into a CSV file, I had to create a list to make my rows. I filled an empty list I created earlier with each of the variables I was seeking, like name or reward, separated by commas. I then created another empty list named row, and looped over every item in the first list with details to append the row list with each set of values. I then used the CSV writer to write row into my file, which I opened at the start of the document outside my loop or functions. And it worked!
I also have a time delay in my file, to make sure I don’t get kicked off. 




