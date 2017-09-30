from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import time

url = 'http://rumkin.com/tools/cipher/'
source_code = requests.get(url)
soup = BeautifulSoup(source_code.text,'lxml')
links=[]

for link in soup.find_all('a'):
    links.append(link['href'].split('.')[0])

links = links[3:8]

def affine(encrypt,inputText):
    driver = webdriver.PhantomJS('phantomjs')
    driver.get("http://rumkin.com/tools/cipher/affine.php")
    e=False
    if(encrypt.lower() == "encrypt"):
        driver.find_element_by_xpath('/html/body/table/tbody/tr[1]/td/table/tbody/tr/td[1]/div/form/p[1]/select/option[1]').click()
        e=True
    elif(encrypt.lower() == "decrypt"):
        driver.find_element_by_xpath('/html/body/table/tbody/tr[1]/td/table/tbody/tr/td[1]/div/form/p[1]/select/option[2]').click()        

    inputElement = driver.find_element_by_xpath('/html/body/table/tbody/tr[1]/td/table/tbody/tr/td[1]/div/form/p[2]/input[1]')
    inputElement.send_keys('5')
    driver.find_element_by_xpath('/html/body/table/tbody/tr[1]/td/table/tbody/tr/td[1]/div/form/p[3]/select/option[6]').click()

    inputTextElement = driver.find_element_by_xpath('/html/body/table/tbody/tr[1]/td/table/tbody/tr/td[1]/div/form/p[4]/textarea')
    inputTextElement.send_keys(inputText)
    time.sleep(1)
    text = driver.find_element_by_xpath('//*[@id="affine"]').text
    return text,e

def atbash(encrypt,inputText):
    driver = webdriver.PhantomJS('phantomjs')
    driver.get("http://rumkin.com/tools/cipher/atbash.php")
    e=False
    if(encrypt.lower() == "encrypt"):
        e=True        


    inputTextElement = driver.find_element_by_xpath('/html/body/table/tbody/tr[1]/td/table/tbody/tr/td[1]/div/form/p/textarea')
    inputTextElement.send_keys(inputText)
    time.sleep(1)
    text = driver.find_element_by_xpath('//*[@id="affine"]').text
    return text,e

def baconian(encrypt,inputText):
    driver = webdriver.PhantomJS('phantomjs')
    driver.get("http://rumkin.com/tools/cipher/baconian.php")
    e=False
    if(encrypt.lower() == "encrypt"):
        driver.find_element_by_xpath('/html/body/table/tbody/tr[1]/td/table/tbody/tr/td[1]/div/form/p[1]/select/option[1]').click()
        e=True
    elif(encrypt.lower() == "decrypt"):
        driver.find_element_by_xpath('/html/body/table/tbody/tr[1]/td/table/tbody/tr/td[1]/div/form/p[1]/select/option[2]').click()        
       

    inputTextElement = driver.find_element_by_xpath('/html/body/table/tbody/tr[1]/td/table/tbody/tr/td[1]/div/form/p[3]/textarea')
    inputTextElement.send_keys(inputText)
    time.sleep(1)
    text = driver.find_element_by_xpath('//*[@id="output"]').text
    return text,e

def base64(encrypt,inputText):
    driver = webdriver.PhantomJS('phantomjs')
    driver.get("http://rumkin.com/tools/cipher/base64.php")
    e=False
    if(encrypt.lower() == "encrypt"):
        driver.find_element_by_xpath('/html/body/table/tbody/tr[1]/td/table/tbody/tr/td[1]/div/form/p[1]/select/option[2]').click()
        e=True
    elif(encrypt.lower() == "decrypt"):
        driver.find_element_by_xpath('/html/body/table/tbody/tr[1]/td/table/tbody/tr/td[1]/div/form/p[1]/select/option[1]').click()        
       

    inputTextElement = driver.find_element_by_xpath('/html/body/table/tbody/tr[1]/td/table/tbody/tr/td[1]/div/form/p[2]/textarea')
    inputTextElement.send_keys(inputText)
    time.sleep(1)
    text = driver.find_element_by_xpath('//*[@id="output"]').text
    return text,e

def bifid(encrypt,inputText):
    driver = webdriver.PhantomJS('phantomjs')
    driver.get("http://rumkin.com/tools/cipher/bifid.php")
    e=False
    if(encrypt.lower() == "encrypt"):
        driver.find_element_by_xpath('/html/body/table/tbody/tr[1]/td/table/tbody/tr/td[1]/div/form/p[1]/select/option[1]').click()
        e=True
    elif(encrypt.lower() == "decrypt"):
        driver.find_element_by_xpath('/html/body/table/tbody/tr[1]/td/table/tbody/tr/td[1]/div/form/p[1]/select/option[2]').click()        
       

    inputTextElement = driver.find_element_by_xpath('/html/body/table/tbody/tr[1]/td/table/tbody/tr/td[1]/div/form/p[4]/textarea')
    inputTextElement.send_keys(inputText)
    time.sleep(1)
    text = driver.find_element_by_xpath('//*[@id="output"]').text
    return text,e





def main():
    try:
        while(True):
            print('The number of cyphers available')
            for link in links:
                print(link)
            print()
            typ = input('Enter the name of the encryption \n')
            encrypt = input('Enter if you want to encrypt or decrypt \n')
            inputText = input('Enter the text \n')

            text=""
            e=False
            if(typ.lower()=="affine"):
                text,e = affine(encrypt,inputText)
            elif(typ.lower()=="atbash"):
                text,e = atbash(encrypt,inputText)
            elif(typ.lower()=="baconian"):
                text,e = baconian(encrypt,inputText)
            elif(typ.lower()=="base64"):
                text,e = base64(encrypt,inputText)
            elif(typ.lower()=="bifid"):
                text,e = bifid(encrypt,inputText)
            
                
            if(e):
                print('the encrypted text is "'+text+'"\n\n')
            else:
                print('the decrypted text is "'+text+'"\n\n')
    except(KeyboardInterrupt):
        print('\n\n Thank you for your time')
main()
