#!/usr/bin/python3.9
from random import shuffle
from selenium import webdriver
from more_itertools import windowed
import sys

from selenium.webdriver.remote.webelement import WebElement

metric_names = ["Всего символов:", "Всего слов:", "Уникальных слов:"]
expected_metrics = {'Всего символов:': 11, 'Всего слов:': 3, 'Уникальных слов:': 3}

def test_text():
    return "lol kek top"

def test_word_counter():
    browser = webdriver.Firefox()
    browser.get("http://simvoli.net/")
    textarea: WebElement = browser.find_element_by_id("textarea")
    textarea.send_keys(test_text())
    browser.find_element_by_class_name("sibut").click()
    result_div: WebElement = browser.find_element_by_id("result_div")
    result_items = list(windowed(map(lambda x: x.text, result_div.find_elements_by_css_selector("u")), 2))
    browser.close()
    metrics = { m: None for m in metric_names}
    for metric, value in result_items:
        if metric in metric_names:
            metrics[metric] = int(value)
    if metrics == expected_metrics:
        print("Test passed")
    else:
        print(f"Test failed, expected\n{expected_metrics}\nbut actual:\n{metrics}")


def main(args):
    test_word_counter()

if __name__ == "__main__":
    main(sys.argv)