import pandas as pd
from scipy.stats import chi2_contingency
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import warnings
import scipy.cluster.hierarchy as sch
import os

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

# generate dictionary for code-feature description
def gen_code_feature_desc(file):
    code_feature_desc_file = 'code_feature_desc.xlsx'
    current_path = os.path.dirname(os.path.abspath(__file__))
    temp_path = ''
    for i in current_path:
        if i == '\\':
            i = '/'
        temp_path += i
    temp_path += '/' + code_feature_desc_file
    df = pd.read_excel(temp_path, index_col=0)
    res = df.copy()
    res_dict = {
        'title': 'Описание признаков',
        'desc': '',
        'value': []
    }
    template_params = {
        'desc': '',
        'col_title': res.columns.tolist(),
        'row_num': [[res.index.tolist()[i], i] for i in range(0, len(res.index.tolist()))],
        'data': res.values.tolist(),
        'data_len': [i for i in range(0, len(res.columns))],
        'p_cond': False,
        'graph_option': False
    }
    res_dict['value'].append(template_params)
    return res_dict, [None]

# generate dictionary for statistics 1
def gen_statistics_1(file):
    df = pd.DataFrame([file[file['1.3.1'] == True].sum(), file[file['1.3.1'] == False].sum()], index=['eng', 'ru'])
    raw_df = df.copy()
    template_params = {
        'desc': 'Таблица сырых данных',
        'col_title': raw_df.columns.tolist(),
        'row_num': [[raw_df.index.tolist()[i], i] for i in range(0, len(raw_df.index.tolist()))],
        'data': raw_df.values.tolist(),
        'data_len': [i for i in range(0, len(raw_df.columns))],
        'p_cond': False,
        'graph_option': False
    }
    res_dict = {
        'title': 'Статистический анализ 1',
        'desc': 'Тест значимости при помощи алгоритма chi-square',
        'value': []
    }
    res_dict['value'].append(template_params)
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
        'p_cond': True,
        'graph_option': True
    }
    res_dict['value'].append(template_params)
    return res_dict, [None, ax]

# generate dictionary for statistics 2
def gen_statistics_2(file):
    df = pd.DataFrame([file[file['1.3.1'] == True].sum(), file[file['1.3.1'] == False].sum()], index=['eng', 'ru'])
    raw_df = df.copy()
    template_params = {
        'desc': 'Таблица сырых данных',
        'col_title': raw_df.columns.tolist(),
        'row_num': [[raw_df.index.tolist()[i], i] for i in range(0, len(raw_df.index.tolist()))],
        'data': raw_df.values.tolist(),
        'data_len': [i for i in range(0, len(raw_df.columns))],
        'p_cond': False,
        'graph_option': False
    }
    res_dict = {
        'title': 'Статистический анализ 2',
        'desc': 'Тест значимости при помощи алгоритма chi-square',
        'value': []
    }
    res_dict['value'].append(template_params)
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
        'p_cond': True,
        'graph_option': True
    }
    res_dict['value'].append(template_params)
    return res_dict, [None, ax]

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
        raw_df = data_temp.copy()
        template_params = {
            'desc': 'Таблица сырых данных',
            'col_title': raw_df.columns.tolist(),
            'row_num': [[raw_df.index.tolist()[i], i] for i in range(0, len(raw_df.index.tolist()))],
            'data': raw_df.values.tolist(),
            'data_len': [i for i in range(0, len(raw_df.columns))],
            'p_cond': False,
            'graph_option': False
        }
        res_dict['value'].append(template_params)
        axes.append(None)
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
            'p_cond': True,
            'graph_option': True
        }
        res_dict['value'].append(template_params)
        axes.append(ax)
    return res_dict, axes

