# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# chrome_driver_path = "C:\Development\chromedriver.exe"
# service = Service(executable_path=chrome_driver_path)
# # Keep the browser open when the script finises
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)
# #driver = webdriver.Chrome(service=service, options=chrome_options)
# driver = webdriver.Chrome(service=service)
#
# # OBTENER EL PRECIO DE UN PRODUCTO DE AMAZON
# driver.get("https://www.amazon.es/dp/B075WWQY2Y?tag=dap-pivot-21&th=1")
# # Obtener el precio como entero
# price = driver.find_element(By.CLASS_NAME, "a-price-whole")
# print(f"El precio es {price.text} euros")
# # Obtener el precio completo
# price_full = driver.find_element(By.XPATH, '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[1]/span[1]')
# print(f"El precio completo es {price_full.text} euros")
#
# # OBTENER EL TAMAÑO DE UNA IMAGEN
# driver.get("https://www.python.org/")
# logo = driver.find_element(By.CLASS_NAME, "python-logo")
# print(logo.size)
#
# # BUSCAR UN ENLACE QUE NO TIENE UNA CLASE
# driver.get("https://www.python.org/")
# documentation_link = driver.find_element(By.CLASS_NAME, "documentation-widget a")
# print(documentation_link.text)
#
# # XPath
# bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

# Find elements

#driver.close()

# Challenge, crear un diccionario con los 'Upcoming Eventes' de la pagina de "https://www.python.org/"
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

URL_Python = "https://www.python.org/"

# Crear el driver
chrome_driver_path = "C:\Development\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Obtener las cosas
driver.get(URL_Python)
event_list = driver.find_elements(By.CLASS_NAME, "event-widget li a")
time_list = driver.find_elements(By.CLASS_NAME, "event-widget time")

events = {}
for n in range(len(event_list)):
    events[n] = {
        "time": time_list[n].text,
        "name": event_list[n].text,
    }
print(events)


