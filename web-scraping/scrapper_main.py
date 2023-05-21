import os
from GoogleImageScraper import GoogleImageScraper
from patch import webdriver_executable

webdriver_path = os.path.normpath(os.path.join(os.getcwd(), 'web-scraping/chrome_driver', webdriver_executable()))
image_path = os.path.normpath(os.path.join(os.getcwd(), 'ml-engineering/Datasets/tmp'))
print(f'webdriver path : {webdriver_path}')
print(f'save image path : {image_path}')
#add new search key into array ["cat","t-shirt","apple","orange","pear","fish"]
search_keys= ["Rumah mewah","rumah miskin","Rumah pedesaan",]
number_of_images = 10
headless = False
#min_resolution = (width,height)
min_resolution=(0,0)
#max_resolution = (width,height)
max_resolution=(1920,1080)
for search_key in search_keys:
    image_scraper = GoogleImageScraper(webdriver_path,image_path,search_key,number_of_images,headless,min_resolution,max_resolution)
    image_urls = image_scraper.find_image_urls()
    image_scraper.save_images(image_urls, False)