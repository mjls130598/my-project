from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("/home/mjesus/workspaces/test-lab/chromedriver")

try:
    driver.get("https://www.eltiempo.es/madrid.html")

    link_cookies = driver.find_element(By.XPATH, "//span[text()='ACEPTAR']")
    link_cookies.click()

    texto_temperatura = driver.find_element(By.CSS_SELECTOR, ".c-tib-text")
    temperatura = int(texto_temperatura.text[:-1])

    assert 0 < temperatura < 100

except Exception:
    driver.save_screenshot("temp/ejemplo.png") #para hacer las capturas
    raise
finally:
    driver.quit()