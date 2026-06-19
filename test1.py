
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

create_btn = wait.until(
    EC.presence_of_element_located(
        (By.ID, "createNewMaster")
    )
)

driver.execute_script(
    "arguments[0].click();",
    create_btn
)

print("Create Generic Parameter Clicked")

time.sleep(5)

print(driver.current_url)

df = pd.read_excel(
    r"C:\Users\91010910\Downloads\Group code data 1.xlsx"
)

create_another = driver.find_element(
    By.ID,
    "create_another_master"
)

if not create_another.is_selected():
    create_another.click()
for index, row in df.iterrows():

    print(f"\nProcessing Row {index + 1}")
    print("Current URL:", driver.current_url)

    # Agar grid page par aa gaya ho toh Create page reopen karo
    if "loadColumnConfig" in driver.current_url:

        print("Returned to Grid Page. Opening Create Generic Parameter...")

        create_btn = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "createNewMaster"))
        )

        driver.execute_script(
            "arguments[0].click();",
            create_btn
        )

        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "genericCode"))
        )

        create_another = driver.find_element(
            By.ID,
            "create_another_master"
        )

        if not create_another.is_selected():
            create_another.click()

        print("Create Page Opened Again")

    summary = str(row["Summary"])

    code_match = re.search(
        r"GROUP\s*CODE\s*:\s*(.*)",
        summary,
        re.IGNORECASE
    )

    name_match = re.search(
        r"GROUP\s*NAME\s*:\s*(.*)",
        summary,
        re.IGNORECASE
    )

    desc_match = re.search(
        r"DESCRIPTION\s*:\s*(.*)",
        summary,
        re.IGNORECASE
    )

    code_value = code_match.group(1).strip() if code_match else ""
    name_value = name_match.group(1).strip() if name_match else ""
    desc_value = desc_match.group(1).strip() if desc_match else ""

    print("Code:", code_value)
    print("Name:", name_value)
    print("Desc:", desc_value)

    try:

        code_box = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.ID, "genericCode"))
        )

        name_box = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.ID, "genericName"))
        )

        desc_box = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.ID, "genericDescription"))
        )

        code_box.clear()
        code_box.send_keys(code_value)

        name_box.clear()
        name_box.send_keys(name_value)

        desc_box.clear()
        desc_box.send_keys(desc_value)

        dtype = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.ID, "Text_dTypeId"))
        )

        dtype.clear()
        dtype.send_keys("GroupName")

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//li[@username='GroupName']")
            )
        ).click()

        save_btn = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "_saveandsend"))
        )

        save_btn.click()

        print(f"Row {index + 1} submitted")

        time.sleep(3)

        print("After Save URL:", driver.current_url)

        driver.save_screenshot(f"row_{index+1}.png")

    except Exception as e:

        print(f"Failed on row {index + 1}")
        print("URL:", driver.current_url)
        print("Error:", e)

        driver.save_screenshot(f"error_row_{index+1}.png")

        raise

input("Press Enter to exit...")
driver.quit()
