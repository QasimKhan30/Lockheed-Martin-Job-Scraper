import requests
from bs4 import BeautifulSoup
import csv
import os

"""
LOCKHEED MARTIN JOB PARSER
"""

# Method that gets job title (string)
def extract_job_title(job_elem):
    title_elem = job_elem.find('h1', class_='ajd_header__job-title')
    title = title_elem.text.strip()
    return title

# Method that gets job location (string)
def extract_job_location(job_elem):
    location_elem = job_elem.find('p', class_='ajd_header__location')
    location = location_elem.text.strip()
    return location


# Method that gets date when job was posted (string)
def extract_date(job_elem):
    date_elem = job_elem.find('span', class_='job-date job-info')
    date = date_elem.text.strip()[13:]
    return date
# Method that gets the unique job ID number (string)
def extract_job_ID(job_elem):
    ID_elem = job_elem.find('span', class_='job-id job-info')
    ID = ID_elem.text.strip()[8:]
    return ID

# Method that gets all information abot job including desired skills
def extract_description(job_elem):
    description_elem = job_elem.find('div', class_="ats-description ajd_job-details__ats-description")

    description = description_elem.text.strip()
    return description

# Method that gets the link to apply to the job. This is different from the link to the job posting that we provide.
def extract_apply_link(job_elem):
    link = job_elem.find('a', class_ ='ajd_btn__apply button job-apply bottom')['href']
    return link


# Create a CSV file to store the data


csv_filename = "lockheed_job_applications.csv"


saved_jobs = [] #used to keep track of all the jobs that have been applied to

file_exists = os.path.exists(csv_filename) #boolean to see if we are appending to old file or creating a new one
with open(csv_filename, 'a', newline='', encoding='utf-8') as csv_file:
        if file_exists:
        #populate jobs array with all jobs in file
        with open(csv_filename, 'r') as file:
            csv_reader = csv.DictReader(file)
    
            for row in csv_reader:
                # Assuming the column name is 'JOB ID'. Replace it with the actual column name if different
                job_id = row['Job ID']
                saved_jobs.append(job_id)
        print("Appending to: " + csv_filename)
    else:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Job Title', 'Location', 'Date', 'Job ID', 'Apply Link', 'Description'])
        print(csv_filename + " created")

        
    while True:

        #TODO
        # user provides job id and we need to mark the job as applied 
        # also need to save the date that we applied to the job

        link = input("Enter link for job to save (or 'q' to quit): ").strip()
        if link == 'q':
            break

        page = requests.get(link)
        job_soup = BeautifulSoup(page.content, "html.parser")
        if job_soup:
            
            job_id = extract_job_ID(job_soup)
            #check to make sure the csv consists of unique jobs
            if job_id in saved_jobs:
                print("Already applied to this job!")
                continue
            saved_jobs.append(job_id)
            
            title = extract_job_title(job_soup)
            location = extract_job_location(job_soup)
            date = extract_date(job_soup)
            apply_link = extract_apply_link(job_soup)
            description = extract_description(job_soup)


            csv_writer.writerow([title, location, date, job_id, apply_link,description])
            print(title + " saved!")

print(f"Job data has been saved to {csv_filename}")
