#!/usr/bin/python3.9
import webbrowser 
from random import shuffle
from selenium import webdriver
import sys

def read_links(path: str) -> list[str]:
    with open(path) as file:
        links = list(map(lambda link: link.rstrip(), file.readlines()))
        return links

def shuffle_links(links: list[str]) -> list[str]:
    links_ = links[:]
    shuffle(links_)
    return links_

def open_links(links):
    opened_links = []
    for link in links:
        browser = webdriver.Firefox()
        browser.get(link)
        opened_links.append((browser, link))
        print(f"Opened {link}")
    for browser, link in reversed(opened_links):
        browser.close()
        print(f"Closed {link}")



def main(args):
    links = shuffle_links(read_links(args[1]))
    open_links(links)

if __name__ == "__main__":
    main(sys.argv)