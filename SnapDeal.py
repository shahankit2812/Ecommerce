from selenium import webdriver
from bs4 import BeautifulSoup
import time


driver = webdriver.Firefox()
driver.get("http://www.snapdeal.com/")
driver.find_element_by_id("keyword").click()
driver.find_element_by_id("keyword").clear()
driver.find_element_by_id("keyword").send_keys("mobile phones")
driver.find_element_by_id("searchBtn").click()
driver.find_element_by_class_name("fnt14").click()



# #url = Request('http://www.snapdeal.com/product/apple-iphone-5c-32-gb/1253041810', headers={'User-Agent': 'Mozilla/5.0'})
# url = driver.current_url
# response = urllib.request.urlopen(url)
# data = response.read()
for i in range(1,20):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)

source=driver.page_source
soup=BeautifulSoup(source)

    #Ankit S method
    #productTitle=soup.select("div.pdpName")[0].text.strip()
    #price=soup.select("span#selling-price-id")[0].text
    #reviews=soup.select("span.average")[0].text

    #Ankit A method
productTitle = soup.find_all('div', attrs={'class': 'product-title'})
for div in productTitle:
    print(div.getText().strip())

# price = soup.find_all('div', attrs={'class': 'product-price'})
# for p in price:
#     rupees =p.contents[1]
#     r=rupees.contents[0]
#     print(r.strip())
price=driver.find_elements_by_xpath('/html/body/div[1]/div[6]/div[1]/div[5]/div[2]/div/div/div[4]/div[3]/a/div[2]/div[1]')
for amount in price:
    print (amount.text)

rating = soup.find_all('div', attrs={'class': 'ratingsWrapper'})
for rat in rating:
    review = rat.contents[1]
    if review.has_attr('ratings'):
        print(review.attrs['ratings'])