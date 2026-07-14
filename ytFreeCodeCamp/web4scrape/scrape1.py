#This code is generate from claude
from bs4 import BeautifulSoup
from pathlib import Path
import time

HTML_FILE = "C:\pyProject\websraping\ytFreeCodeCamp\web4scrape\index.html"      # local mock job board file
OUTPUT_DIR = Path("posts")
POLL_MINUTES = 10


def slow_write(f, text, delay=0.3):
    """Write text to file with a small delay between writes, for readability."""
    f.write(text)
    time.sleep(delay)


def find_jobs(unfamiliar_skill):
    html_text = Path(HTML_FILE).read_text(encoding="utf-8")
    soup = BeautifulSoup(html_text, "lxml")
    jobs = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")

    OUTPUT_DIR.mkdir(exist_ok=True)

    for index, job in enumerate(jobs):
        published_date = job.find("span", class_="sim-posted").span.text

        if "few" in published_date:
            company_name = job.find("h3", class_="job-list-comp-name").text.strip()
            skills = job.find("span", class_="srp-skills").text.strip()
            more_info = job.header.h2.a["href"]

            if unfamiliar_skill.lower() not in skills.lower():
                out_path = OUTPUT_DIR / f"{index}.txt"
                with open(out_path, "w", encoding="utf-8") as f:
                    slow_write(f, f"Company Name: {company_name}\n")
                    slow_write(f, f"Skills Required: {skills}\n")
                    slow_write(f, f"More Info: {more_info}\n")
                print(f"File saved: {out_path}")


if __name__ == "__main__":
    print("Put some skill that you are not familiar with")
    unfamiliar_skill = input("> ")
    print(f"Filtering out {unfamiliar_skill}")

    while True:
        find_jobs(unfamiliar_skill)
        print(f"Waiting {POLL_MINUTES} minutes...")
        time.sleep(POLL_MINUTES * 60)