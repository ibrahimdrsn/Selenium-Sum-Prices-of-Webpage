
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://www.trendyol.com/sr?q=laptop&qt=laptop&st=laptop&os=1")

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "prc-box-dscntd")))

laptop_prices = driver.find_elements(By.CLASS_NAME, "prc-box-dscntd")

total_price = 0
for price in laptop_prices:
    try:
        price_value = float(price.text.replace("TL","").replace(",",".").strip())
        total_price  += price_value
    except ValueError:
        print(f"Geçersiz fiyat: {price.text}")

    print(f"Total Price for laptops in the page: {total_price}")

driver.quit()


