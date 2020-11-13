# imports
import zipfile
import os

# function that unzips files from zip-archive into a folder with the same name as archive
def zip_to_folder(path_to_zip_files):
    
    files = os.listdir(path_to_zip_files)
    print("Following files were unzipped:")
    for file in files:
        
        if file.endswith('.zip'):
            print('* ' + file)
            os.path.splitext(os.path.basename(file))[0]
            filePath = path_to_zip_files + '/' + file
            zip_file = zipfile.ZipFile(filePath)
            path_to_unzip_files = path_to_zip_files + '/' + os.path.splitext(os.path.basename(file))[0]

            for names in zip_file.namelist():
                zip_file.extract(names, path_to_unzip_files)

    print("Done")

zip_to_folder('W:projapps/dxf_einmessdaten/ungeprueft/RB3')
