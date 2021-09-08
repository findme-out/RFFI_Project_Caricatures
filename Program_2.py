import os
import pandas as pd


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
    df = file.agg(['mean', 'median', 'std', 'var'])
    path = path_to_csv[:(path_to_csv.rfind('/')) + 1]
    temp = 'отчет_статистика'
    index = 1
    # check for existing files with such name in the folder
    while os.path.exists(path + temp + '.html'):
        temp = 'отчет_статистика' + '_' + str(index)
        index += 1
    df.to_html(path + temp + '.html')