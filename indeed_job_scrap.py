from jobs_scraper import JobsScraper

country = 'IL'
# country = input("Enter Country:\n example: IL\n")
position = 'Energy'
# position = input("Enter Position:\n example: Energy\n")
location = 'Tel Aviv'
# location= input("Enter City:\n example: Tel Aviv\n")
pages = 5
# pages = int(input("Enter Number of pages to scrape:\n example: 5\n"))
max_delay = 1
# max_delay = int(input("Enter max delay for scrapping:\n example: 5\n"))
full_urls = True
# full_urls = bool(input("Show URLS?\n example: True/False\n"))
search_word = 'student'  # All letters must be lower case
# search_word = input("Enter search string:\nmust be lower case\nexample: student\n")


def set_df(the_scraper, search_key):
    df = the_scraper.scrape()
    df["title"] = df["title"].str.lower()
    df = df[df['title'].str.contains(search_key)]
    print(df)
    df = df.drop('salary', axis=1)
    df = df.reset_index(drop=True)
    return df


def create_msg_from_df(df):
    jobs = df.values  # array
    job_messages = []
    for job in jobs:
        job_title = job[0]
        location = job[1]
        company = job[2]
        description = job[3]
        job_url = job[4]
        job_message_list = [" ", "Job Title: " + job_title, " ",
                            "Location: " + location, " ",
                            "Company: " + company, " ",
                            "Description: ", description, " ",
                            "Job URL: ", " ", job_url, " ",
                            "------------------------------------", " "]
        for elem in job_message_list:
            job_messages.append(elem)
    # job_messages.append(eran_str)
    # job_message = "".join([message_head, job_message, eran_str])
    return job_messages


# Create a new JobsScraper object and perform the scraping for a given query:
scraper = JobsScraper(country=country, position=position, location=location, pages=pages, max_delay=max_delay, full_urls=full_urls)
# Format the DF:
jobs_df = set_df(the_scraper=scraper, search_key=search_word)
# Convert DF to Excel:
#file_name = " ".join(["This week", search_word, "energy jobs.xlsx"])
#jobs_df.to_excel(file_name, sheet_name='Jobs')
message_list = create_msg_from_df(jobs_df)
