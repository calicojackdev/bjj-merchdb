import csv
import json
import time
import logging
import requests


data_file_path = "../data/input.csv"
backup_file_path = "../data/backup/input.csv"
field_names = ["brand","brand_url","gi","gi_url","rashguard","rashguard_url","shorts","shorts_url","belt","belt_url","tags"]
urls_to_check = ["gi_url", "rashguard_url", "shorts_url", "belt_url"]

def backup_data(input_file_path: str, backup_file_path: str) -> None:
    """ copy input csv to backup dir"""

    with open(input_file_path, mode="r") as input_file:
        reader = csv.reader(input_file)
        data = list(reader)
    
    with open(backup_file_path, mode="w", newline="") as backup_file:
        writer = csv.writer(backup_file)
        writer.writerows(data)

def update_data(file_path: str, data: list) -> None:
    """ update data file with healthy links """

    with open(file_path, mode="w", newline="") as data_file:
        writer = csv.DictWriter(data_file, field_names)
        writer.writeheader()
        writer.writerows(data)
    return

def get_data(file_path: str) -> csv.DictReader:
    """ get input data """

    with open(file_path, mode="r") as data_file:
        data = csv.DictReader(data_file)
        data = list(data)
    return data

def get_pulse(url: str) -> bool:
    """ make request to a url and check for 200 OK """

    time.sleep(1)
    if url:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return True
            else:
                print(f"non 200 status code found for {url}")
                return False
        except requests.exceptions.ConnectionError:
            print(f"ConnectionError on {url}")
    return False

def check_health(data: csv.DictReader) -> list: 
    """ iterate through links and blank if bad request """

    for site in data[:10]:
        print(f"brand: {site['brand']}")
        for url in urls_to_check:
            print(f"checking {url}")
            link_healthy = get_pulse(site[url])
            if not link_healthy and site[url]:
                print(f"blanking value for {site[url]}") # log instead
                site[url] = ""
    return data

backup_data(data_file_path, backup_file_path)
data = get_data(data_file_path)
healthy_data = check_health(data)
update_data(data_file_path, healthy_data)