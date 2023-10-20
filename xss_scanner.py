import argparse
import requests
import json
from art import text2art
from termcolor import colored


# ASCII art for "Givari Hertz"
ascii_art = text2art("XSS Scanner")
instagram_handle = "Twitter: @gh3rtz    Instagram: @givarirmdn"

# Print the ASCII art and Instagram handle in green color
print(colored(ascii_art, "green"))
print(colored(instagram_handle, "green"))

def check_xss_vulnerability(url, xss_payload):
    try:
        response = requests.get(url, params={"param": xss_payload})
        if xss_payload in response.text:
            print(colored(f"[VULN] {url} is vulnerable to XSS", 'red'))
        else:
            print(colored(f"[NOT VULN] {url} is not vulnerable to XSS", 'green'))
    except Exception as e:
        print(f"[ERROR] {url} - {str(e)}")

def main():
    try:
        parser = argparse.ArgumentParser(description="Cross-Site Scripting (XSS) Scanner")
        parser.add_argument("-l", "--file", help="File with a list of URLs to test", required=True)
        parser.add_argument("-p", "--payloads", help="JSON file containing XSS payloads", required=True)
        args = parser.parse_args()

        with open(args.file, "r") as file:
            urls = file.read().splitlines()

        with open(args.payloads, "r") as payload_file:
            payload_data = json.load(payload_file)
            payloads = payload_data["payloads"]

        for url in urls:
            for payload in payloads:
                check_xss_vulnerability(url.replace("FUZZ", payload), payload)
    except KeyboardInterrupt:
        print("XSS scanning completed.")

if __name__ == "__main__":
    main()
