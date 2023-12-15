import requests
from bs4 import BeautifulSoup
import pandas

def tshirt(page):
    url = f"https://www.flipkart.com/clothing-and-accessories/topwear/tshirt/men-tshirt/pr?sid=clo,ash,ank,edy&otracker=categorytree&otracker=nmenu_sub_Men_0_T-Shirts={page}"    
    r = requests.get(url)
    # return r.status_code
    
    # create content of website into html formate
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

# extract various itwm form the website from this function
def extrat(soup):
    divs = soup.find_all('div', class_ = '_1xHGtK _373qXS')
    # return len(divs)
    for items in divs:
        title = items.find('a', class_ = 'IRpwTa').text
        # print(title)
        
        company = items.find('div', class_ = '_2WkVRV').text
        # print(company)
        
        try:
            c_price = items.find('div', class_ ='_30jeq3').text.replace('₹', '')
        except:
            c_price = ''
        # print(c_price) 
           
        try:
            p_price = items.find('div', class_ ="_3I9_wc").text.replace('₹', '')   
        except:
            p_price = ''
        # print(p_price) 
            
        try:
            discount = items.find('div', class_ ="_3Ay6Sb").span.text.replace(' off', '')
        except:
            discount = ''
        # print(discount) 
        
         
        
        tshirt_con = {
            'Product Name' : title,
            'Company Name': company,
            'Current Price': c_price,
            'Dicounted Price': discount,
            'Old Price': p_price,            
        }
        tshirt_list.append(tshirt_con)
             
            
       
            
        
    return

# list created for item storage
tshirt_list = []





# for 1 to 6 page data will be show below:
for i in range(1,6):
    print('Total Page',i)
    c = tshirt(1) 
    extrat(c) 

# use pandas for csv file
data_frame = pandas.DataFrame(tshirt_list)
data_frame.to_csv('Tshirts.csv')  
     
  




       
    
        
        




