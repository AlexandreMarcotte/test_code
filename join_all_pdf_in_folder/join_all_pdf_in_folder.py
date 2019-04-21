import os
from natural_sorting import natural_keys

all_pdf = []

base_path = '/home/alex/Documents/poly_H2019/interface/th'
sub_folders_lst = os.listdir(base_path)
sub_folders_lst.sort(key=natural_keys)

for folder_name in sub_folders_lst:
    print('FOLDER_NAME: ', folder_name)
    sub_folder_path = os.path.join(base_path, folder_name)
    pdf_in_sub_folder = os.listdir(sub_folder_path)
    all_pdf += [os.path.join(base_path, folder_name, pdf_name) \
                for pdf_name in pdf_in_sub_folder]

all_pdf = ["'" + pdf_name + "'" for pdf_name in all_pdf]
all_pdf_str = ' '.join(all_pdf)
print(all_pdf_str)

os.system(f'pdftk {all_pdf_str} cat output \'/home/alex/Downloads/interface_all_pdf.pdf\'')



# import subprocess
# subprocess.check_call(['ls'])
