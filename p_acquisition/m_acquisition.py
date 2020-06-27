import pandas as pd
from sqlalchemy import create_engine
import requests
from bs4 import BeautifulSoup
import time


#load dataset
def load_dataset(sqlitedb_path):
    time.sleep(1)
    print('Uploading raw data base')
    sqlitedb_path = '/home/usuario/Documentos/Ironhack/Project_1_0420_JuanMunoz/data/raw/raw_data_project_m1.db'
    engine = create_engine(f'sqlite:///{sqlitedb_path}')

    query_all = """SELECT * FROM career_info cif  
    inner join poll_info pif on cif.uuid = pif.uuid  
    inner join country_info ci on ci.uuid = pif.uuid 
    inner join personal_info pi on pi.uuid = ci.uuid"""

    df_all_raw_data = pd.read_sql_query(query_all, engine)
    df_all_raw_data[0:10]
    time.sleep(2)
    print("Database raw_data_project_m1.db has been uploaded successfully!")
    time.sleep(2)
    print('Raw Dataframe Shape \n - rows: {} \n - columns: {}'.format(df_all_raw_data.shape[0], df_all_raw_data.shape[1]))
    #print('RAW DATAFRAME NULLS COUNT: \n{}'.format(df_all_raw_data.isnull().sum()), '\n')
    #print('RAW DATAFRAME % NULLS:')
    #print(df_all_raw_data.isnull().sum() / len(df_all_raw_data) * 100)
    print('-----------------------------------------------------------------------------------------------------------')
    return df_all_raw_data

def import_data_api(df_all_raw_data):
    time.sleep(3)
    import json
    list_api = []
    list_job_codes = set(df_all_raw_data['normalized_job_code'])
    list_job_codes_2 = list(list_job_codes) #just downloading five codes to not be blocked by the api
    list_job_codes_2 = list_job_codes_2[0:10] #just downloading five codes to not be blocked by the api
    print('Connecting to http://api.dataatwork.org ')
    time.sleep(4)
    print('Api connected..!')
    time.sleep(2)
    #WARNING FOR THE REAL TEST NEED TO CHANGE list_job_codes2 by list_job_codes
    count = 0
    for i in list_job_codes_2:
        print(f'Downloading the job code: {i}...')
        url = f'http://api.dataatwork.org/v1/jobs/{i}'
        response = requests.get(url)
        results_jobs = response.json()
        list_api.append(results_jobs)
        count += 1
    print(f'Api has downloaded:  {count} jobs successfully!')
    data_jobs = pd.DataFrame(list_api)
    data_jobs = data_jobs.rename(columns={'uuid': 'normalized_job_code'})
    data_jobs_api = data_jobs[['normalized_job_code', 'title', 'normalized_job_title']]
    #print('DATAFRAME JOBS WITH TITLE SHAPE \n - rows: {} \n - columns: {}'.format(data_jobs_api.shape[0],data_jobs_api.shape[1]), '\n')
    print('-----------------------------------------------------------------------------------------------------------')
    time.sleep(3)
    return data_jobs_api

def scraping_countrycodes(URL_SCRAPING):
    URL_SCRAPING = 'https://countrycode.org/'
    print(f'Scraping process from {URL_SCRAPING} is about to start....')
    time.sleep(2)
    html = requests.get(URL_SCRAPING).content

    # lxml is the parsing module
    soup = BeautifulSoup(html, 'lxml')
    soup.contents[0:5]
    table = soup.find_all('table', {'class': 'table table-hover table-striped main-table'})[0]

    # tr represent the table rows
    rows = table.find_all('tr')
    rows_parsed = [row.text for row in rows]
    rows_parsed
    row_list = [i.strip('\n').split('\n') for i in rows_parsed]

    colnames = ['country_name', 'code_c', 'iso_codes', 'population', 'area_km2', 'gpd_usd']
    data = row_list[1:]
    data_country = pd.DataFrame(data, columns=colnames)
    print('Scraping has ended succesfully and is now stored in data_country dataframe')
    print('-----------------------------------------------------------------------------------------------------------')
    return data_country

def country_codes(x):
    return x[0:2]

def field_country(data_country):
    data_country['country_code'] = data_country['iso_codes'].apply(country_codes)
    data_country_scraping = data_country[['country_code', 'country_name', 'population']]

    return data_country_scraping

def export_results(path_to,df_all_raw_data,data_country_scraping,data_jobs_api):
    path_to = '/home/usuario/Documentos/Ironhack/Project_1_0420_JuanMunoz/data/processed'
    df_all_raw_data.to_csv(f'{path_to}/df_all_raw_data.csv', index=False, header=True, sep=';')
    data_country_scraping.to_csv(f'{path_to}/data_country_scraping.csv', index=False, header=True, sep=';')
    data_jobs_api.to_csv(f'{path_to}/data_jobs_api.csv', index=False, header=True, sep=';')





