import pandas as pd
from scipy.stats import chi2_contingency
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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
    ax = plt.figure(figsize=(40, 5))
    X = res.columns.tolist()
    row_0 = res.iloc[0].values.tolist()
    row_1 = res.iloc[1].values.tolist()
    X_axis = np.arange(len(X))
    bar_width = 0.4
    for Y, Y_desc in [[row_0, 'eng'], [row_1, 'ru']]:
        plt.bar(X_axis, Y, label=Y_desc, align='center', width=bar_width, edgecolor='grey')
        X_axis = [x + bar_width for x in X_axis]
    plt.xticks([r + bar_width for r in range(len(X))], X, rotation=45)
    plt.xlabel("Правила")
    plt.ylabel("Разница в %")
    plt.legend(loc='upper left')
    plt.tight_layout()
    temp_data = res.values.tolist()
    for i in range(0, len(temp_data)):
        for j in range(0, len(temp_data[i])):
            temp_data[i][j] = [str(round(p, 4)), str(temp_data[i][j])]
    res = pd.DataFrame([temp_data[0], temp_data[1]], index=['eng', 'ru'], columns=res.columns)
    template_params = {
        'desc': '',
        'col_title': res.columns.tolist(),
        'row_num': [[res.index.tolist()[i], i] for i in range(0, len(res.index.tolist()))],
        'data': res.values.tolist(),
        'data_len': [i for i in range(0, len(res.columns))],
        'p_cond': True
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
    ax = plt.figure(figsize=(40, 5))
    X = res.columns.tolist()
    row_0 = res.iloc[0].values.tolist()
    row_1 = res.iloc[1].values.tolist()
    X_axis = np.arange(len(X))
    bar_width = 0.4
    for Y, Y_desc in [[row_0, 'eng'], [row_1, 'ru']]:
        plt.bar(X_axis, Y, label=Y_desc, align='center', width=bar_width, edgecolor='grey')
        X_axis = [x + bar_width for x in X_axis]
    plt.xticks([r + bar_width for r in range(len(X))], X, rotation=45)
    plt.xlabel("Правила")
    plt.ylabel("Разница в %")
    plt.legend(loc='upper left')
    plt.tight_layout()
    temp_data = res.values.tolist()
    for i in range(0, len(temp_data)):
        for j in range(0, len(temp_data[i])):
            temp_data[i][j] = [str(round(p, 4)), str(temp_data[i][j])]
    res = pd.DataFrame([temp_data[0], temp_data[1]], index=['eng', 'ru'], columns=res.columns)
    template_params = {
        'desc': 'Разделение на языковые подгруппы согласно пункту 1.3.1 (eng-ru)',
        'col_title': res.columns.tolist(),
        'row_num': [[res.index.tolist()[i], i] for i in range(0, len(res.index.tolist()))],
        'data': res.values.tolist(),
        'data_len': [i for i in range(0, len(res.columns))],
        'p_cond': True
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
    res_dict = {
        'title': 'Статистический анализ 3',
        'desc': 'Тест значимости при помощи алгоритма chi-square на языковых подгруппах согласно пункту 1.3.1 (eng-ru)',
        'value': []
    }
    axes = []
    for data, desc_num in [[df_eng, 'Разделение подгруппы по фоновым знаниям согласно пункту 2.1.1, 2.1.2, 2.1.3, 2.1.4 на данных подгруппы eng'],
                            [df_ru, 'Разделение подгруппы по фоновым знаниям согласно пункту 2.1.1, 2.1.2, 2.1.3, 2.1.4 на данных подгруппы ru']]:
        df_1 = data[data['2.1.1']==True]
        df_2 = data[data['2.1.2']==True]
        df_3 = data[data['2.1.3']==True]
        df_4 = data[data['2.1.4']==True]
        data_temp = pd.DataFrame([df_1.sum(), df_2.sum(), df_3.sum(), df_4.sum()], index=['2.1.1', '2.1.2', '2.1.3', '2.1.4'])
        data_temp = data_temp.drop(['1.3.1', '1.3.2', '2.1.1', '2.1.2', '2.1.3', '2.1.4'], axis=1)
        if 0 in data_temp.values:
            data_temp = data_temp.apply(add_one)
        stat, p, dof, expected = chi2_contingency(data_temp)
        res = gen_stat(data_temp, expected)
        res = pd.DataFrame([res[0], res[1], res[2], res[3]], index=['2.1.1', '2.1.2', '2.1.3', '2.1.4'], columns=data_temp.columns)
        ax = plt.figure(figsize=(40, 5))
        X = res.columns.tolist()
        row_0 = res.iloc[0].values.tolist()
        row_1 = res.iloc[1].values.tolist()
        row_2 = res.iloc[2].values.tolist()
        row_3 = res.iloc[3].values.tolist()
        X_axis = np.arange(len(X))
        bar_width = 0.2
        temp = 0
        for Y, Y_desc in [[row_0, '2.1.1'], [row_1, '2.1.2'], [row_2, '2.1.3'], [row_3, '2.1.4']]:
            #X_axis = [x + temp for x in X_axis]
            plt.bar(X_axis + temp, Y, label=Y_desc, align='center', width=bar_width, edgecolor='grey')
            temp += bar_width
        plt.xticks([r + bar_width for r in range(len(X))], X, rotation=45)
        plt.xlabel("Правила")
        plt.ylabel("Разница в %")
        plt.legend(loc='upper left')
        plt.tight_layout()
        temp_data = res.values.tolist()
        for i in range(0, len(temp_data)):
            for j in range(0, len(temp_data[i])):
                temp_data[i][j] = [str(round(p, 4)), str(temp_data[i][j])]
        res = pd.DataFrame([temp_data[0], temp_data[1], temp_data[2], temp_data[3]], index=['2.1.1', '2.1.2', '2.1.3', '2.1.4'], columns=res.columns)
        template_params = {
            'desc': desc_num,
            'col_title': res.columns.tolist(),
            'row_num': [[res.index.tolist()[i], i] for i in range(0, len(res.index.tolist()))],
            'data': res.values.tolist(),
            'data_len': [i for i in range(0, len(res.columns))],
            'p_cond': True
        }
        res_dict['value'].append(template_params)
        axes.append(ax)
    return res_dict, axes

# generate dictionary for correlation 1
def gen_correlation_1(file):
    df = file.copy()
    df = df.drop(['1.3.1', '1.3.2'], axis=1)
    res = df.corr(method='pearson')
    plt.figure(figsize=(20, 20))
    ax = sns.heatmap(res, vmin=-1, vmax=1, cmap='Blues')
    plt.tight_layout()
    res = res.round(4)
    template_params = {
        'desc': '',
        'col_title': res.columns.tolist(),
        'row_num': [[res.index.tolist()[i], i] for i in range(0, len(res.index.tolist()))],
        'data': res.values.tolist(),
        'data_len': [i for i in range(0, len(res.columns))],
        'p_cond': False
    }
    res_dict = {
        'title': 'Корреляционный анализ 1',
        'desc': 'Корреляционный анализ по коэффициенту корреляции Пирсона',
        'value': [template_params]
    }
    return res_dict, [ax]

# generate dictionary for correlation 2
def gen_correlation_2(file):
    df_eng = file[file['1.3.1'] == True]
    df_ru = file[file['1.3.1'] == False]
    res_dict = {
        'title': 'Корреляционный анализ 2',
        'desc': 'Корреляционный анализ по коэффициенту корреляции Пирсона',
        'value': []
    }
    axes = []
    for data, desc_num in [[df_eng,
                            'Данные подгруппы eng'],
                           [df_ru,
                            'Данные подгруппы ru']]:
        data = data.drop(['1.3.1', '1.3.2'], axis=1)
        res = data.corr(method='pearson')
        plt.figure(figsize=(20, 20))
        ax = sns.heatmap(res, vmin=-1, vmax=1, cmap='Blues')
        plt.tight_layout()
        res = res.round(4)
        template_params = {
            'desc': desc_num,
            'col_title': res.columns.tolist(),
            'row_num': [[res.index.tolist()[i], i] for i in range(0, len(res.index.tolist()))],
            'data': res.values.tolist(),
            'data_len': [i for i in range(0, len(res.columns))],
            'p_cond': False
        }
        res_dict['value'].append(template_params)
        axes.append(ax)
    return res_dict, axes