from imports import requests, BeautifulSoup


def parseJobs() -> list:
    # Parse html page
    search_url = "https://www.linkedin.com/jobs/search/?f_E=1%2C2&f_TPR=r86400&f_WT=2&geoId=103644278&keywords=software%20engineer&location=United%20States"
    r = requests.get(search_url)
    soup = BeautifulSoup(r.content, "html.parser")
    mydivs = soup.find_all("div", {"class": "base-card"})

    # Add jobs to list
    jobs = []
    count = -1
    for div in mydivs:
        count += 1
        jobs.append([])
        jobs[count].append(div.find("h4").text.strip())
        jobs[count].append(
            div.find("h3", {"class": "base-search-card__title"}).text.strip()
        )
        jobs[count].append(
            div.find("span", {"class": "job-search-card__location"}).text.strip()
        )
        jobs[count].append(div.find("a", href=True)["href"])

    return jobs


jobs = parseJobs()


def create_alerts(jobs):
    messages = []
    for job in jobs:
        messages.append(
            f"{job[0]}({job[2]}) is hiring a remote {job[1]}. Submit your application here: {job[3]}."
        )

    return messages


messages = create_alerts(jobs)
