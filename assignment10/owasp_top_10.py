from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://owasp.org/www-project-top-ten/")
time.sleep(5)

results = []

# Get ALL links on the page
links = driver.find_elements("tag name", "a")

for link in links:
    text = link.text.strip()
    href = link.get_attribute("href")

    # OWASP Top 10 titles always start like this
    if text.startswith("A0") or text.startswith("A10"):
        results.append({
            "Title": text,
            "Link": href
        })

# Remove duplicates and keep first 10
unique = []
seen = set()
for r in results:
    if r["Title"] not in seen:
        unique.append(r)
        seen.add(r["Title"])

results = unique[:10]

print("Number of items found:", len(results))
print(results)

pd.DataFrame(results).to_csv("owasp_top_10.csv", index=False)

driver.quit()
