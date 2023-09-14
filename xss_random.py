import requests
import urllib.parse
import base64
import random
import string
import multiprocessing
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Function to generate random upper and lower case variations of a string
def random_case(string):
    return ''.join(random.choice([c.lower(), c.upper()]) for c in string)

# Function to test a URL with a payload
def test_url(url, payload):
    try:
        # Send a GET request with the payload
        response = requests.get(url + payload)
        
        # Check if the payload is present in the response content
        if payload in response.text:
            return True
    except Exception as e:
        pass

    return False

# Function to test URL with various payloads and encodings
def detect_xss(url, payloads):
    for payload in payloads:
        # Test the original payload
        if test_url(url, payload):
            print(f"{Fore.RED}Vulnerable to XSS: {url} with payload: {Fore.GREEN} {payload}{Style.RESET_ALL}")
        
        # Test URL-encoded payload
        url_encoded_payload = urllib.parse.quote(payload)
        if test_url(url, url_encoded_payload):
            print(f"{Fore.RED}Vulnerable to XSS (URL-encoded): {url} with payload: {Fore.GREEN} {url_encoded_payload}{Style.RESET_ALL}")

        # Test base64-encoded payload
        base64_payload = base64.b64encode(payload.encode()).decode()
        if test_url(url, base64_payload):
            print(f"{Fore.RED}Vulnerable to XSS (Base64-encoded): {url} with payload: {Fore.GREEN} {base64_payload}{Style.RESET_ALL}")

        # Test random case payload
        random_case_payload = random_case(payload)
        if test_url(url, random_case_payload):
            print(f"{Fore.RED}Vulnerable to XSS (Random Case): {url} with payload:  {Fore.GREEN}{random_case_payload}{Style.RESET_ALL}")

# Read payloads from a file
def read_payloads_from_file(file_path):
    payloads = []
    try:
        with open(file_path, 'r') as file:
            payloads = [line.strip() for line in file.readlines()]
    except Exception as e:
        print(f"Error reading payloads from file: {e}")
    return payloads

# Read target URLs from a file
def read_targets_from_file(file_path):
    targets = []
    try:
        with open(file_path, 'r') as file:
            targets = [line.strip() for line in file.readlines()]
    except Exception as e:
        print(f"Error reading target URLs from file: {e}")
    return targets

# Function to test URLs concurrently with multiprocessing
def test_urls_concurrently(targets, payloads, num_processes):
    with multiprocessing.Pool(processes=num_processes) as pool:
        pool.starmap(detect_xss, [(target, payloads) for target in targets])

# Example usage
if __name__ == "__main__":
    target_file_path = input("Enter the path to the target URL file: ")
    payload_file_path = input("Enter the path to the payload file: ")
    num_processes = int(input("Enter the number of processes to use: "))

    targets = read_targets_from_file(target_file_path)
    payloads = read_payloads_from_file(payload_file_path)

    print(f"{Fore.GREEN}Testing target URLs for XSS vulnerabilities using {num_processes} processes:{Style.RESET_ALL}")
    test_urls_concurrently(targets, payloads, num_processes)
