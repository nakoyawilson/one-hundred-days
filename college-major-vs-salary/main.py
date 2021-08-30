from bs4 import BeautifulSoup
import requests
import numpy
import pandas

url_list = [
    "https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors",
    "https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors/page/2",
    "https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors/page/3",
    "https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors/page/4"
]

highest_paying_jobs = []
for url in  url_list:
    response = requests.get(url)
    response.raise_for_status()
    salary_data = response.text

    soup = BeautifulSoup(salary_data, "html.parser")
    table_data = soup.find_all(class_="data-table__value")
    data_list = [data_point.get_text() for data_point in table_data]
    highest_paying_jobs.extend(data_list)

new_list = []
for item in highest_paying_jobs:
    if item.startswith("$"):
        item = item.replace("$", "")
        item = item.replace(",", "")
        new_list.append(int(item))
    else:
        new_list.append(item)

# Convert to numpy array
array = numpy.array(new_list)

#  Change  shape to a two dimensional matrix
reshaped = array.reshape(100, 6)

# Construct table
dataframe = pandas.DataFrame(reshaped,
                 columns=['Rank', 'Major', 'Degree Type', 'Early Career Pay', 'Mid-Career Pay', '% High Meaning'])

dataframe.to_csv('highest_paying_jobs_2021.csv',index=False)