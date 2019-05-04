import os
from natural_sorting import natural_keys
# from . import add_apostrophes


# Add apostrophes to pdf name (right format for merging tool)
def add_apostrophes(all_pdf: list) -> str:
    """Take a list of pdf str and add apostrophes to each of them and
        put them all together in one single big str"""
    all_pdf = ["'" + pdf_name + "'" for pdf_name in all_pdf]
    all_pdf_str = ' '.join(all_pdf)
    print(all_pdf_str)
    return all_pdf_str


def merge_pdf(name_of_pdf_to_merge: str, output_file_name: str)-> None:
    """Merge pdf from with a command line request to the module pdftk"""
    os.system(f'pdftk {name_of_pdf_to_merge} cat output {output_file_name}')


all_pdf = []

base_path = '/home/alex/Documents/poly_H2019/interface/th'
sub_folders_lst = os.listdir(base_path)
sub_folders_lst.sort(key=natural_keys)

for folder_name in sub_folders_lst:
    print('FOLDER_NAME: ', folder_name)
    sub_folder_path = os.path.join(base_path, folder_name)
    pdf_in_sub_folder = os.listdir(sub_folder_path)

    # Create complete file name and use only .pdf file extention type
    pdf_in_sub_folder = [os.path.join(sub_folder_path, pdf_name)
                         for pdf_name in pdf_in_sub_folder
                         if 'pdf' in pdf_name]

    pdf_in_sub_folder_str = add_apostrophes(pdf_in_sub_folder)
    output_sub_file_name = os.path.join(sub_folder_path, 'sub_merge.pdf')
    merge_pdf(pdf_in_sub_folder_str, output_sub_file_name)

    all_pdf += pdf_in_sub_folder

all_pdf_str = add_apostrophes(all_pdf)
output_file_name = '\'/home/alex/Documents/poly_H2019/interface/interface_all_pdf.pdf\''


merge_pdf(all_pdf_str, output_file_name)


# import subprocess
# subprocess.check_call(['ls'])
