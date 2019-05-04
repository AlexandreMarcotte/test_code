import os
from natural_sorting import natural_keys
from typing import List, Dict


# Add apostrophes to pdf name (right format for merging tool)
def add_apostrophes(all_pdf: List[str]) -> str:
    """Take a list of pdf str and add apostrophes to each of them and
        put them all together in one single big str"""
    all_pdf = ["'" + pdf_name + "'" for pdf_name in all_pdf]
    all_pdf_str = ' '.join(all_pdf)
    print(all_pdf_str)
    return all_pdf_str


all_pdf = []

base_path = '/home/alex/Documents/poly_H2019/site_web/TH'
sub_folders_lst = os.listdir(base_path)
sub_folders_lst.sort(key=natural_keys)

for folder_name in sub_folders_lst:
    print('FOLDER_NAME: ', folder_name)
    sub_folder_path = os.path.join(base_path, folder_name)
    pdf_in_sub_folder = os.listdir(sub_folder_path)
    all_pdf += [os.path.join(base_path, folder_name, pdf_name) \
                for pdf_name in pdf_in_sub_folder if 'pdf' in pdf_name]


all_pdf_str = add_apostrophes(all_pdf)
os.system(f'pdftk {all_pdf_str} cat output \'/home/alex/Documents/poly_H2019/site_web/site_web_all_pdf.pdf\'')




