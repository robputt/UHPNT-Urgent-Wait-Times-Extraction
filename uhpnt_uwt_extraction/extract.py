import logging
import requests

from bs4 import BeautifulSoup


logging.basicConfig(encoding='utf-8', level=logging.DEBUG)


def fetch_data(
        url='https://www.plymouthhospitals.nhs.uk/urgent-waiting-times'
):
    logging.info("Fetching data from UHPNT website")
    response = requests.get(url, verify=False)
    return response.text


def extract_data(content):
    logging.info("Extracting wait time data")
    soup = BeautifulSoup(content, "lxml")
    raw = soup.find_all("span", {"class": "data-number"})
    return {
        'longest_wait_time': int(raw[0].text),
        'patients_waiting': int(raw[1].text),
        'patients_in_department': int(raw[2].text)
    }


def main():
    logging.info("Extracting UHPNT Urgent Wait Times")
    content = fetch_data()
    data = extract_data(content)
    print(data)


if __name__ == '__main__':
    main()
