from bs4 import BeautifulSoup
import requests

def scrape_google_results(query, num_results=10):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
    }
    url = f"https://www.google.com/search?q={query.replace(' ', '+')}&num={num_results}"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    results = []
    for g in soup.find_all("div", class_="tF2Cxc"):
        title = g.find("h3").text
        link = g.find("a")["href"]
        desc = g.find("div", class_="VwiC3b").text if g.find("div", class_="VwiC3b") else ""
        results.append({"title": title, "link": link, "desc": desc})

    return results

# Example usage
QUERY = "Python web scraping"
try:
    results = scrape_google_results(QUERY)
    for i, result in enumerate(results, start=1):
        print(f"Result {i}:")
        print(f"Title: {result['title']}")
        print(f"Link: {result['link']}")
        print(f"Discription: {result['desc']}\n")
except Exception as e:
    print(f"An error occurred: {e}")