# generate dictionary for statistics 4
def gen_statistics_4(file):
    df_eng = file[file['1.3.1'] == True]
    df_ru = file[file['1.3.1'] == False]
    res_dict = {
        'title': 'Статистический анализ 4',
        'desc': 'Тест значимости при помощи алгоритма chi-square на языковых подгруппах согласно пункту 1.3.1 (eng-ru)',
        'value': []
    }
    axes = []
    for data, desc_num in [[df_eng, 'Разделение подгруппы по мишень-президент согласно пункту 2.4.2.1.1 на данных подгруппы eng'],
                            [df_ru, 'Разделение подгруппы по мишень-президент согласно пункту 2.4.2.1.1 на данных подгруппы ru']]:
        df_1 = data[data['2.4.2.1.1']==True]
        df_2 = data[data['2.4.2.1.1'] == False]
        data_temp = pd.DataFrame([df_1.sum(), df_2.sum()], index=['российский президент', 'не российский президент'])
        raw_df = data_temp.copy()
        template_params = {
            'desc': 'Таблица сырых данных',
            'col_title': raw_df.columns.tolist(),
            'row_num': [[raw_df.index.tolist()[i], i] for i in range(0, len(raw_df.index.tolist()))],
            'data': raw_df.values.tolist(),
            'data_len': [i for i in range(0, len(raw_df.columns))],
            'p_cond': False,
            'graph_option': False
        }
        res_dict['value'].append(template_params)
        axes.append(None)
        data_temp = data_temp.drop(['1.3.1', '1.3.2', '2.4.2.1.1'], axis=1)
        if 0 in data_temp.values:
            data_temp = data_temp.apply(add_one)
        stat, p, dof, expected = chi2_contingency(data_temp)
        res = gen_stat(data_temp, expected)
        res = pd.DataFrame([res[0], res[1]], index=['российский президент', 'не российский президент'], columns=data_temp.columns)
        ax = plt.figure(figsize=(40, 5))
        X = res.columns.tolist()
        row_0 = res.iloc[0].values.tolist()
        row_1 = res.iloc[1].values.tolist()
        X_axis = np.arange(len(X))
        bar_width = 0.4
        temp = 0
        for Y, Y_desc in [[row_0, 'российский президент'], [row_1, 'не российский президент']]:
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
        res = pd.DataFrame([temp_data[0], temp_data[1]], index=['российский президент', 'не российский президент'], columns=res.columns)
        template_params = {
            'desc': desc_num,
            'col_title': res.columns.tolist(),
            'row_num': [[res.index.tolist()[i], i] for i in range(0, len(res.index.tolist()))],
            'data': res.values.tolist(),
            'data_len': [i for i in range(0, len(res.columns))],
            'p_cond': True,
            'graph_option': True
        }
        res_dict['value'].append(template_params)
        axes.append(ax)
    return res_dict, axes

