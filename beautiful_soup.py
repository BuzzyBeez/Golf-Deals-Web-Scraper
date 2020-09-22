#! python3
# this program is a webscraper that goes to a supremegolf and gets the best deals of the day.

#at some point I will add a text option so we can send text messages to some one with the best deals
# I also want to add other sites so we can scrape like 3 golf booking sites and send a text with the best 3 deals



import requests, bs4           # import beautifulSoup and request

url = 'https://supremegolf.com/tee-times/near/san-jose-california-united-states'

res = requests.get(url)                     # use requests to get the site

try:                                        # here are just chekcing to make sure there is no issues with the site
    res.raise_for_status()
except Exception as exc:
    print(f'There was an error {exc}')

soup = bs4.BeautifulSoup(res.text, 'html.parser')        # Use BeautifulSoup to get the html text and parse it
try:
    findTag = soup.find('div', {"class": "js-teetime-wrap"}) # find the body div with all the links in it
except:                                                         # check to make sure the website hasn't been updated or changed
    print('Please check wbsite as elements may have chaged')


httpList = []                                            # we need an emptuy list to put the html dictonaries into

for links in findTag.findAll('a'):                        # find all the 'a' tags in side the div body which returns a dic
    for key, values in links.attrs.items():                # go through and match the value with the link /tee-times/at and add it to the list
        if 'https://supremegolf.com/tee-times/at/' in values:
            httpList.append(values)


newHttpList = []                                        # because the body has multiple links for the same thing we need to
                                                        # make a new list and just append the different links and not the same ones
for hrefs in httpList:
    if hrefs not in newHttpList:
        newHttpList.append(hrefs)
print(newHttpList[:3])
