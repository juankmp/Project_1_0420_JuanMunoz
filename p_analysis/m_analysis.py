import pandas as pd


def quest_arg_against(df_all):
    print('Calculating your data....')
    value_list = []
    for i in df_all['quest_arguments_against_2']:
        val = list(i.split(","))
        value_list.append(val)

    df_all['quest_arguments_against_2'] = value_list

    # count the times we have each answer in total
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0

    for data in df_all['quest_arguments_against_2']:
        if len(list(data)) == 1:
            if data[0] == 'noneoftheabove':
                a += 1
            elif data[0] == 'itmightencouragepeopletostopworking':
                b += 1
            elif data[0] == 'foreignersmightcometomycountryandtakeadvantageofthebenefit':
                c += 1
            elif data[0] == 'itisimpossibletofinance':
                d += 1
            elif data[0] == 'itincreasesdependenceonthestate':
                e += 1
            elif data[0] == 'itisagainsttheprincipleoflinkingmeritandreward':
                f += 1
            elif data[0] == 'onlythepeoplewhoneeditmostshouldgetsomethingfromthestate':
                g += 1
        else:
            for datain in list(data):
                if datain == 'noneoftheabove':
                    a += 1
                elif datain == 'itmightencouragepeopletostopworking':
                    b += 1
                elif datain == 'foreignersmightcometomycountryandtakeadvantageofthebenefit':
                    c += 1
                elif datain == 'itisimpossibletofinance':
                    d += 1
                elif datain == 'itincreasesdependenceonthestate':
                    e += 1
                elif datain == 'itisagainsttheprincipleoflinkingmeritandreward':
                    f += 1
                elif datain == 'onlythepeoplewhoneeditmostshouldgetsomethingfromthestate':
                    g += 1

    dict_result = {'None of the above': a,
                   'It might encourage people to stop working': b,
                   'Foreigners might come to my country and take advantage of the benefit': c,
                   'It is impossible to finance': d,
                   'It increases dependence on the state': e,
                   'It is against the principle of linking merit and reward': f,
                   'Only the people who need it most should get something from the state': g}

    df_answer_against = pd.DataFrame.from_dict(dict_result, orient='index', columns=['Answers'])

    df_answer_against['%Total'] = round((df_answer_against['Answers'] / len(df_all['quest_arguments_against_2']) * 100),
                                        2).astype(str) + '%'

    df_answer_against = df_answer_against.sort_values('Answers', ascending=False)

    return df_answer_against

def quest_arg_for(df_all):
    value_list = []
    for i in df_all['quest_arguments_for_2']:
        val = list(i.split(","))
        value_list.append(val)

    df_all['quest_arguments_for_2'] = value_list

    # count the times we have each answer in total
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0

    for data in df_all['quest_arguments_for_2']:
        if len(list(data)) == 1:
            if data[0] == 'noneoftheabove':
                a += 1
            elif data[0] == 'itincreasesappreciationforhouseholdworkandvolunteering':
                b += 1
            elif data[0] == 'itencouragesfinancialindependenceandself-responsibility':
                c += 1
            elif data[0] == 'itreducesanxietyaboutfinancingbasicneeds':
                d += 1
            elif data[0] == 'itcreatesmoreequalityofopportunity':
                e += 1
            elif data[0] == 'itreducesbureaucracyandadministrativeexpenses':
                f += 1
            elif data[0] == 'itincreasessolidarity-becauseitisfundedbyeveryone':
                g += 1
        else:
            for datain in list(data):
                if datain == 'noneoftheabove':
                    a += 1
                elif datain == 'itincreasesappreciationforhouseholdworkandvolunteering':
                    b += 1
                elif datain == 'itencouragesfinancialindependenceandself-responsibility':
                    c += 1
                elif datain == 'itreducesanxietyaboutfinancingbasicneeds':
                    d += 1
                elif datain == 'itcreatesmoreequalityofopportunity':
                    e += 1
                elif datain == 'itreducesbureaucracyandadministrativeexpenses':
                    f += 1
                elif datain == 'itincreasessolidarity-becauseitisfundedbyeveryone':
                    g += 1

    dict_result = {'None of the above': a,
                   'It increases appreciation for household work and volunteering': b,
                   'It encourages financial independence and self-responsibility': c,
                   'It reduces anxiety about financing basic needs': d,
                   'It creates more equality of opportunity': e,
                   'It reduces bureaucracy and administrative expenses': f,
                   'It increase ssolidarity because it is funded by everyone': g}

    df_answer_for = pd.DataFrame.from_dict(dict_result, orient='index', columns=['Answers'])

    df_answer_for['%Total'] = round((df_answer_for['Answers'] / len(df_all['quest_arguments_for_2']) * 100), 2).astype(
        str) + '%'

    df_answer_for = df_answer_for.sort_values('Answers', ascending=False)

    return df_answer_for

