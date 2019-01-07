# Simple-Python3-Google-Search
Simple google search with python and bs4

With this code you can make a simple google search without using its API, just using python3 libraries. It is still very simple but soon i'll implement others functionalities. 

This may also present some problems in specific searchs but I'm working on it.

## How to use

All you need to do is call the function 'search' and send as parameters the term you want to search and the number of results you desire. ***OBS: it only returns at maximum 9 results per search***

## Dependencies

#### Requests library

If you don't have it, you can install with 

```
pip3 install requests
```

Or you can download at https://pypi.org/project/requests/

#### BeaultifulSoup4

This is used to scrap the result page. 

If you’re using a recent version of Debian or Ubuntu Linux, you can install Beautiful Soup with the system package manager:

```
apt-get install python3-bs4
```

If you can't, follow the steps at https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup

## Example

Calling the function

```
import sgs
s = sgs.Google.search("Github", 9)
for r in s:
	print(r)
```

Result

```
https://github.com/
https://github.com/github
https://github.com/features
https://github.com/explore
https://github.com/join
https://desktop.github.com/
https://github.com/features/code-review/
https://pt.wikipedia.org/wiki/GitHub
https://en.wikipedia.org/wiki/GitHub
https://github.community/
```
