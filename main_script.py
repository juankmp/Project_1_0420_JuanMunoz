import argparse
import time
from p_acquisition import m_acquisition as mac
from p_wrangling import m_wrangling as mwr
from p_analysis import m_analysis as man
from p_reporting import m_reporting as mre

def argument_parser():
    parser = argparse.ArgumentParser(description='Specify the original path')
    parser.add_argument("-p", "--path", type=str, help='original database path', required=True)
    parser.add_argument("-u", "--user_name", type=str, help='User name', required=True)
    args = parser.parse_args()
    return args


def main(args):
    #User needs
    option_user = str(input(f'Hi {args.user_name} ! To start please [Enter 1 or 2]: 1. To get all countries report / 2: To get the table for a specific country: '))
    while option_user != '1' and option_user != '2':
        print(f'Opsss {args.user_name}... you have typed and invalid option {option_user}, please try again!')
        option_user = str(input('Enter 1 or 2: '))

    time.sleep(1)
    print(f'{args.user_name} the process is starting..!! ')
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
        print(f'{args.user_name} you have selected [1], you will get the table for every country included in the dataset ')
        option_country = 'Spain'
    elif option_user == '2':
        option_country = str(input(f'{args.user_name} please enter the country where you want to receive the report: '))
        while option_country not in country_unique_list:
            print(f'Opsss... {option_country} is not available in the current dataframe, please try again!')
            option_country = str(input(f'{args.user_name} enter the country once again: '))

    # Analysis
    time.sleep(0.5)
    df_answer_against = man.quest_arg_against(df_all)
    df_answer_for = man.quest_arg_for(df_all)
    df_all_countries_agegroup = man.results_all_countries_agegroup(df_all)
    df_by_country_age_group = man.results_by_country_agegroup(df_all, option_country)
    df_age_group_unemployment = man.results_age_group_unemployment(df_all)
    df_age_unemployment = man.results_age_unemployment(df_all)


    # Reporting, Exporting & Mailing
    time.sleep(3)
    mre.export_final_results('/home/usuario/Documentos/Ironhack/Project_1_0420_JuanMunoz/data/results',df_all_countries_agegroup,df_by_country_age_group,df_answer_for,df_answer_against,option_country,df_all)
    mre.create_export_barchart(df_age_unemployment)
    print('Creating a PDF File... Please wait!')
    if option_user == '1':
        mre.export_to_pdf(df_all_countries_agegroup,'results_all_countries')
    else:
        mre.export_to_pdf(df_by_country_age_group, f'results_{option_country}')
    print('PDF file created!')
    time.sleep(3)
    to_address = str(input(f'{args.user_name}, register your e-mail to receive the final report...: '))
    mre.sending_email(to_address,option_user,option_country,args.user_name)
    time.sleep(1)
    print(f'Enjoy the report {args.user_name}, but before leaving did you know....')
    time.sleep(1)
    print('-----------------------------------------------------------------------------------------------------------')
    print('The following dataframe will show the unemployment rate by age group ')
    print(df_age_group_unemployment)
    #print(df_age_unemployment)
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
    print('Juan Muñoz - Data Part-Time Ironhack 2020')

if __name__ == '__main__':
    arguments = argument_parser()
    main(arguments)


