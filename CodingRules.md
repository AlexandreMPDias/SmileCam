[![N|Solid](https://i.imgur.com/rUMbDaZ.png)](https://cyberlabs.com.br)  
    
    
  # Project Structure  
    
    The project structure was created based on [python-guide.org](http://docs.python-guide.org/en/latest/writing/structure/)  
    Unless it is said otherwise in this ReadMe, follow **python-guide** completly
    
  ### Structure  
  Directory  | Description  
  ------------- | -------------  
  root | .  
  project_info  | Contain files with information about the project  
  config | Contain all config files needed by the project  
  test | Contains Python scripts for automated tests
  docs | Contains all the documentation for the Project
  src  | Contains the script files and data files  
  src/data | Contain all data files needed by the project   
  src/constant | Contain Python scripts with only variable declarations  
  src/modules | Contain Python scripts that is the project itself  
    
  ### Directory Tree  (with sample files)
  ```   
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
  			┬  
  			├ checkpoints  
  				┬  
  				└ epoch_75.hdf5  
  			├ face_images  
  				┬  
  				└  face.png  
  			└ haarcascade_frontalface_default.xml  
  		├ modules  
  			┬  
  		 	├ script1.py  
              └ script2.py  
  		├ constant  
  			┬  
  			├ general.py  
  			└ sql.py  
  		└ main.py  
  	├ config    
  		┬    
  	 	└ config.json  
  	└ test    
  		┬    
  	 	└ testing.py 
  ```  

  ### In-Depth Description

  **./project_info**  
  *Contain files with information about the project*  
  This directory should contain all sorts of information about the project. Such as version, bug reports,  
  changes made, comments, todo lists, how to run, etc...  
  
  **./src**  
  *Contain the script files and data files*  
  This directory should contain [ main.py ], [ data ], [ modules ], [ constant ].  
  Whatever file, that has following statement, should be in here 
  ```py
    if __name__ == "__main__":
        ...
  ``` 
  
  **./config**  
  *Contain all config files needed by the project*  
  This directory should contain [ main.py ], [ data ], [ modules ], [ constant ].  
  
  **./src/data**  
  *Contain all data files needed by the project*  
  This directory should contain all the data files need to run the application. Such as png's, gif's, csv's, etc.  

  **./src/constant**  
  *Contain Python scripts with only variable declarations *  
  This directory should contain python scripts with only constant declarations inside.  
  A constant may be just a path, of the file itself.  

  **./src/modules**  
  *Contain Python scripts that is the project itself*  
  This directory should contain python scripts necessary to run the application. Such as server.py, ad_feed.py, etc...  

  **./test**  
  *Containt Python scripts for automated tests*  
  This directory should contain all the python scripts necessary to run automated tests.  
  This tests should contain even the most basic tests to ensure the environment integrity and to assist in setting up new environment


  # Variables and Files  
  ### Naming Variables:  
  **Class(es):**  UpperCamelCase.  
  *Example(s):  
  MetaServer  
  Process  
  ProcessGenerator  
  WriterOfStuff*  
    
  **Method(s)**/**Function(s) :** lowerCamelCase.    
  *Example(s):  
  createServer(...)  
  writeToFile(...)  
  createHeatMap(...)*  
    
  **Constant(s) :** CAPSLOCK, words divided by <u>underscore</u>, with public/private prefix  
  <i>Example(s):  
  SQL_PASSWORD = PUBLIC_DIR + "1234"  
  SQL_HOST = PUBLIC_DIR + "0:0:0:0"  
  SERVER_KEY = PUBLIC_DIR + "12345"  
  HAARCASCADE = PRIVATE_DIR + "haarcascade.xml" </i>  
  <i><b>Note: PRIVATE_DIR and PUBLIC_DIR should be declared inside constant/general.py </i></b>
    
  **Data File(s) :** lowercase, words divided by <u>underscore</u>   
  <i>Example(s):  
  haarcascade_frontalface_default.xml  
  log.txt  
  smile.png  
  file.csv</i>  
    
  **Python Script(s) :** lowercase, words divided by <u>underscore</u>    
  *Example(s): 
   main.py  
   server.py  
   webcam_server.py*  
    
  ### Declaring Variables:  
    
  **Class(es):**  inside class_name.py  
  *Example(s):  
  MetaServer inside meta_server.py  
  Process inside process.py  
  ProcessGenerator inside process_generator.py  
  WriterOfStuff inside writer_of_stuff.py*  
    
  **Constant(s) :** inside constant/*.py  
  *Example(s):  
  SQL_PASSWORD inside constant/sql.py  
  SQL_HOST inside constant/sql.py  
  SERVER_KEY inside constant/server.py  
  HAARCASCADE inside constant/general.py*  
    
  **Data File(s) :** inside src/data or src/data's subdirectory  
  *Example(s):  
  src/data/haarcascade.xml  
  src/data/log.txt  
  smile.png  
  src/data/csv/file.csv*  
    
  **Python Script(s) :** inside src/modules or src/modules's subdirectory  
  *Example(s):  
  src/modules/server.py  
  src/modules/webcam_server.py  
  src/modules/heatmap/load.py*  
  <i><b>Note: except main.py, that stays inside ./src</i></b>  
