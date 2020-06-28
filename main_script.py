import argparse
import time
from p_acquisition import m_acquisition as mac
from p_wrangling import m_wrangling as mwr
from p_analysis import m_analysis as man
from p_reporting import m_reporting as mre

def argument_parser():
    parser = argparse.ArgumentParser(description='Specify the original path')
    parser.add_argument("-p", "--path", type=str, help='original database path', required=True)
    args = parser.parse_args()
    return args


def main(args):
    option_user = str(input('Hi Ironhacker! To start please [Enter 1 or 2]: 1. To get all countries report / 2: To get the table for a specific country: '))
    while option_user != '1' and option_user != '2':
        print(f'Opsss... you have typed and invalid option {option_user}, please try again!')
        option_user = str(input('Enter 1 or 2: '))

    time.sleep(1)
    print('Starting the process..! ')
    # acquisition
    time.sleep(1)
    df_all_raw_data = mac.load_dataset(sqlitedb_path=args.path)
    time.sleep(3)
    data_country = mac.scraping_countrycodes(URL_SCRAPING='https://countrycode.org/')
    data_country_scraping = mac.field_country(data_country)
    data_jobs_api = mac.import_data_api(df_all_raw_data)
    mac.export_results('/home/usuario/Documentos/Ironhack/Project_1_0420_JuanMunoz/data/processed', df_all_raw_data,data_country_scraping, data_jobs_api)

    # Wrangling
    df_all = mwr.merging_dataframes(df_all_raw_data, data_jobs_api, data_country_scraping)
    df_all = mwr.renaming_df(df_all)
    df_all = mwr.cleaning_data(df_all)
    country_unique_list = mwr.country_list(df_all)

    #User logic

    if option_user == '1':
        print('you selected [1], you will get the table for every country included in the dataset ')
        option_country = 'Spain'
    elif option_user == '2':
        option_country = str(input('Please enter the country where you want to receive the report: '))
        while option_country not in country_unique_list:
            print(f'Opsss... {option_country} is not available in the current dataframe, please try again!')
            option_country = str(input('Enter the country once again: '))

    # Analysis
    time.sleep(0.5)
    df_answer_against = man.quest_arg_against(df_all)
    df_answer_for = man.quest_arg_for(df_all)
    df_all_countries_agegroup = man.results_all_countries_agegroup(df_all)
    df_age_group_unemployment = man.results_age_group_unemployment(df_all)
    df_age_unemployment = man.results_age_unemployment(df_all)
    df_by_country_age_group = man.results_by_country_agegroup(df_all,option_country)

    # Reporting, Exporting & Mailing
    time.sleep(3)
    mre.export_final_results('/home/usuario/Documentos/Ironhack/Project_1_0420_JuanMunoz/data/results',df_all_countries_agegroup,df_by_country_age_group,df_answer_for,df_answer_against,option_country,df_all)
    time.sleep(3)
    to_address = str(input('Enter your e-mail to receive the final report...: '))
    mre.sending_email(to_address,option_user,option_country)
    time.sleep(1)
    print('Enjoy the report, but before leaving did you know....')
    time.sleep(1)
    print('-----------------------------------------------------------------------------------------------------------')
    print('The following dataframe will show the unemployment rate by age group ')
    print(df_age_group_unemployment)
    print(df_age_unemployment)
    time.sleep(3)
    print('-----------------------------------------------------------------------------------------------------------')
    time.sleep(1)
    print('The following dataframe will show you the % of answers against: ')
    print(df_answer_against)
    time.sleep(3)
    print('-----------------------------------------------------------------------------------------------------------')
    time.sleep(3)
    print('The following dataframe will show you the % of answers for: ')
    print(df_answer_for)
    time.sleep(2)
    print('-----------------------------------------------------------------------------------------------------------')
    time.sleep(3)
    print('Juan Muñoz - Data Part Time Ironhack 2020')

if __name__ == '__main__':
    arguments = argument_parser()
    main(arguments)


