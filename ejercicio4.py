from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("/home/mjesus/workspaces/test-lab/chromedriver")

try:
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

    numero_veces = 20

    boton_add = driver.find_element(By.XPATH, '//button[text()="Add Element"]')
    for i in range(numero_veces):
        boton_add.click()

    numero_deletes = len(driver.find_elements(By.CSS_SELECTOR, '#elements > button'))
    for i in range(numero_deletes):
        boton_delete = driver.find_element(By.XPATH, '//button[text()="Delete"][' + str(numero_veces - i) + ']')
        boton_delete.click()

    numero_deletes = len(driver.find_elements(By.CSS_SELECTOR, '#elements button'))

    assert numero_deletes == 0

finally:
    driver.quit()


