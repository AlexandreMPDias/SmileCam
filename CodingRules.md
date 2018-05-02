[![N|Solid](https://i.imgur.com/rUMbDaZ.png)](https://cyberlabs.com.br)

[TOCM]

[TOC]

#Project Structure
###Structure
Directory  | Description
------------- | -------------
root | .
project_info  | Contain files with information about the project
src  | Contain the script files and data files
data | Contain all data files needed by the project
config | Contain all config files needed by the project
constant | Contain Python scripts containing constant variables declaration
modules | Contain Python scripts that is the project itself

###Directory Tree
<pre> 
root
	 ┬  
	 ├ project_info  
			 ┬  
		 	├ changes_log.txt
		 	├ requirements.txt
		 	└ version.txt
	├ src  
			┬ 
			├ data  
					┬ checkpoints
							┬
							└ epoch_75.hdf5
					├ face_images
							┬
							└  face.png
					└ haarcascade_frontalface_default.xml
			 ├ modules
				 	├ scripts.py
			 ├ modules
					 ├ general.py
					 └ sql.py
			 └ main.py
	 ├ config  
			 ┬  
		 	└ config.json
</pre>

#Variables and Files
###Naming Variables:
**Class:**  UpperCamelCase.
*Example(s):  MetaServer, Process, ProcessGenerator, WriterOfStuff*

**Methods / Functions : ** lowerCamelCase.
*Example(s):  createServer(...), writeToFile(...), createHeatMap(...)*

**Constants :** CAPSLOCK, words divided by <u>underscore</u>, with public/private prefix
*Example(s): SQL_PASSWORD = PUBLIC_DIR + "1234",
SQL_HOST = PUBLIC_DIR + "0:0:0:0",
SERVER_KEY = PUBLIC_DIR + "12345",
HAARCASCADE = PRIVATE_DIR + "haarcascade.xml" *

**Data Files :** lowercase
*Example(s): haarcascade.xml, log.txt, smile.png, file.csv*

**Python Scripts :** lowercase, word divided by <u>underscore</u>  
*Example(s): main.py, server.py, webcam_server.py*

###Declaring Variables:

**Class:**  inside class_name.py
*Example(s):  MetaServer inside meta_server.py, Process inside process.py, ProcessGenerator inside process_generator.py, WriterOfStuff inside writer_of_stuff.py*

**Constants :** inside constants/*.py
*Example(s): SQL_PASSWORD inside constants/sql.py, SQL_HOST inside constants/sql.py, SERVER_KEY inside constants/server.py, HAARCASCADE inside constants/general.py*

**Data Files :** inside src/data or src/data's subdirectory
*Example(s): src/data/haarcascade.xml, src/data/log.txt, smile.png, src/data/csv/file.csv*

**Python Scripts :** inside src/modules or src/modules's subdirectory
*Example(s): src/modules/server.py, src/modules/webcam_server.py, src/modules/heatmap/load.py*
Note: except main.py, that stays inside ./src
