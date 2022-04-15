import json
import os
import glob
import shutil
from io import StringIO

if __name__ == '__main__':
    os.chdir('/Users/ludmilamalomuz/Documents')
    #files = glob.glob('*.pdf')
    docs = ('*.pdf', '*.docx', '*.doc')
    #images = ('*.jpg', '*.jpeg', '*.png') 
    files_grabbed = []
    for files in docs:
        print(glob.glob(files))
        files_grabbed.extend(glob.glob(files))    
    with open('merged.pdf', 'w+') as merged_pdf:
        for file in files_grabbed:
            document = open(file, encoding = "ISO-8859-1")
            shutil.copyfileobj(document, merged_pdf)
            document.close()
            merged_pdf.write("\r\n")
    
    
    """
    io = StringIO()
    try:
        with open('sample.json', 'r') as f:
            data = json.loads(f.read())
            dumped_values = json.dumps(data, sort_keys=True, indent=4)
            print("Dumped values: "+dumped_values)
            #io.getValue()
        output = ','.join([*data[0]])
        
        print(output)
        
        for obj in data:
            output += f'\n{obj["Name"]},{obj["Contact"]},{obj["Age"]}'

        with open('output.csv', 'w') as f:
            f.write(output)
    except Exception as ex:
        print(f'Error: {str(ex)}')
        """