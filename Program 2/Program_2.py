import Algorithms
import os
import pandas as pd
from chameleon import PageTemplateLoader

# generate html file according to the template
def generate_html(path_to_csv, template_list, template_name='template.html', output_file_name='Алгоритмы'):
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
        file.write(template(dict_list_list=template_list))


# handle statistics
def work_with_format_csv(path_to_csv, gen_statistics_1=True, gen_statistics_2=True, gen_statistics_3=True):
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
    template_list = []
    if gen_statistics_1:
        template_list.append(Algorithms.gen_statistics_1(file))
    if gen_statistics_2:
        template_list.append(Algorithms.gen_statistics_2(file))
    if gen_statistics_3:
        template_list.append(Algorithms.gen_statistics_3(file))
    generate_html(path, template_list)