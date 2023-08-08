"""
2. Write a Python program to validate the  twitter url and extract twitter url from the given
 text and give the count of valid url present in the text.
 “Follow our leader Elon musk on   twitter here: https://twitter.com/elonmusk,
 more information on Tesla's products can be   found at https://www.tesla.com/.
 Also here are leading influencers for tesla related news,
 https://twitter.com/teslarati https://twitter.com/dummy_tesla       https://twiter.com/dummy_2_tesla”
"""




import re

urls = "https://twitter.com/elonmusk, https://www.tesla.com/, https://twitter.com/teslarati, https://twitter.com/dummy_tesla, https://twiter.com/dummy_2_tesla"

def is_valid_twitter_url(url):
    # validate a Twitter URL
    res = r'^https?://(?:www\.)?twitter\.com/(\w+)/?$'
    return re.match(res, url)

def check_urls_validity(urls):
    url_list = urls.split(", ")
    valid_urls = []
    invalid_urls = []

    for url in url_list:
        if is_valid_twitter_url(url):
            valid_urls.append(url)
        else:
            invalid_urls.append(url)

    return valid_urls, invalid_urls


valid_urls, invalid_urls = check_urls_validity(urls)

print("Valid URLs:")
c=0
for url in valid_urls:
    print(url)
    c+=1
print("Number of valid Twitter urls : ",c)

c=0
print("\nInvalid URLs:")
for url in invalid_urls:
    print(url)
    c+=1
print("Number of invalid Twitter urls : ",c)
