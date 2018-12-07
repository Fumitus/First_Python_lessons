import os

for folderName, subfolders, filenames in os.walk('c:\\Andrius'):
	print('The folder is ' + folderName)
	print('The subfolder in ' + folderName + ' are: ' + str(subfolders))
	print('The filenames in ' + folderName + ' are: ' + str(filenames))
	print()

	for subfolder in subfolders:
	    if 'something' in subfolder:
		#os.rmdir(subfolder)
		print('rmdir on ' + subfolder)

	for file in filenames:
	        if file.endswith('.txt'):
		        print('copying file to ' + filenames  + ' to ' subfolder)
