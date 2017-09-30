from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import time


def main():
    inp = input('Enter the translation you want: Yoda, Pig, or Pirate')
    sentence = input('Enter the sentence')

    if(inp.lower()=='yoda'):
        print('Your converted sentence is '+yoda(sentence))
    elif(inp.lower()=='pig'):
        print('Your converted sentence is '+pig(sentence))
    elif(inp.lower()=='pirate'):
        print('Your converted sentence is '+pirate(sentence))

def yoda(sentence):    
    driver = webdriver.PhantomJS('phantomjs')
    driver.get("http://www.yodaspeak.co.uk/index.php")
    inputElement = driver.find_element_by_xpath('/html/body/div[6]/form/div[1]/textarea')
    inputElement.send_keys(sentence)
    driver.find_element_by_xpath('/html/body/div[6]/form/div[2]/input[1]').click()
    return driver.find_element_by_xpath('//*[@id="result"]/div[1]/span/textarea').text

def pirate(sentence):    
    driver = webdriver.PhantomJS('phantomjs')
    driver.get("http://speakpirate.com/")
    inputElement = driver.find_element_by_xpath('//*[@id="source_text_area"]')
    inputElement.send_keys(sentence)
    driver.find_element_by_xpath('//*[@id="translate_button"]/input').click()
    return driver.find_element_by_xpath('//*[@id="translated"]').text

def pig(sentence):    
    driver = webdriver.PhantomJS('phantomjs')
    driver.get("http://snowcrest.net/donnelly/piglatin.html")
    inputElement = driver.find_element_by_xpath('/html/body/div/font[1]/font/form/b[1]/textarea[1]')
    inputElement.send_keys(sentence)
    driver.find_element_by_xpath('/html/body/div/font[1]/font/form/b[1]/input[1]').click()
    time.sleep(1)
    return driver.find_element_by_xpath('/html/body/div/font[1]/font/form/b[1]/textarea[2]').text



main()


