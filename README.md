# XSS Scanner

XSS Scanner is a simple Python script to detect Cross-Site Scripting (XSS) vulnerabilities in web applications. This tool takes a list of URLs and a set of XSS payloads as input and tests each URL with various payloads to identify potential vulnerabilities.

## Features

- Scan multiple URLs for XSS vulnerabilities.
- Utilizes a list of customizable XSS payloads.
- Provides a colorful ASCII art header.

## Prerequisites

Before using the XSS Scanner, you need to have the following dependencies installed:

- Python 3
- Required Python packages (install them using `pip`):
  - `requests`
  - `art`
  - `termcolor`

You can install the required Python packages by running:

```shell
pip install -r requirements.txt
```

## Usage

To use the XSS Scanner, run the script with the `-h` or `--help` option to see all available options and usage examples:

python xss_scanner.py -l urls.txt -p payloads.json

-l or --file: Path to the file containing URLs to scan.
-p or --payloads: Path to the JSON file containing XSS payloads.

## Interpreting Results:

The tool will test each URL with various payloads and display whether a URL is vulnerable to XSS or not.

## Author

Givari Hertz
Twitter: @gh3rtz
Instagram: @givarirmdn
Feel free to reach out to the author for feedback or questions.
