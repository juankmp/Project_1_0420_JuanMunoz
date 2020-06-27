import pandas as pd


def merging_dataframes(df_all_raw_data,data_jobs_api,data_country_scraping):
    df_1 = pd.merge(df_all_raw_data,data_jobs_api, how='left',on = 'normalized_job_code')
    df_all = pd.merge(df_1,data_country_scraping, how='left',on = 'country_code')
    #print(df_all[0:5])
    return df_all

def renaming_df(df_all):
    new_names_list = ['uuid','education_level','full_time_job','job_code',
    'uuid_1','quest_awareness',
    'quest_vote',
    'quest_effect',
    'quest_arguments_for',
    'quest_arguments_against',
    'uuid_2',
    'country_code',
    'rural',
    'uuid_3',
    'age',
    'gender',
    'has_children',
    'age_group',
    'job_title',
    'job_title_normalized',
    'country',
    'population']
    df_all.columns = new_names_list

    filter_list = ['uuid', 'education_level', 'full_time_job', 'job_code',
                   'job_title',
                   'country_code',
                   'country',
                   'rural',
                   'age',
                   'gender',
                   'has_children',
                   'age_group',
                   'quest_awareness',
                   'quest_vote',
                   'quest_effect',
                   'quest_arguments_for',
                   'quest_arguments_against']

    df_all = df_all[filter_list]

    #print(df_all[0:6])
    return df_all

# function for remove strange characters
def replace(x):
    try:
        return x.replace("‰û_ ", "").replace("‰Û_ ", "")
    except:
        return x

def lower(x):
    try:
        return x.lower()
    except:
        return x

def replace_age(x):
    try:
        return int(x.replace(' years old',""))
    except:
        return x

def calculate_age(x):
    try:
        if len(str(x))>3:
            reference_age = 2016
            real_age = reference_age - x
            return real_age
        else:
            return x
    except:
        return x

def replace_comma(x):
    try:
        return x.replace(" ", "").replace(",", "-").lower()
    except:
        return x

def cleaning_data(df_all):
    df_all['education_level'] = df_all['education_level'].fillna('undefined')
    df_all['job_code'] = df_all['job_code'].fillna('Unemployed')
    df_all['job_title'] = df_all['job_title'].fillna('Unemployed')
    df_all['quest_effect']= df_all['quest_effect'].apply(replace)
    df_all['rural'] = df_all['rural'].apply(lower)
    df_all['has_children'] = df_all['has_children'].apply(lower)
    df_all['age_group'] = df_all['age_group'].replace("juvenile",'14_25')
    df_all['age'] = df_all['age'].apply(replace_age)
    df_all['age'] = df_all['age'].apply(calculate_age)
    df_all['gender'] = df_all['gender'].apply(lower).replace('fem','female')
    df_all['quest_arguments_against_2'] = df_all['quest_arguments_against'].apply(replace_comma)
    df_all['quest_arguments_for_2'] = df_all['quest_arguments_for'].apply(replace_comma)
    df_all['quest_arguments_against_2'] = df_all['quest_arguments_against_2'].str.replace("|",",")
    df_all['quest_arguments_for_2'] = df_all['quest_arguments_for_2'].str.replace("|",",")
    return df_all

def country_list(df_all):
    country_unique_list = set(df_all['country'])
    return country_unique_list