def results_all_countries_agegroup(df_all):
    df_result = df_all.groupby(['country', 'job_title', 'new_age_group']).agg({'uuid': ['count']})
    df_result.columns = ['Quantity']
    df_result = df_result.reset_index().sort_values(by='Quantity', ascending=False)
    df_result.columns = ['Country', 'Job Title', 'New age group', 'Quantity']
    # df_result.loc['Total']= df_result.sum(numeric_only=True, axis=0)
    df_result_per = df_result.copy()
    df_result_per['Percentage'] = round(df_result['Quantity'] / df_result['Quantity'].sum() * 100, 2).astype(str) + '%'
    df_all_countries_agegroup = df_result_per.set_index('Country')

    return df_all_countries_agegroup


def results_by_country_agegroup(df_all,option_country):
    df_result = df_all.groupby(['country', 'job_title', 'new_age_group']).agg({'uuid': ['count']})
    df_result.columns = ['Quantity']
    df_result = df_result.reset_index().sort_values(by='Quantity', ascending=False)
    df_result.columns = ['Country', 'Job Title', 'New age group', 'Quantity']
    filter_country = df_result['Country'] == option_country

    df_result_country = df_result[filter_country].sort_values(by='Quantity', ascending=False)
    df_result_country['Percentage'] = round(df_result_country['Quantity'] / df_result_country['Quantity'].sum() * 100,
                                            2).astype(str) + '%'
    df_by_country_age_group = df_result_country.set_index('Country')

    return df_by_country_age_group

def results_age_group_unemployment(df_all):
    df_result_test = df_all.groupby(['new_age_group']).agg({'uuid': ['count']})
    df_result_test.columns = ['Total_Qty']
    df_result_test = df_result_test.reset_index()
    df_result_test.columns = ['new_age_group', 'Total_Qty']
    df_result_test.loc['Total'] = df_result_test.sum(numeric_only=True, axis=0)
    df_result_test['%Share/Total'] = round(df_result_test['Total_Qty'] / df_result_test['Total_Qty'].sum() * 100 * 2,
                                           1).astype(str) + '%'
    df_result_test['new_age_group'] = df_result_test['new_age_group'].fillna('Total')

    filter = (df_all['full_time_job'] == 'no')
    df_all_2 = df_all[filter]

    df_result_test_2 = df_all_2.groupby(['new_age_group']).agg({'uuid': ['count']})
    df_result_test_2.columns = ['Unemployed_Qty']
    df_result_test_2 = df_result_test_2.reset_index()
    df_result_test_2.columns = ['new_age_group', 'Unemployed_Qty']
    df_result_test_2.loc['Total'] = df_result_test_2.sum(numeric_only=True, axis=0)
    df_result_test_2['%Share/Unemployed'] = round(
        df_result_test_2['Unemployed_Qty'] / df_result_test_2['Unemployed_Qty'].sum() * 100 * 2, 1).astype(str) + '%'
    df_result_test_2['new_age_group'] = df_result_test_2['new_age_group'].fillna('Total')

    df_age_group_unemployment = pd.merge(df_result_test, df_result_test_2, how='left', on='new_age_group')
    df_age_group_unemployment['%Unemployment rate'] = round(
        df_age_group_unemployment['Unemployed_Qty'] / df_age_group_unemployment['Total_Qty'] * 100, 1).astype(str) + '%'

    return df_age_group_unemployment

def results_age_unemployment(df_all):
    df_result_test = df_all.groupby(['age']).agg({'uuid': ['count']})
    df_result_test.columns = ['Total_Qty']
    df_result_test = df_result_test.reset_index()
    df_result_test.columns = ['age', 'Total_Qty']
    # df_result_test.loc['Total']= df_result_test.sum(numeric_only=True, axis=0)
    df_result_test['%Share/Total'] = round(df_result_test['Total_Qty'] / df_result_test['Total_Qty'].sum() * 100 * 2,
                                           1).astype(str) + '%'
    df_result_test['age'] = df_result_test['age'].fillna('Total')

    filter = (df_all['full_time_job'] == 'no')
    df_all_2 = df_all[filter]

    df_result_test_2 = df_all_2.groupby(['age']).agg({'uuid': ['count']})
    df_result_test_2.columns = ['Unemployed_Qty']
    df_result_test_2 = df_result_test_2.reset_index()
    df_result_test_2.columns = ['age', 'Unemployed_Qty']
    # df_result_test_2.loc['Total']= df_result_test_2.sum(numeric_only=True, axis=0)
    df_result_test_2['%Share/Unemployed'] = round(
        df_result_test_2['Unemployed_Qty'] / df_result_test_2['Unemployed_Qty'].sum() * 100 * 2, 1).astype(str) + '%'
    df_result_test_2['age'] = df_result_test_2['age'].fillna('Total')

    df_age_unemployment = pd.merge(df_result_test, df_result_test_2, how='left', on='age')
    df_age_unemployment['%Unemployment rate'] = round(
        df_age_unemployment['Unemployed_Qty'] / df_age_unemployment['Total_Qty'] * 100, 1).astype(str) + '%'

    return df_age_unemployment


