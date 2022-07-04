import logging
import requests


logging.basicConfig(encoding='utf-8', level=logging.DEBUG)


def fetch_data(
        url='https://www.plymouthhospitals.nhs.uk/urgent-waiting-times'
):
    logging.info("Fetching data from UHPNT website")
    response = requests.get(url, verify=False)
    return response.text


def main():
    logging.info("Extracting UHPNT Urgent Wait Times")
    content = fetch_data()
    print(len(content))


if __name__ == '__main__':
    main()
