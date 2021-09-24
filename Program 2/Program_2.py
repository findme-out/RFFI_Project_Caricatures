import os
import pandas as pd
from chameleon import PageTemplateLoader

# generate html file according to the template
def generate_html(output_file_name, path_to_csv, template_params, template_name='template.html'):
    path_to_template = os.path.dirname(os.path.abspath(__file__))
    path_to_template = path_to_template + '/' + "templates"
    temp_path = ""
    for i in path_to_template:
        if i == '\\':
            temp_path += '/'
        else:
            temp_path += i
    path_to_template = temp_path
    templates = PageTemplateLoader(path_to_template)
    template = templates[template_name]
    # check for existing files with such name in the folder
    path = path_to_csv
    temp_file_name = output_file_name
    index = 1
    while os.path.exists(path + temp_file_name + '.html'):
        temp_file_name = output_file_name + '_' + str(index)
        index += 1
    with open(path + temp_file_name + '.html', 'w', encoding='utf-8') as file:
        file.write(template(title=template_params['title'], col_title=template_params['col_title'], row_num=template_params['row_num'],
                            data=template_params['data'], data_len=template_params['data_len']))

# generate dictionary for statistics 1
def gen_statistics_1(file):
    df = file.agg(['mean', 'median', 'std', 'var'])
    template_params = {
        'title': 'Статистический анализ 1',
        'col_title': list(df.columns),
        'row_num': [['mean', 0], ['median', 1], ['std', 2], ['var', 3]],
        'data': df.values.tolist(),
        'data_len': [i for i in range(0, len(df.columns))]
    }
    return template_params

# generate dictionary for statistics 2
def gen_statistics_2(file):
    df_eng = file[file['1.3.1'] == True].agg(['mean', 'median', 'std', 'var'])
    df_ru = file[file['1.3.1'] == False].agg(['mean', 'median', 'std', 'var'])
    col_title = []
    if len(df_eng.columns) != 0:
        col_title = list(df_eng.columns)
    else:
        col_title = list(df_ru.columns)
    template_params = {
        'title': 'Статистический анализ 2',
        'col_title': col_title,
        'row_num': [['mean_eng', 0], ['median_eng', 1], ['std_eng', 2], ['var_eng', 3], ['mean_ru', 4], ['median_ru', 5], ['std_ru', 6], ['var_ru', 7]],
        'data': df_eng.values.tolist() + df_ru.values.tolist(),
        'data_len': [i for i in range(0, len(col_title))]
    }
    return template_params

# generate dictionary for statistics 3
def gen_statistics_3(file):
    df_eng = file[file['1.3.1'] == True]
    df_eng_1 = df_eng[df_eng['2.1.1'] == True].agg(['mean', 'median', 'std', 'var'])
    df_eng_2 = df_eng[df_eng['2.1.2'] == True].agg(['mean', 'median', 'std', 'var'])
    df_eng_3 = df_eng[df_eng['2.1.3'] == True].agg(['mean', 'median', 'std', 'var'])
    df_eng_4 = df_eng[df_eng['2.1.4'] == True].agg(['mean', 'median', 'std', 'var'])
    df_ru = file[file['1.3.1'] == False]
    df_ru_1 = df_ru[df_ru['2.1.1'] == True].agg(['mean', 'median', 'std', 'var'])
    df_ru_2 = df_ru[df_ru['2.1.2'] == True].agg(['mean', 'median', 'std', 'var'])
    df_ru_3 = df_ru[df_ru['2.1.3'] == True].agg(['mean', 'median', 'std', 'var'])
    df_ru_4 = df_ru[df_ru['2.1.4'] == True].agg(['mean', 'median', 'std', 'var'])
    col_title = []
    if len(df_eng.columns) != 0:
        col_title = list(df_eng.columns)
    else:
        col_title = list(df_ru.columns)
    template_params = {
        'title': 'Статистический анализ 3',
        'col_title': col_title,
        'row_num': [['mean_eng_1', 0], ['median_eng_1', 1], ['std_eng_1', 2], ['var_eng_1', 3], ['mean_ru_1', 4], ['median_ru_1', 5], ['std_ru_1', 6], ['var_ru_1', 7],
                    ['mean_eng_2', 8], ['median_eng_2', 9], ['std_eng_2', 10], ['var_eng_2', 11], ['mean_ru_2', 12], ['median_ru_2', 13], ['std_ru_2', 14], ['var_ru_2', 15],
                    ['mean_eng_3', 16], ['median_eng_3', 17], ['std_eng_3', 18], ['var_eng_3', 19], ['mean_ru_3', 20], ['median_ru_3', 21], ['std_ru_3', 22], ['var_ru_3', 23],
                    ['mean_eng_4', 24], ['median_eng_4', 25], ['std_eng_4', 26], ['var_eng_4', 27], ['mean_ru_4', 28], ['median_ru_4', 29], ['std_ru_4', 30], ['var_ru_4', 31]],
        'data': df_eng_1.values.tolist() + df_ru_1.values.tolist() + df_eng_2.values.tolist() + df_ru_2.values.tolist() +
        df_eng_3.values.tolist() + df_ru_3.values.tolist() + df_eng_4.values.tolist() + df_ru_4.values.tolist(),
        'data_len': [i for i in range(0, len(col_title))]
    }
    return template_params

# handle statistics
def work_with_format_csv(path_to_csv):
    temp_path = ""
    for i in path_to_csv:
        if i == '\\':
            temp_path += '/'
        else:
            temp_path += i
    path_to_csv = temp_path
    file = pd.read_csv(path_to_csv, sep=';')
    file = file.drop(file.columns[0], axis=1)
    path = path_to_csv[:(path_to_csv.rfind('/')) + 1]
    template_params = gen_statistics_1(file)
    generate_html(template_params['title'], path, template_params)
    template_params = gen_statistics_2(file)
    generate_html(template_params['title'], path, template_params)
    template_params = gen_statistics_3(file)
    generate_html(template_params['title'], path, template_params)