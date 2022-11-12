### Clean-folder script package.
![](https://img.shields.io/aur/last-modified/clean-folder?color=orange)
____
This python script can clean any folders, it sorts all files in folder according to file's suffix.

> How to install this package?
> > Please can run from the command line:  `pip install /path/to/clean-folder_script/folder`    
>    _(where is setup.py)_

> How to use clean-folder script?
>> You need run from the command line:  `clean-folder /path/to folder/you want to clean/`

+ [x] if this folder is not exists, you'll see a message in console.
+ [x] The script sorts files according to file's `suffix`.
+ [x] Default folders are `documents`, `images`, `video`, `audio` and `archives`. 
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
+ [x] if these folders were not exist they will be created;
+ [x] The script recursively checks all subfolders and it moves all files to the main folder;
+ [x] Empty folders will be deleted;
+ [x] Files with kirilic name will be __renamed to latin name__;
+ [x] if subfolders involve the files with the same name, these files will be renamed - __date-time will be added to file's name__;
+ [x] All archives will be unpacked with the same name in folder `archive`;
+ [x] if achive is broken, script will continue its work without unpacking this archive. In console you'll see message about this broken archive;
+ [x] When script finishes clean folder you'll see the report.
  
If any questions, please contact to oleksandr.gnatiuk@gmail.com