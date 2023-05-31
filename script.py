from selenium import webdriver

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://www.mytek.tn/")
search_btn = driver.find_element_by_id("searchbox")
search_btn.send_keys("BARRETTES MÉMOIRE")
search_btn = driver.find_element_by_class_name("btn-searchbox")
search_btn.click()
all_titles = driver.find_elements_by_class_name("product-item-link")

file = open("RAMs.txt", "w")
for title in all_titles:
    if title.text != "":
        file.writelines(f"{title.text}\n")
print("done")
