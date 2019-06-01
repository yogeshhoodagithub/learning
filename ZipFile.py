# -*- coding: utf-8 -*-
"""
Created on Mon May 27 11:41:40 2019

@author: GUR15277
"""

import os
import zipfile
#import time
#timestr = time.strftime("%Y%m%d-%H%M%S")

#fileName='report'+timestr+'.zip'
#print(fileName)

fantasy_zip = zipfile.ZipFile('C:\\Users\\gur15277\\Desktop\\MyProject\\reports.zip', 'w')
 

for folder, subfolders, files in os.walk('D:\\jenkins\\workspace\\'):
 
    for file in files:
        if file.endswith('.html'):
#            fantasy_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), 'C:\\Stories\\Fantasy'), compress_type = zipfile.ZIP_DEFLATED)
            fantasy_zip.write(os.path.join(folder, file), file, compress_type = zipfile.ZIP_DEFLATED)


fantasy_zip.close()
