from bs4 import BeautifulSoup
import requests
import time

print("Put some skill that you are not fimilar with")
unfimilar_skill = input(">")
print("Filtering out{unfimilar_skill}")

def find_job():
    html_text = requests.get("timesjob.html").text
    soup = BeautifulSoup(html_text, "lxml")
    jobs = soup.find_all("li", class_ = "clearfix job-bx wht-shd-bx")

    for index, job in enumerate(jobs):
        published_date = job.find("span", class_ = "sim-posted").span.text
        if "few" in published_date:
            company_name = job.find("h3", class_ = "clearfix job-bx wht-shd-bx").text.replace(" ", "")
            skills = job.find("span", class_ = "srp-skills").text.replace(" ", "")
            more_info = job.header.h2.a["href"]
            if unfimilar_skill not in skills:
                with open(f"posts/{index}.txt", "w") as f:
                    
                    time_wait(f"Company Name: {company_name.strip()}\n")
                    time_wait(f"Skills Required: {skils.strip()}\n")
                    time_wait(f"More Info: {more_info}")
                print("File save: {index}")


if __name__ == "__main__":
    while True:
        find_jobs()
        time_wait = 10
        print(f"Waiting {time_wait} minutes...")
        time.sleep(time_wait * 600)
        
