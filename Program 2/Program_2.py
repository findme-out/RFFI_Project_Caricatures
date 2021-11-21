import Algorithms
import os
import pandas as pd
from chameleon import PageTemplateLoader
import base64

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
def work_with_format_csv(path_to_csv, gen_code_feature_desc=True, gen_statistics_1=True, gen_statistics_2=True, gen_statistics_3=True, gen_statistics_4=True,
                         gen_statistics_5=True, gen_correlation_1=True, gen_correlation_2=True, gen_regression_1=True, gen_regression_2=True,
                         gen_clusterization_1=True, gen_clusterization_2=True):
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
    if gen_code_feature_desc:
        temp_dict, fig_list = Algorithms.gen_code_feature_desc(file)
        temp_path = path + 'code_feature_'
        for i in range(0, len(fig_list)):
            if fig_list[i] is not None:
                temp_temp_path = temp_path + str(i) + '.png'
                fig_list[i].savefig(temp_temp_path)
                with open(temp_temp_path, 'rb') as image_file:
                    encoded_string = base64.b64encode(image_file.read())
                fig_list[i] = encoded_string
        for i in range(0, len(temp_dict['value'])):
            if temp_dict['value'][i]['graph_option']:
                temp_dict['value'][i]['graph'] = fig_list[i]
        template_list.append(temp_dict)
    if gen_statistics_1:
        temp_dict, fig_list = Algorithms.gen_statistics_1(file)
        temp_path = path + 'stat_1_'
        for i in range(0, len(fig_list)):
            if fig_list[i] is not None:
                temp_temp_path = temp_path + str(i) + '.png'
                fig_list[i].savefig(temp_temp_path)
                with open(temp_temp_path, 'rb') as image_file:
                    encoded_string = base64.b64encode(image_file.read())
                fig_list[i] = encoded_string
        for i in range(0, len(temp_dict['value'])):
            if temp_dict['value'][i]['graph_option']:
                temp_dict['value'][i]['graph'] = fig_list[i]
        template_list.append(temp_dict)
        print('Completed statistics 1 successfully')
    if gen_statistics_2:
        temp_dict, fig_list = Algorithms.gen_statistics_2(file)
        temp_path = path + 'stat_2_'
        for i in range(0, len(fig_list)):
            if fig_list[i] is not None:
                temp_temp_path = temp_path + str(i) + '.png'
                fig_list[i].savefig(temp_temp_path)
                with open(temp_temp_path, 'rb') as image_file:
                    encoded_string = base64.b64encode(image_file.read())
                fig_list[i] = encoded_string
        for i in range(0, len(temp_dict['value'])):
            if temp_dict['value'][i]['graph_option']:
                temp_dict['value'][i]['graph'] = fig_list[i]
        template_list.append(temp_dict)
        print('Completed statistics 2 successfully')
    if gen_statistics_3:
        temp_dict, fig_list = Algorithms.gen_statistics_3(file)
        temp_path = path + 'stat_3_'
        for i in range(0, len(fig_list)):
            if fig_list[i] is not None:
                temp_temp_path = temp_path + str(i) + '.png'
                fig_list[i].savefig(temp_temp_path)
                with open(temp_temp_path, 'rb') as image_file:
                    encoded_string = base64.b64encode(image_file.read())
                fig_list[i] = encoded_string
        for i in range(0, len(temp_dict['value'])):
            if temp_dict['value'][i]['graph_option']:
                temp_dict['value'][i]['graph'] = fig_list[i]
        template_list.append(temp_dict)
        print('Completed statistics 3 successfully')
    if gen_statistics_4:
        temp_dict, fig_list = Algorithms.gen_statistics_4(file)
        temp_path = path + 'stat_4_'
        for i in range(0, len(fig_list)):
            if fig_list[i] is not None:
                temp_temp_path = temp_path + str(i) + '.png'
                fig_list[i].savefig(temp_temp_path)
                with open(temp_temp_path, 'rb') as image_file:
                    encoded_string = base64.b64encode(image_file.read())
                fig_list[i] = encoded_string
        for i in range(0, len(temp_dict['value'])):
            if temp_dict['value'][i]['graph_option']:
                temp_dict['value'][i]['graph'] = fig_list[i]
        template_list.append(temp_dict)
        print('Completed statistics 4 successfully')
    if gen_statistics_5:
        temp_dict, fig_list = Algorithms.gen_statistics_5(file)
        temp_path = path + 'stat_5_'
        for i in range(0, len(fig_list)):
            if fig_list[i] is not None:
                temp_temp_path = temp_path + str(i) + '.png'
                fig_list[i].savefig(temp_temp_path)
                with open(temp_temp_path, 'rb') as image_file:
                    encoded_string = base64.b64encode(image_file.read())
                fig_list[i] = encoded_string
        for i in range(0, len(temp_dict['value'])):
            if temp_dict['value'][i]['graph_option']:
                temp_dict['value'][i]['graph'] = fig_list[i]
        template_list.append(temp_dict)
        print('Completed statistics 5 successfully')
    if gen_correlation_1:
        temp_dict, fig_list = Algorithms.gen_correlation_1(file)
        temp_path = path + 'corr_1_'
        for i in range(0, len(fig_list)):
            if fig_list[i] is not None:
                temp_temp_path = temp_path + str(i) + '.png'
                fig_list[i].figure.savefig(temp_temp_path)
                with open(temp_temp_path, 'rb') as image_file:
                    encoded_string = base64.b64encode(image_file.read())
                fig_list[i] = encoded_string
        for i in range(0, len(temp_dict['value'])):
            if temp_dict['value'][i]['graph_option']:
                temp_dict['value'][i]['graph'] = fig_list[i]
        template_list.append(temp_dict)
        print('Completed correlation 1 successfully')
    if gen_correlation_2:
        temp_dict, fig_list = Algorithms.gen_correlation_2(file)
        temp_path = path + 'corr_2_'
        for i in range(0, len(fig_list)):
            if fig_list[i] is not None:
                temp_temp_path = temp_path + str(i) + '.png'
                fig_list[i].figure.savefig(temp_temp_path)
                with open(temp_temp_path, 'rb') as image_file:
                    encoded_string = base64.b64encode(image_file.read())
                fig_list[i] = encoded_string
        for i in range(0, len(temp_dict['value'])):
            if temp_dict['value'][i]['graph_option']:
                temp_dict['value'][i]['graph'] = fig_list[i]
        template_list.append(temp_dict)
        print('Completed correlation 2 successfully')
    if gen_regression_1:
        temp_dict, fig_list = Algorithms.gen_regression_1(file)
        temp_path = path + 'regr_1_'
        for i in range(0, len(fig_list)):
            if fig_list[i] is not None:
                temp_temp_path = temp_path + str(i) + '.png'
                fig_list[i].figure.savefig(temp_temp_path)
                with open(temp_temp_path, 'rb') as image_file:
                    encoded_string = base64.b64encode(image_file.read())
                fig_list[i] = encoded_string
        for i in range(0, len(temp_dict['value'])):
            if temp_dict['value'][i]['graph_option']:
                temp_dict['value'][i]['graph'] = fig_list[i]
        template_list.append(temp_dict)
        print('Completed regression 1 successfully')
    if gen_regression_2:
        temp_dict, fig_list = Algorithms.gen_regression_2(file)
        temp_path = path + 'regr_2_'
        for i in range(0, len(fig_list)):
            if fig_list[i] is not None:
                temp_temp_path = temp_path + str(i) + '.png'
                fig_list[i].figure.savefig(temp_temp_path)
                with open(temp_temp_path, 'rb') as image_file:
                    encoded_string = base64.b64encode(image_file.read())
                fig_list[i] = encoded_string
        for i in range(0, len(temp_dict['value'])):
            if temp_dict['value'][i]['graph_option']:
                temp_dict['value'][i]['graph'] = fig_list[i]
        template_list.append(temp_dict)
        print('Completed regression 2 successfully')
    if gen_clusterization_1:
        temp_dict, fig_list = Algorithms.gen_clusterization_1(file)
        temp_path = path + 'clust_1_'
        for i in range(0, len(fig_list)):
            if fig_list[i] is not None:
                temp_temp_path = temp_path + str(i) + '.png'
                fig_list[i].figure.savefig(temp_temp_path)
                with open(temp_temp_path, 'rb') as image_file:
                    encoded_string = base64.b64encode(image_file.read())
                fig_list[i] = encoded_string
        for i in range(0, len(temp_dict['value'])):
            if temp_dict['value'][i]['graph_option']:
                temp_dict['value'][i]['graph'] = fig_list[i]
        template_list.append(temp_dict)
        print('Completed clusterization 1 successfully')
    if gen_clusterization_2:
        temp_dict, fig_list = Algorithms.gen_clusterization_2(file)
        temp_path = path + 'clust_2_'
        for i in range(0, len(fig_list)):
            if fig_list[i] is not None:
                temp_temp_path = temp_path + str(i) + '.png'
                fig_list[i].figure.savefig(temp_temp_path)
                with open(temp_temp_path, 'rb') as image_file:
                    encoded_string = base64.b64encode(image_file.read())
                fig_list[i] = encoded_string
        for i in range(0, len(temp_dict['value'])):
            if temp_dict['value'][i]['graph_option']:
                temp_dict['value'][i]['graph'] = fig_list[i]
        template_list.append(temp_dict)
        print('Completed clusterization 2 successfully')
    generate_html(path, template_list)