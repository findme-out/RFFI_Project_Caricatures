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
        file.write(template(title=template_params['title'][0], col_title=template_params['col_title'], row_num=template_params['row_num'],
                            data=template_params['data'], data_len=template_params['data_len']))
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
    template_params = {
        'title': ['Статистический анализ 1'],
        'col_title': list(df.columns),
        'row_num': [['mean', 0], ['median', 1], ['std', 2], ['var', 3]],
        'data': df.values.tolist(),
        'data_len': [i for i in range(0, len(df.columns))]
    }
    generate_html('Статистический анализ 1', path, template_params)