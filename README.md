# Competitor Webscraping 

Pull inventory details of competeing ecommerce retailers. 

## Description

Pulls all readily availible inventory data of yarn from 2 competitors.

* Lovecrafts has a custom itemloader that makes applying logic easier. 
* WEBS will use a simpler crawler.

## Getting Started

### Set Up

Clone repo
'''
git clone https://github.com/MDeanLindsay/scrapy.git
'''
Step into folder.
'''
cd Yarn/
'''
Start virtual environment.
'''
source bin/activate
'''
Pip requirements/scrapy and its dependencies.
'''
pip install -r /requirements.txt
'''

### Run

Lovecrafts crawl.
'''
scrapy crawl LoveCrafts -O testexport.json
'''
WEBS crawl.
'''
scrapy crawl WEBS -O testexport.json
'''


### Export Example

'''
{"brand": "Lion Brand", "product_type": "Yarns", "name": "Lion Brand Vanna's Choice", "details": "100% Acrylic, 3.5oz", "price": "4.9900", "shades": "33 shades"},
{"brand": "Bernat", "product_type": "Yarns", "name": "Bernat Softee Chunky", "details": "3.5oz", "price": "4.4900", "shades": "34 shades"},
{"brand": "Berroco", "product_type": "Yarns", "name": "Berroco Vintage", "details": "52% Acrylic 40% Wool 8% Nylon, 3.5oz", "price": "8.9900", "shades": "55 shades"},
{"brand": "Plymouth Yarn", "product_type": "Yarns", "name": "Plymouth Yarn Encore Worsted", "details": "75% Acrylic 25% Wool, 3.5oz", "price": "6.5000", "shades": "62 shades"},

'''

