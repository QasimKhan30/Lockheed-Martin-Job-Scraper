# Lockheed Martin Job Scraper

This is a Python script for scraping job postings from Lockheed Martin's careers website. It extracts various details about job listings and saves them to a CSV file for easy reference.

## Features

- Scrapes job title, location, date posted, job ID, apply link, and job description.
- Ensures that only unique job listings are saved to the CSV file.
- Allows users to input job links to save data or quit the application.

## Requirements

Before running the script, make sure you have the following libraries installed:

- `requests`
- `beautifulsoup4`
- `csv`
- `os`

## Usage

### Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/lockheed-martin-job-scraper.git
```
### Run using 
```bash
python3 job_scraper.py
```
### Details
The script will prompt you to enter job links to save data. You can enter a job link from Lockheed Martin's careers website, and the script will extract and save the job details to a CSV file. To quit the application, simply enter 'q'.

The scraped job data will be saved to a CSV file named lockheed_job_applications.csv. If the file does not exist, it will be created.

## CSV File Format
The CSV file will have the following columns:

- Job Title
- Location
- Date
- Job ID
- Apply Link
- Description

## Note
This script currently keeps track of jobs applied to only in the current session. If you want to maintain a history of all applied jobs across multiple sessions, you may need to implement additional functionality.

## Contribution
Contributions to this project are welcome. If you find any issues or have ideas for improvements, please create a pull request or open an issue on GitHub.