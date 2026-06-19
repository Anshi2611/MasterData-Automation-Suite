from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import re

service = Service(
    r"C:\Users\91010910\Desktop\chromedriver\chromedriver.exe"
)

driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get(
    ..
)

# Login details
driver.find_element(
    By.ID,
    "username"
).send_keys("")

driver.find_element(
    By.ID,
    "password-entry"
).send_keys("")

print("Waiting for dashboard...")

wait = WebDriverWait(driver, 120)

buttons = wait.until(
    EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, "a.btn.module-btn")
    )
)

print("Login Done")

# Dashboard buttons ka wait
wait = WebDriverWait(driver, 30)

buttons = wait.until(
    EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, "a.btn.module-btn")
    )
)

print("Buttons found:", len(buttons))

for i, btn in enumerate(buttons):
    print(i, btn.text, btn.get_attribute("onclick"))

# Common Masters = third button
buttons[2].click()

time.sleep(5)

print("Tabs:", driver.window_handles)
print("Current URL:", driver.current_url)

# Agar new tab open hua ho
if len(driver.window_handles) > 1:
    driver.switch_to.window(driver.window_handles[-1])
    print("After Switch:", driver.current_url)

# Hamburger menu click
menu_btn = wait.until(
    EC.element_to_be_clickable(
        (By.ID, "menuClick")
    )
)

menu_btn.click()

time.sleep(2)

# Search box
search_box = wait.until(
    EC.element_to_be_clickable(
        (By.ID, "textMenuListSearch")
    )
)

search_box.clear()
search_box.send_keys("Seed Data")

time.sleep(2)

seed_data = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            "//a[contains(@class,'searchedMenu') and contains(text(),'Seed Data')]"
        )
    )
)

seed_data.click()

print("Seed Data Clicked")

time.sleep(5)

print("Current URL:", driver.current_url)

print(driver.current_url)

print("Seed Data searched")
print("Before Rows")
rows = driver.find_elements(
    By.XPATH,
    "//table[@id='GenericParameter']//tbody/tr"
)
print("After Rows")
print("Rows:", len(rows))

print("Before Excel Read")


try:
    df = pd.read_excel(
        r"C:\Users\91010910\Downloads\Group code data 1.xlsx"
    )

    print("Excel Loaded Successfully")

except Exception as e:
    print("Excel Error:", e)
print("Excel Loaded Successfully")
print("Columns:", df.columns.tolist())
print("Total Rows:", len(df))

for index, row in df.iterrows():

    summary = str(row["Summary"])

    code_match = re.search(
        r"GROUP\s*CODE\s*:\s*(.*)",
        summary,
        re.IGNORECASE
    )

    if not code_match:
        print(f"Row {index+1}: Code not found")
        continue

    code_value = code_match.group(1).strip()

    print(f"\nSearching ({index+1}/{len(df)}): {code_value}")

    search_box = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (
                By.CSS_SELECTOR,
                "input[type='search'][aria-controls='GenericParameter']"
            )
        )
    )

    search_box.clear()
    search_box.send_keys(code_value)

    time.sleep(2)

    rows = driver.find_elements(
        By.XPATH,
        "//table[@id='GenericParameter']//tbody/tr"
    )

    print("Rows Found:", len(rows))

    if rows:

        print("Matched Row:")
        print(rows[0].text)

        approve_btn = rows[0].find_element(
            By.XPATH,
            ".//img[@title='Approve']"
        )

        driver.execute_script(
            "arguments[0].click();",
            approve_btn
        )

        print("Approve Clicked")

        time.sleep(2)

    else:
        print("No Match Found")
input("press enter to quit")
driver.quit()