# generate dictionary for statistics 5
def gen_statistics_5(file):
    df_eng = file[file['1.3.1'] == True]
    df_ru = file[file['1.3.1'] == False]
    res_dict = {
        'title': 'Статистический анализ 5',
        'desc': 'Тест значимости при помощи алгоритма chi-square на языковых подгруппах согласно пункту 1.3.1 (eng-ru)',
        'value': []
    }
    axes = []
    for data, desc_num in [[df_eng, 'Разделение подгруппы по внешней политике, внутренней политике, истории согласно пункту 2.5.1, 2.5.2, 2.5.3 на данных подгруппы eng'],
                            [df_ru, 'Разделение подгруппы по внешней политике, внутренней политике, истории согласно пункту 2.5.1, 2.5.2, 2.5.3 на данных подгруппы ru']]:
        df_1 = data[(data['2.5.1.1.1']==True) | (data['2.5.1.1.2']==True) | (data['2.5.1.1.3']==True) | (data['2.5.1.1.4']==True) | (data['2.5.1.1.5']==True) |
                    (data['2.5.1.1.6']==True) | (data['2.5.1.1.7']==True) | (data['2.5.1.1.8']==True) | (data['2.5.1.1.9']==True) | (data['2.5.1.1.10']==True)]
        df_2 = data[(data['2.5.2.1.1']==True) | (data['2.5.2.1.2']==True) | (data['2.5.2.1.3']==True) | (data['2.5.2.1.4']==True) | (data['2.5.2.1.5']==True) |
                    (data['2.5.2.1.6']==True) | (data['2.5.2.1.7']==True) | (data['2.5.2.1.8']==True) | (data['2.5.2.1.9']==True) | (data['2.5.2.1.10']==True) |
                    (data['2.5.2.1.11']==True) | (data['2.5.2.1.12']==True) | (data['2.5.2.1.13']==True) | (data['2.5.2.1.14']==True) | (data['2.5.2.1.15']==True) |
                    (data['2.5.2.1.16']==True) | (data['2.5.2.1.17']==True)]
        df_3 = data[data['2.5.3.1.1']==True]
        data_temp = pd.DataFrame([df_1.sum(), df_2.sum(), df_3.sum()], index=['2.5.1', '2.5.2', '2.5.3'])
        raw_df = data_temp.copy()
        template_params = {
            'desc': 'Таблица сырых данных',
            'col_title': raw_df.columns.tolist(),
            'row_num': [[raw_df.index.tolist()[i], i] for i in range(0, len(raw_df.index.tolist()))],
            'data': raw_df.values.tolist(),
            'data_len': [i for i in range(0, len(raw_df.columns))],
            'p_cond': False,
            'graph_option': False
        }
        res_dict['value'].append(template_params)
        axes.append(None)
        data_temp = data_temp.drop(['1.3.1', '1.3.2', '2.5.1.1.1', '2.5.1.1.2', '2.5.1.1.3', '2.5.1.1.4', '2.5.1.1.5',
                                    '2.5.1.1.6', '2.5.1.1.7', '2.5.1.1.8', '2.5.1.1.9', '2.5.1.1.10', '2.5.2.1.1', '2.5.2.1.2',
                                    '2.5.2.1.3', '2.5.2.1.4', '2.5.2.1.5', '2.5.2.1.6', '2.5.2.1.7', '2.5.2.1.8', '2.5.2.1.9', '2.5.2.1.10',
                                    '2.5.2.1.11', '2.5.2.1.12', '2.5.2.1.13', '2.5.2.1.14', '2.5.2.1.15', '2.5.2.1.16', '2.5.2.1.17', '2.5.3.1.1',
                                    '2.5.3.1.2'], axis=1)
        if 0 in data_temp.values:
            data_temp = data_temp.apply(add_one)
        stat, p, dof, expected = chi2_contingency(data_temp)
        res = gen_stat(data_temp, expected)
        res = pd.DataFrame([res[0], res[1], res[2]], index=['2.5.1', '2.5.2', '2.5.3'], columns=data_temp.columns)
        ax = plt.figure(figsize=(40, 5))
        X = res.columns.tolist()
        row_0 = res.iloc[0].values.tolist()
        row_1 = res.iloc[1].values.tolist()
        row_2 = res.iloc[2].values.tolist()
        X_axis = np.arange(len(X))
        bar_width = 0.26
        temp = 0
        for Y, Y_desc in [[row_0, '2.5.1'], [row_1, '2.5.2'], [row_2, '2.5.3']]:
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
        res = pd.DataFrame([temp_data[0], temp_data[1], temp_data[2]], index=['2.5.1', '2.5.2', '2.5.3'], columns=res.columns)
        template_params = {
            'desc': desc_num,
            'col_title': res.columns.tolist(),
            'row_num': [[res.index.tolist()[i], i] for i in range(0, len(res.index.tolist()))],
            'data': res.values.tolist(),
            'data_len': [i for i in range(0, len(res.columns))],
            'p_cond': True,
            'graph_option': True
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
    plt.title('Корреляционная матрица')
    plt.tight_layout()
    res = res.round(4)
    res_na = res.isnull().values.any()
    if res_na:
        res = res.fillna('error')
    template_params = {
        'desc': 'error в качестве значения означает, что данное сочетание признаков не имеет корреляции '
                '(все значения одного или обоих признаков относятся к классу 0)',
        'col_title': res.columns.tolist(),
        'row_num': [[res.index.tolist()[i], i] for i in range(0, len(res.index.tolist()))],
        'data': res.values.tolist(),
        'data_len': [i for i in range(0, len(res.columns))],
        'p_cond': False,
        'graph_option': True
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
        plt.title('Корреляционная матрица')
        plt.tight_layout()
        res = res.round(4)
        res_na = res.isnull().values.any()
        if res_na:
            res = res.fillna('error')
        template_params = {
            'desc': desc_num + '. ' +
                    'error в качестве значения означает, что данное сочетание признаков не имеет корреляции '
                    '(все значения одного или обоих признаков относятся к классу 0)',
            'col_title': res.columns.tolist(),
            'row_num': [[res.index.tolist()[i], i] for i in range(0, len(res.index.tolist()))],
            'data': res.values.tolist(),
            'data_len': [i for i in range(0, len(res.columns))],
            'p_cond': False,
            'graph_option': True
        }
        res_dict['value'].append(template_params)
        axes.append(ax)
    return res_dict, axes

# generate dictionary for regression 1
def gen_regression_1(file):
    df = file.copy()
    res_dict = {
        'title': 'Регрессионный анализ 1',
        'desc': 'Регрессионный анализ при помощи логистической регрессии. '
                'Показаны результаты отчета классификации, где 0 - False, 1 - True',
        'value': []
    }
    reg_dict = {
        '0_precision': [],
        '0_recall': [],
        '0_f1-score': [],
        '1_precision': [],
        '1_recall': [],
        '1_f1-score': [],
        'accuracy': []
    }
    reg_cols = ['1.3.1', '1.3.2', '2.1.1', '2.1.2', '2.1.3', '2.1.4', '2.4.1.1.1', '2.4.1.1.2', '2.4.1.1.3', '2.4.1.1.4', '2.4.1.1.5', '2.4.1.1.6',
                '2.4.1.1.7', '2.4.1.1.8', '2.4.1.1.9', '2.4.1.2.1', '2.4.1.2.2', '2.4.1.2.3', '2.4.1.2.4', '2.4.1.2.5', '2.4.1.2.6', '2.4.1.2.7',
                '2.4.1.2.8', '2.4.1.2.9', '2.4.2.1.1', '2.4.2.1.2', '2.4.2.1.3', '2.4.2.1.4', '2.4.2.1.5', '2.4.2.1.6', '2.4.2.1.7', '2.4.2.1.8',
                '2.4.2.1.9', '2.4.2.2.1', '2.4.2.2.2', '2.4.2.2.3', '2.4.2.2.4', '2.5.1.1.1', '2.5.1.1.2', '2.5.1.1.3', '2.5.1.1.4', '2.5.1.1.5',
                '2.5.1.1.6', '2.5.1.1.7', '2.5.1.1.8', '2.5.1.1.9', '2.5.1.1.10', '2.5.2.1.1', '2.5.2.1.2', '2.5.2.1.3', '2.5.2.1.4', '2.5.2.1.5',
                '2.5.2.1.6', '2.5.2.1.7', '2.5.2.1.8', '2.5.2.1.9', '2.5.2.1.10', '2.5.2.1.11', '2.5.2.1.12', '2.5.2.1.13', '2.5.2.1.14', '2.5.2.1.15',
                '2.5.2.1.16', '2.5.2.1.17', '2.5.3.1.1', '2.5.3.1.2', '2.6.1', '2.6.2', '2.6.3', '2.6.4', '2.6.5', '2.6.6', '2.6.7', '2.7.1', '2.7.2', '2.7.3',
                '2.9.1.1.1', '2.9.1.1.2', '2.9.1.1.3', '2.9.1.1.4', '2.9.1.1.5', '2.9.1.2.1', '2.9.1.2.2', '2.9.1.2.3', '2.9.1.2.4', '2.9.2', '3.1.1.1.1',
                '3.1.1.1.2', '3.1.1.1.3', '3.1.1.1.4', '3.1.1.1.5', '3.1.1.1.6', '3.1.1.1.7', '3.1.2', '3.5.1.1.1', '3.5.1.1.2', '3.5.1.1.3', '3.5.1.1.4',
                '3.5.1.1.5', '3.5.2.1.1', '3.5.2.1.2', '3.5.2.1.3', '3.5.2.1.4', '3.5.2.1.5', '3.5.3.1.1', '3.5.3.1.2', '3.5.3.1.3', '3.5.3.1.4', '3.5.3.1.5',
                '3.5.4.1.1', '3.5.4.1.2', '3.5.4.1.3', '3.5.4.1.4', '3.5.4.1.5', '3.5.5.1.1', '3.5.5.1.2', '3.5.5.1.3', '3.5.5.1.4', '3.5.5.1.5', '4.6.1',
                '4.6.2', '4.6.3', '4.6.4', '4.6.5', '4.6.6', '4.6.7', '4.6.8', '4.6.9', '4.6.10', '4.6.11', '4.6.12', '4.6.13', '4.6.14', '4.6.15', '4.6.16',
                '4.6.17', '4.6.18', '4.6.19', '4.6.20', '4.6.21', '4.6.22', '4.6.23', '4.6.24', '4.6.25', '4.2.1', '4.2.2', '4.2.3', '4.2.4', '4.2.5', '4.2.6',
                '4.2.7', '4.3.1', '4.3.2', '4.3.3', '4.3.4', '4.3.5', '4.3.6', '4.3.7', '4.3.8', '4.3.9', '4.3.10', '4.3.11', '4.3.12', '4.3.13', '4.3.14', '4.4.1',
                '4.4.2', '4.4.3', '4.4.4', '4.4.5', '4.4.6', '4.5.1', '4.5.2', '4.5.3', '4.5.4', '4.5.5', '4.5.6', '4.5.7', '4.5.8', '4.5.9']
    warnings.filterwarnings('ignore')
    for col in reg_cols:
        if len(df[col].unique()) != 1 and (df[col].value_counts()[0] > 2 and df[col].value_counts()[1] > 2):
            X = df.drop(col, axis=1)
            y = df[col]
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42, stratify=y)
            scaler = preprocessing.StandardScaler().fit(X_train)
            X_train_scaled = scaler.transform(X_train)
            model = LogisticRegression()
            model.fit(X_train_scaled, y_train)
            y_pred = model.predict(X_test)
            cl_dict = classification_report(y_test, y_pred, output_dict=True)
            if '0' in cl_dict.keys():
                reg_dict['0_precision'].append(cl_dict['0']['precision'])
                reg_dict['0_recall'].append(cl_dict['0']['recall'])
                reg_dict['0_f1-score'].append(cl_dict['0']['f1-score'])
            else:
                reg_dict['0_precision'].append(None)
                reg_dict['0_recall'].append(None)
                reg_dict['0_f1-score'].append(None)
            if '1' in cl_dict.keys():
                reg_dict['1_precision'].append(cl_dict['1']['precision'])
                reg_dict['1_recall'].append(cl_dict['1']['recall'])
                reg_dict['1_f1-score'].append(cl_dict['1']['f1-score'])
            else:
                reg_dict['1_precision'].append(None)
                reg_dict['1_recall'].append(None)
                reg_dict['1_f1-score'].append(None)
            reg_dict['accuracy'].append(cl_dict['accuracy'])
        else:
            reg_dict['0_precision'].append('error')
            reg_dict['0_recall'].append('error')
            reg_dict['0_f1-score'].append('error')
            reg_dict['1_precision'].append('error')
            reg_dict['1_recall'].append('error')
            reg_dict['1_f1-score'].append('error')
            reg_dict['accuracy'].append('error')
    res = pd.DataFrame.from_dict(reg_dict, orient='index', columns=reg_cols)
    res = res.round(4)
    res_na = res.isnull().values.any()
    if res_na:
        res = res.fillna('error')
    template_params = {
        'desc': 'При расчете регрессии пары данных зависимой и независимой переменных используются для тренировки модели '
                '(подбор модели, минимизирующей неточность прогноза). '
                'error в качестве значения означает, что в зависимой переменной '
                'наблюдаются результаты, принадлежащие '
                'только одному классу (0 или 1), или количество объектов, принадлежащих к одному из классов, меньше 2',
        'col_title': res.columns.tolist(),
        'row_num': [[res.index.tolist()[i], i] for i in range(0, len(res.index.tolist()))],
        'data': res.values.tolist(),
        'data_len': [i for i in range(0, len(res.columns))],
        'p_cond': False,
        'graph_option': False
    }
    res_dict['value'].append(template_params)
    return res_dict, [None]

# generate dictionary for regression 2
def gen_regression_2(file):
    df = file.copy()
    df_eng = df[df['1.3.1']==True]
    df_ru = df[df['1.3.1']==False]
    res_dict = {
        'title': 'Регрессионный анализ 2',
        'desc': 'Регрессионный анализ при помощи логистической регрессии. '
                'Показаны результаты отчета классификации, где 0 - False, 1 - True',
        'value': []
    }
    reg_cols = ['2.1.1', '2.1.2', '2.1.3', '2.1.4', '2.4.1.1.1', '2.4.1.1.2', '2.4.1.1.3',
                '2.4.1.1.4', '2.4.1.1.5', '2.4.1.1.6',
                '2.4.1.1.7', '2.4.1.1.8', '2.4.1.1.9', '2.4.1.2.1', '2.4.1.2.2', '2.4.1.2.3', '2.4.1.2.4', '2.4.1.2.5',
                '2.4.1.2.6', '2.4.1.2.7',
                '2.4.1.2.8', '2.4.1.2.9', '2.4.2.1.1', '2.4.2.1.2', '2.4.2.1.3', '2.4.2.1.4', '2.4.2.1.5', '2.4.2.1.6',
                '2.4.2.1.7', '2.4.2.1.8',
                '2.4.2.1.9', '2.4.2.2.1', '2.4.2.2.2', '2.4.2.2.3', '2.4.2.2.4', '2.5.1.1.1', '2.5.1.1.2', '2.5.1.1.3',
                '2.5.1.1.4', '2.5.1.1.5',
                '2.5.1.1.6', '2.5.1.1.7', '2.5.1.1.8', '2.5.1.1.9', '2.5.1.1.10', '2.5.2.1.1', '2.5.2.1.2', '2.5.2.1.3',
                '2.5.2.1.4', '2.5.2.1.5',
                '2.5.2.1.6', '2.5.2.1.7', '2.5.2.1.8', '2.5.2.1.9', '2.5.2.1.10', '2.5.2.1.11', '2.5.2.1.12',
                '2.5.2.1.13', '2.5.2.1.14', '2.5.2.1.15',
                '2.5.2.1.16', '2.5.2.1.17', '2.5.3.1.1', '2.5.3.1.2', '2.6.1', '2.6.2', '2.6.3', '2.6.4', '2.6.5',
                '2.6.6', '2.6.7', '2.7.1', '2.7.2', '2.7.3',
                '2.9.1.1.1', '2.9.1.1.2', '2.9.1.1.3', '2.9.1.1.4', '2.9.1.1.5', '2.9.1.2.1', '2.9.1.2.2', '2.9.1.2.3',
                '2.9.1.2.4', '2.9.2', '3.1.1.1.1',
                '3.1.1.1.2', '3.1.1.1.3', '3.1.1.1.4', '3.1.1.1.5', '3.1.1.1.6', '3.1.1.1.7', '3.1.2', '3.5.1.1.1',
                '3.5.1.1.2', '3.5.1.1.3', '3.5.1.1.4',
                '3.5.1.1.5', '3.5.2.1.1', '3.5.2.1.2', '3.5.2.1.3', '3.5.2.1.4', '3.5.2.1.5', '3.5.3.1.1', '3.5.3.1.2',
                '3.5.3.1.3', '3.5.3.1.4', '3.5.3.1.5',
                '3.5.4.1.1', '3.5.4.1.2', '3.5.4.1.3', '3.5.4.1.4', '3.5.4.1.5', '3.5.5.1.1', '3.5.5.1.2', '3.5.5.1.3',
                '3.5.5.1.4', '3.5.5.1.5', '4.6.1',
                '4.6.2', '4.6.3', '4.6.4', '4.6.5', '4.6.6', '4.6.7', '4.6.8', '4.6.9', '4.6.10', '4.6.11', '4.6.12',
                '4.6.13', '4.6.14', '4.6.15', '4.6.16',
                '4.6.17', '4.6.18', '4.6.19', '4.6.20', '4.6.21', '4.6.22', '4.6.23', '4.6.24', '4.6.25', '4.2.1',
                '4.2.2', '4.2.3', '4.2.4', '4.2.5', '4.2.6',
                '4.2.7', '4.3.1', '4.3.2', '4.3.3', '4.3.4', '4.3.5', '4.3.6', '4.3.7', '4.3.8', '4.3.9', '4.3.10',
                '4.3.11', '4.3.12', '4.3.13', '4.3.14', '4.4.1',
                '4.4.2', '4.4.3', '4.4.4', '4.4.5', '4.4.6', '4.5.1', '4.5.2', '4.5.3', '4.5.4', '4.5.5', '4.5.6',
                '4.5.7', '4.5.8', '4.5.9']
    for data, desc_num in [[df_eng,
                            'Основано на данных подгруппы eng'],
                           [df_ru,
                            'Основано на данных подгруппы ru']]:
        data = data.drop(['1.3.1', '1.3.2'], axis=1)
        reg_dict = {
            '0_precision': [],
            '0_recall': [],
            '0_f1-score': [],
            '1_precision': [],
            '1_recall': [],
            '1_f1-score': [],
            'accuracy': []
        }
        warnings.filterwarnings('ignore')
        for col in reg_cols:
            if len(data[col].unique()) != 1 and (data[col].value_counts()[0] > 2 and data[col].value_counts()[1] > 2):
                X = data.drop(col, axis=1)
                y = data[col]
                X_train, X_test, y_train, y_test = train_test_split(
                    X, y, test_size=0.2, random_state=42, stratify=y)
                scaler = preprocessing.StandardScaler().fit(X_train)
                X_train_scaled = scaler.transform(X_train)
                model = LogisticRegression()
                model.fit(X_train_scaled, y_train)
                y_pred = model.predict(X_test)
                cl_dict = classification_report(y_test, y_pred, output_dict=True)
                if '0' in cl_dict.keys():
                    reg_dict['0_precision'].append(cl_dict['0']['precision'])
                    reg_dict['0_recall'].append(cl_dict['0']['recall'])
                    reg_dict['0_f1-score'].append(cl_dict['0']['f1-score'])
                else:
                    reg_dict['0_precision'].append(None)
                    reg_dict['0_recall'].append(None)
                    reg_dict['0_f1-score'].append(None)
                if '1' in cl_dict.keys():
                    reg_dict['1_precision'].append(cl_dict['1']['precision'])
                    reg_dict['1_recall'].append(cl_dict['1']['recall'])
                    reg_dict['1_f1-score'].append(cl_dict['1']['f1-score'])
                else:
                    reg_dict['1_precision'].append(None)
                    reg_dict['1_recall'].append(None)
                    reg_dict['1_f1-score'].append(None)
                reg_dict['accuracy'].append(cl_dict['accuracy'])
            else:
                reg_dict['0_precision'].append('error')
                reg_dict['0_recall'].append('error')
                reg_dict['0_f1-score'].append('error')
                reg_dict['1_precision'].append('error')
                reg_dict['1_recall'].append('error')
                reg_dict['1_f1-score'].append('error')
                reg_dict['accuracy'].append('error')
        res = pd.DataFrame.from_dict(reg_dict, orient='index', columns=reg_cols)
        res = res.round(4)
        res_na = res.isnull().values.any()
        if res_na:
            res = res.fillna('error')
        template_params = {
            'desc': desc_num + '. ' +
                    'При расчете регрессии пары данных зависимой и независимой переменных используются для тренировки модели '
                    '(подбор модели, минимизирующей неточность прогноза). '
                    'error в качестве значения означает, что в зависимой переменной '
                    'наблюдаются результаты, принадлежащие '
                    'только одному классу (0 или 1), или количество объектов, принадлежащих к одному из классов, меньше 2',
            'col_title': res.columns.tolist(),
            'row_num': [[res.index.tolist()[i], i] for i in range(0, len(res.index.tolist()))],
            'data': res.values.tolist(),
            'data_len': [i for i in range(0, len(res.columns))],
            'p_cond': False,
            'graph_option': False
        }
        res_dict['value'].append(template_params)
    return res_dict, [None, None]

# generate dictionary for clusterization 1
def gen_clusterization_1(file):
    df = file.copy()
    res_dict = {
        'title': 'Кластерный анализ 1',
        'desc': 'Кластерный анализ на основе построения дендрограммы',
        'value': []
    }
    ax = plt.figure(figsize=(50, 8))
    ax_axes = plt.axes()
    dendrogram = sch.dendrogram(sch.linkage(df, method="ward"), ax=ax_axes, labels=df.index.tolist())
    color_list = []
    for i in dendrogram.get('leaves_color_list'):
        if i not in color_list:
            color_list.append(i)
    msg_legend = ''
    for i in color_list:
        msg_legend += str(i) + '\n'
    ax = ax.add_axes(ax_axes)
    plt.title('Дендрограмма')
    plt.xlabel('Карикатура')
    plt.ylabel('Евклидово расстояние')
    plt.legend([msg_legend], loc='upper left')
    plt.tight_layout()
    cluster_index_dict = dict()
    index_list = dendrogram.get('ivl')
    color_list = dendrogram.get('leaves_color_list')
    for i in range(0, len(index_list)):
        cluster_index_dict[index_list[i]] = color_list[i]
    res = [cluster_index_dict[i] for i in df.index.tolist()]
    res = pd.DataFrame(res, index=df.index.tolist(), columns=['Кластер']).T
    template_params = {
        'desc': 'В таблице отображена принадлежность определенных кластеров для каждой карикатуры (строки в матрице). '
        'Для нахождения кластеров использовался ward метод - минимизация вариации в каждом кластере. '
        'Разделение кластеров было произведено по цветам листьев получившейся дендрограммы. '
        'В легенде дендрограммы названия кластеров отображены в соответствии с их очередностью появления (слева направо)',
        'col_title': res.columns.tolist(),
        'row_num': [[res.index.tolist()[i], i] for i in range(0, len(res.index.tolist()))],
        'data': res.values.tolist(),
        'data_len': [i for i in range(0, len(res.columns))],
        'p_cond': False,
        'graph_option': True
    }
    res_dict['value'].append(template_params)
    return res_dict, [ax]

# generate dictionary for clusterization 2
def gen_clusterization_2(file):
    df = file.copy()
    df_eng = df[df['1.3.1']==True]
    df_ru = df[df['1.3.1']==False]
    res_dict = {
        'title': 'Кластерный анализ 2',
        'desc': 'Кластерный анализ на основе построения дендрограммы',
        'value': []
    }
    axes = []
    for data, desc_num in [[df_eng,
                            'Основано на данных подгруппы eng'],
                           [df_ru,
                            'Основано на данных подгруппы ru']]:
        ax = plt.figure(figsize=(50, 8))
        ax_axes = plt.axes()
        dendrogram = sch.dendrogram(sch.linkage(data, method="ward"), ax=ax_axes, labels=data.index.tolist())
        color_list = []
        for i in dendrogram.get('leaves_color_list'):
            if i not in color_list:
                color_list.append(i)
        msg_legend = ''
        for i in color_list:
            msg_legend += str(i) + '\n'
        ax = ax.add_axes(ax_axes)
        plt.title('Дендрограмма')
        plt.xlabel('Карикатура')
        plt.ylabel('Евклидово расстояние')
        plt.legend([msg_legend], loc='upper left')
        plt.tight_layout()
        cluster_index_dict = dict()
        index_list = dendrogram.get('ivl')
        color_list = dendrogram.get('leaves_color_list')
        for i in range(0, len(index_list)):
            cluster_index_dict[index_list[i]] = color_list[i]
        res = [cluster_index_dict[i] for i in data.index.tolist()]
        res = pd.DataFrame(res, index=data.index.tolist(), columns=['Кластер']).T
        template_params = {
            'desc': 'В таблице отображена принадлежность определенных кластеров для каждой карикатуры (строки в матрице). '
                    'Для нахождения кластеров использовался ward метод - минимизация вариации в каждом кластере. '
                    'Разделение кластеров было произведено по цветам листьев получившейся дендрограммы. '
                    'В легенде дендрограммы названия кластеров отображены в соответствии с их очередностью появления (слева направо)' + '. ' +
                    desc_num,
            'col_title': res.columns.tolist(),
            'row_num': [[res.index.tolist()[i], i] for i in range(0, len(res.index.tolist()))],
            'data': res.values.tolist(),
            'data_len': [i for i in range(0, len(res.columns))],
            'p_cond': False,
            'graph_option': True
        }
        res_dict['value'].append(template_params)
        axes.append(ax)
    return res_dict, axes