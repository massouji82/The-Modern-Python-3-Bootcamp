from ebaysdk.finding import Connection as finding
from bs4 import BeautifulSoup

Keywords = ('MVS Windjammers')
api = finding(appid='MassoudV-baysearc-PRD-de46bc082-ff1a26ea', config_file=None)
api_request = {'keywords':Keywords, 'outputSelector':'SellerInfo'}

response = api.execute('findItemsByKeywords', api_request, 
		'itemFilter': [
        {'name': 'Condition', 'value': 'Used'},
        {'name': 'MinPrice', 'value': '100', 'paramName': 'Currency', 'paramValue': 'Used'},
        {'name': 'MaxPrice', 'value': '300', 'paramName': 'Currency', 'paramValue': 'USD'}
])
soup = BeautifulSoup(response.content, 'lxml')

totalentries = int(soup.find('totalentries').text)
items = soup.find_all('item')

for item in items: 
	cat = item.categoryname.string.lower() 
	title = item.title.string.lower() 
	price = int(round(float(item.currentprice.string))) 
	url = item.viewitemurl.string.lower() 

	print('________') 
	print('cat:\n' + cat + '\n')
	print('title:\n' + title + '\n') 
	print('price:\n' + str(price) + '\n') 
	print('url:\n' + url + '\n') 
input()