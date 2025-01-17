from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Crear el driver
chrome_driver_path = "C:\Development\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
# Keep browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Obtener el numero de articulos en la wikipedia
URL_Wikipedia = "https://en.wikipedia.org/wiki/Main_Page"
driver.get(URL_Wikipedia)

article_count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
print(f"Welcom to Wikipedia, the free encyclopedia that anyone can edit. {article_count.text} articles in English")

# Click on the element
#article_count.click()

#all_portals = driver.find_element(By.LINK_TEXT, "Pages")
#all_portals.click()

search = driver.find_element(By.NAME, "search")
search.send_keys("Gallipienzo")
search.send_keys(Keys.ENTER)


# Challenge (No funciona la pagina web)
driver.get("https://web.archive.org/web/20220120120408/https://secure-retreat-92358.herokuapp.com/")
first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Angela")
last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Yu")
email = driver.find_element(By.NAME, "email")
email.send_keys("angela@gmail.com")

submit = driver.find_element(By.CSS_SELECTOR, "form button")
submit.click()
