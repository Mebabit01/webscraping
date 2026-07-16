#https://mebabit.github.io/forScraping/
from bs4 import BeautifulSoup
import requests
import time

print("Put some skills that you are not fimilar")
unfimilar_skill = input(">")
print(f"Filtering out {unfimilar_skill}")

def find_job():
    html_text = requests.get("https://mebabit.github.io/forScraping/").text
    soup = BeautifulSoup(html_text, "lxml")
    jobs = soup.find_all("li", class_ = "clearfix job-bx wht-shd-bx")
    for index, job in enumerate(jobs):
        published_date = job.find("span", class_ = "sim-posted").span.text
        if "few" in published_date:
            company_name = job.find("h3", class_ = "job-list-comp-name").text.replace(" ", "")
            skills = job.find("span", class_ = "srp-skills").text.replace(" ", "")
            more_info = job.header.h2.a["href"]
            if unfimilar_skill not in skills:

                with open(f"postsr/{index}.txt", "w") as f:
                    f.write(f"Company name: {company_name}\n")
                    f.write(f"Required Skills: {skills}\n")
                    f.write(f"More Info: {more_info}")
                print(f"File saved {index}")


if __name__ == "__main__":
    while True:
        find_job()
        time_wait = 10
        print(f"Waiting {time_wait} minute...")
        time.sleep(600)
        
