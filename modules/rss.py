from urllib.request import urlopen
import xml.etree.ElementTree as xmlParser


def getRSSLinks(url="https://football.ua/rss2.ashx"):
    rssContent = urlopen(url).read()

    links = []
    if rssContent:
        for item in xmlParser.fromstring(rssContent).findall("channel/item"):
            link = item.find("link").text
            if link:
                links.append(link)
            break  # get only the first

    return links
