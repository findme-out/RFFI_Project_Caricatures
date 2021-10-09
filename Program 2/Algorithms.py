import pandas as pd
from scipy.stats import chi2_contingency
import numpy as np
import matplotlib.pyplot as plt

# utility function
def add_one(x):
    return x + 1

# utility function
def gen_stat(df, expected):
    first_vals = df.values
    last_vals = expected
    res = []
    for i in range(0, len(first_vals)):
        temp = []
        for j in range(0, len(first_vals[i])):
            temp.append(round(100 - first_vals[i][j] / last_vals[i][j] * 100, 4))
        res.append(temp)
    return res
        
# generate dictionary for statistics 1
def gen_statistics_1(file):
    df = pd.DataFrame([file[file['1.3.1'] == True].sum(), file[file['1.3.1'] == False].sum()], index=['eng', 'ru'])
    df = df.drop(['1.3.1', '1.3.2'], axis=1)
    if 0 in df.values:
        df = df.apply(add_one)
    stat, p, dof, expected = chi2_contingency(df)
    res = gen_stat(df, expected)
    res = pd.DataFrame([res[0], res[1]], index=['eng', 'ru'], columns=df.columns)
    ax = plt.figure(figsize=(120,3))
    X = res.columns.tolist()
    row_0 = res.iloc[0].values.tolist()
    row_1 = res.iloc[1].values.tolist()
    X_axis = np.arange(len(X))
    for Y, Y_desc in [[row_0, 'eng'], [row_1, 'ru']]:
        plt.bar(X_axis, Y, label=Y_desc, align='center', width=0.6)
    plt.xticks(X_axis, X)
    plt.xlabel("Rules")
    plt.ylabel("Percentage difference")
    plt.legend(loc='upper left')
    template_params = {
        'desc': '',
        'col_title': res.columns.tolist(),
        'row_num': [[res.index.tolist()[i], i] for i in range(0, len(res.index.tolist()))],
        'data': res.values.tolist(),
        'data_len': [i for i in range(0, len(res.columns))]
    }
    res_dict = {
        'title': 'Статистический анализ 1',
        'desc': 'Тест значимости при помощи алгоритма chi-square',
        'value': [template_params]
    }
    return res_dict, [ax]

# generate dictionary for statistics 2
def gen_statistics_2(file):
    df = pd.DataFrame([file[file['1.3.1'] == True].sum(), file[file['1.3.1'] == False].sum()], index=['eng', 'ru'])
    df = df.drop(['1.3.1', '1.3.2'], axis=1)
    if 0 in df.values:
        df = df.apply(add_one)
    stat, p, dof, expected = chi2_contingency(df)
    res = gen_stat(df, expected)
    res = pd.DataFrame([res[0], res[1]], index=['eng', 'ru'], columns=df.columns)
    ax = plt.figure(figsize=(120, 3))
    X = res.columns.tolist()
    row_0 = res.iloc[0].values.tolist()
    row_1 = res.iloc[1].values.tolist()
    X_axis = np.arange(len(X))
    for Y, Y_desc in [[row_0, 'eng'], [row_1, 'ru']]:
        plt.bar(X_axis, Y, label=Y_desc, align='center', width=0.6)
    plt.xticks(X_axis, X)
    plt.xlabel("Rules")
    plt.ylabel("Percentage difference")
    plt.legend(loc='upper left')
    template_params = {
        'desc': 'Разделение на языковые подгруппы согласно пункту 1.3.1 (eng-ru)',
        'col_title': res.columns.tolist(),
        'row_num': [[res.index.tolist()[i], i] for i in range(0, len(res.index.tolist()))],
        'data': res.values.tolist(),
        'data_len': [i for i in range(0, len(res.columns))]
    }
    res_dict = {
        'title': 'Статистический анализ 2',
        'desc': 'Тест значимости при помощи алгоритма chi-square',
        'value': [template_params]
    }
    return res_dict, [ax]

# generate dictionary for statistics 3
def gen_statistics_3(file):
    df_eng = file[file['1.3.1'] == True]
    df_ru = file[file['1.3.1'] == False]
    df_1 = file[file['2.1.1']==True]
    df_2 = file[file['2.1.2']==True]
    df_3 = file[file['2.1.3']==True]
    df_4 = file[file['2.1.4']==True]
    res_dict = {
        'title': 'Статистический анализ 3',
        'desc': 'Тест значимости при помощи алгоритма chi-square на языковых подгруппах согласно пункту 1.3.1 (eng-ru)',
        'value': []
    }
    axes = []
    for data, desc_num, data_point in [[df_1, 'Разделение подгруппы по фоновым знаниям согласно пункту 2.1.1', '2.1.1'],
                            [df_2, 'Разделение на подгруппы по фоновым знаниям согласно пункту 2.1.2', '2.1.2'],
                            [df_3, 'Разделение на подгруппы по фоновым знаниям согласно пункту 2.1.3', '2.1.3'],
                            [df_4, 'Разделение на подгруппы по фоновым знаниям согласно пункту 2.1.4', '2.1.4']]:
        for second_data, second_data_desc in [[df_eng, 'eng'], [df_ru, 'ru']]:
            data = pd.DataFrame([second_data.sum(), data.sum()], index=[second_data_desc, data_point])
            data = data.drop(['1.3.1', '1.3.2'], axis=1)
            if 0 in data.values:
                data = data.apply(add_one)
            stat, p, dof, expected = chi2_contingency(data)
            res = gen_stat(data, expected)
            res = pd.DataFrame([res[0], res[1]], index=[second_data_desc, data_point], columns=data.columns)
            ax = plt.figure(figsize=(120, 3))
            X = res.columns.tolist()
            row_0 = res.iloc[0].values.tolist()
            row_1 = res.iloc[1].values.tolist()
            X_axis = np.arange(len(X))
            for Y, Y_desc in [[row_0, second_data_desc], [row_1, data_point]]:
                plt.bar(X_axis, Y, label=Y_desc, align='center', width=0.6)
            plt.xticks(X_axis, X)
            plt.xlabel("Rules")
            plt.ylabel("Percentage difference")
            plt.legend(loc='upper left')
            template_params = {
                'desc': desc_num + ', ' + second_data_desc,
                'col_title': res.columns.tolist(),
                'row_num': [[res.index.tolist()[i], i] for i in range(0, len(res.index.tolist()))],
                'data': res.values.tolist(),
                'data_len': [i for i in range(0, len(res.columns))]
            }
            res_dict['value'].append(template_params)
            axes.append(ax)
    return res_dict, axes