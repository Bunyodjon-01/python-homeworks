## weather
from bs4 import BeautifulSoup

with open("weather.html", "r", encoding = "utf-8") as file:
    content = file.read()
    soup = BeautifulSoup(content, "html.parser")
    # print(soup)
rows = soup.find("tbody").find_all("tr")
data = []
for row in rows:
    cols = row.find_all("td")
    day = cols[0].text
    temperature = cols[1].text
    condition = cols[2].text
    data.append((day, temperature, condition))
for day, temperature, condition in data:
    print(f"on {day} temperature is {temperature} and weather condition is {condition}")
max_value = -float("inf")
for day, temperature, condition in data:
    temp = float(temperature.replace("°C", ""))

    if temp > max_value:
        max_value = temp
        mday = day
print("the highest temperature: ", max_value)
print("day: ", mday)

sdays = []
for day, temperature, condition in data:
    if condition == "Sunny":
        sday = day
        sdays.append(sday)
for d in sdays:
    print(f"{d} is sunny day")
temps = []
for day, temperature, condition in data:
    temp = float(temperature.replace("°C", ""))
    temps.append(temp)
avg = sum(temps)/len(temps)
print(f"average temperature is {avg}")


import requests
import sqlite3
from bs4 import BeautifulSoup

# --- Scraping ---
url = "https://realpython.github.io/fake-jobs"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
job_elements = soup.find("div", id="ResultsContainer").find_all("div", class_="card-content")

jobs = []
for job_elem in job_elements:
    title = job_elem.find("h2", class_="title").text.strip()
    company = job_elem.find("h3", class_="company").text.strip()
    location = job_elem.find("p", class_="location").text.strip()
    link = job_elem.find("a")["href"]

    jobs.append({"title": title, "company": company, "location": location, "link": link})

# --- Database ---
conn = sqlite3.connect("fake_jobs.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    company TEXT,
    location TEXT,
    link TEXT,
    UNIQUE(title, company, location)
)
""")
conn.commit()

# --- Incremental load + update tracking ---
for job in jobs:
    cursor.execute("""
        SELECT link FROM jobs 
        WHERE title = ? AND company = ? AND location = ?
    """, (job["title"], job["company"], job["location"]))

    result = cursor.fetchone()

    if result is None:
        # Job mavjud emas → insert
        cursor.execute("""
            INSERT INTO jobs (title, company, location, link)
            VALUES (?, ?, ?, ?)
        """, (job["title"], job["company"], job["location"], job["link"]))
        print(f"Inserted: {job['title']}")
    
    else:
        # Job mavjud → link o‘zgargan bo‘lsa update
        old_link = result[0]
        if old_link != job["link"]:
            cursor.execute("""
                UPDATE jobs
                SET link = ?
                WHERE title = ? AND company = ? AND location = ?
            """, (job["link"], job["title"], job["company"], job["location"]))
            print(f"Updated: {job['title']}")

conn.commit()
conn.close()

import sqlite3
import csv

def export_jobs_to_csv(filter_by=None, filter_value=None, filename="filtered_jobs.csv"):
    """
    Export jobs from database to CSV with optional filtering.
    
    filter_by: "location" or "company"
    filter_value: string to match
    filename: output CSV file
    """
    
    conn = sqlite3.connect("fake_jobs.db")
    cursor = conn.cursor()
    
    # --- Query construction ---
    if filter_by in ("location", "company") and filter_value:
        cursor.execute(f"""
            SELECT title, company, location, link 
            FROM jobs
            WHERE {filter_by} LIKE ?
        """, (f"%{filter_value}%",))
    else:
        cursor.execute("SELECT title, company, location, link FROM jobs")
    
    jobs = cursor.fetchall()
    conn.close()
    
    # --- Export to CSV ---
    with open(filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Title", "Company", "Location", "Link"])  # header
        writer.writerows(jobs)
    
    print(f"{len(jobs)} jobs exported to {filename}.")

# --- Examples ---
# export_jobs_to_csv(filter_by="location", filter_value="AA")  # location bo'yicha filter
# export_jobs_to_csv(filter_by="company", filter_value="Payne")  # company bo'yicha filter
export_jobs_to_csv()  # filtersiz, hammasini export qiladi

## task3

import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# ChromeDriverManager'siz ishga tushirish
driver = webdriver.Chrome() 

# Qolgan kodlar...
driver.get("https://www.demoblaze.com/")

def scrape_laptops():
    try:
        # 1. Saytga kirish
        driver.get("https://www.demoblaze.com/")
        wait = WebDriverWait(driver, 10)

        # "Laptops" bo'limini bosish
        laptops_category = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Laptops")))
        laptops_category.click()
        
        # Ma'lumotlar yuklanishi uchun biroz kutish
        time.sleep(5)

        # 2. "Next" tugmasini bosish (Keyingi sahifaga o'tish)
        next_button = wait.until(EC.element_to_be_clickable((By.ID, "next2")))
        next_button.click()
        
        # Ikkinchi sahifa elementlari yuklanishini kutish
        time.sleep(5)

        # 3. Ma'lumotlarni yig'ish
        laptop_items = driver.find_elements(By.CLASS_NAME, "card-block")
        laptops_data = []

        for item in laptop_items:
            try:
                name = item.find_element(By.CLASS_NAME, "card-title").text
                price = item.find_element(By.TAG_NAME, "h5").text
                description = item.find_element(By.ID, "article").text
                
                laptops_data.append({
                    "name": name,
                    "price": price,
                    "description": description.replace("\n", " ")
                })
            except Exception as e:
                continue

        # 4. JSON formatida saqlash
        with open('laptops.json', 'w', encoding='utf-8') as f:
            json.dump(laptops_data, f, indent=4, ensure_ascii=False)
        
        print(f"Muvaffaqiyatli yakunlandi! {len(laptops_data)} ta laptop saqlandi.")

    finally:
        driver.quit()

if __name__ == "__main__":
    scrape_laptops()