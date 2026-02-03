# Task 3: Write a Program to Extract this Data

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import json
import time

# Set up Selenium driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Load the page
url = "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"
driver.get(url)

time.sleep(5)  # Allow page to fully load

# Find all search result entries
results_list = driver.find_elements(By.TAG_NAME, "li")
print("Total li elements found:", len(results_list))

results = []

# Main loop
for item in results_list:
    try:
        # Title
        title = item.find_element(By.CLASS_NAME, "title-content").text

        # Authors (may be more than one)
        authors = item.find_elements(By.CLASS_NAME, "author-link")
        author_names = [a.text for a in authors]
        author_text = "; ".join(author_names)

        # Format and Year
        format_div = item.find_element(By.CLASS_NAME, "cp-format-info")
        format_year = format_div.find_element(By.TAG_NAME, "span").text

        # Store result
        book = {
            "Title": title,
            "Author": author_text,
            "Format-Year": format_year
        }

        results.append(book)

    except:
        # Skip non-result li elements
        continue

# Create DataFrame
df = pd.DataFrame(results)
print(df)

# Task 4: Write out the data
df.to_csv("get_books.csv", index=False)

with open("get_books.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=4, ensure_ascii=False)

driver.quit()
