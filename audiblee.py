from selenium import webdriver
import pandas as pd 
import time
website = 'https://www.audible.com/adblbestsellers?ref_pageloadid=J6yCqalS9L1Cm3pA&ref=a_search_t1_navTop_pl0cg1c0r0&pf_rd_p=d42ea6af-6ce9-44e1-bbd5-7e2e15acab17&pf_rd_r=DMN0XZHWZ16F26T5KA85&pageLoadId=bEkYNODvZIolXHcr&ref_plink=not_applicable&creativeId=7ba42fdf-1145-4990-b754-d2de428ba482'
edge_path = 'D:\\Sajid\\Scraping\\msedgedriver.exe'
driver = webdriver.Edge(edge_path)
driver.get(website)
driver.maximize_window()
dropdown=driver.find_element_by_class_name('bc-link')
dropdown.click()
time.sleep(1)
#pagination
pagination=driver.find_element_by_xpath('//ul[contains(@class,"pagingElements")]')
pages=pagination.find_elements_by_tag_name('li')
last_page=int(pages[-2].text)
book_title=[]
author=[]
lenght=[]
curret_page=1
while curret_page<=last_page:
    try:
        container=driver.find_element_by_class_name('adbl-impression-container ')
        product=container.find_elements_by_xpath('.//li[contains(@class,"productListItem")]')
        for products in product:
            book_title.append(products.find_element_by_xpath('.//h3[contains(@class,"bc-heading")]').text)
            author.append(products.find_element_by_xpath('.//li[contains(@class,"authorLabel")]').text)
            lenght.append(products.find_element_by_xpath('.//li[contains(@class,"runtimeLabel")]').text)
    except:
        pass
    curret_page=curret_page+1
    try:
        next_page=driver.find_element_by_xpath('//span[contains(@class,"nextButton")]')
        next_page.click()
    except: 
        pass
driver.quit()
df=pd.DataFrame({'book_title':book_title,'author':author,'lenght':lenght})
df.to_csv('best.csv',index=False)