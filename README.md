### Clean-folder script package.
This python script can clean any folder, it sorts all files in folder according to file's suffix.

> How to install this package?
> >_Please can run from the command line: `pip install /path/to/clean-folder_script/folder`_    
>    (where is file setup.py)

> How to use clean-folder script?
>> You need can run from the command line: _`clean-folder /path/to folder/you want to clean/`_

+ [x] if this folder is not exist, you'll see message in console.
+ [X] The script sorts files according to file's `suffix`.
+ [x] Default folders are `documents`, `images`, `video`, `audio`, `archives`. 
+ [x] if you want your own rule of sorting files you need to change `suffix_dict`:
  ``` python
  suffix_dict = {
    "documents": [".doc", ".docx", ".xls", ".xlsx", ".txt", ".pdf"],
    "audio": [".mp3", ".ogg", ".wav", ".amr"],
    "video": [".avi", ".mp4", ".mov", ".mkv"],
    "images": [".jpeg", ".png", ".jpg", ".svg"],
    "archives": [".zip", ".gz", ".tar"],
    }
  ```
+ [x] All files with relevant suffix will be move to these folders;
+ [x] Another files will be move to folder `other`;
+ [x] if these folders was not exist they will be create;
+ [x] The script recursively checks all subfolders and removes all files to the main folder;
+ [x] Empty folders will be delete;
+ [x] Files with kirilic name will be __rename to latin name__;
+ [x] if subfolders involve the files with the same name, this files will be rename - __date-time will be added to file's name__;
+ [x] All archives will be unpack with the same name in folder `archive`;
+ [x] if achive is broken, script will continue its work without unpacking this archive. In console you'll see message about this broken archive;
+ [x] When script finishes clean folder you'll see the report;
  
If any questions, please contact to oleksandr.gnatiuk@gmail.com