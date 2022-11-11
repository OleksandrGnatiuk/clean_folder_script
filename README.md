### Clean-folder script package.
This python script can clean any folder, it sorts all files in folder according to file's suffix.

> How to install package?
> _`pip install /path/to/clean-folder_script/folder`_    
>    (where is file setup.py)

> How to use clean-folder script?
>  _`clean-folder /path/to folder/you want to clean/`_

+ if this folder is not exist, you'll see message in console.
+ The script sorts files according to file's `suffix`.
+ Default folders are `documents`, `images`, `video`, `audio`, `archives`. 
  All files with relevant suffix will be move to these folders;
+ Another files will be move to folder `other`;
+ if these folders was not exist they will be create;
+ The script recursively checks all subfolders and removes all files to the main folder;
+ Empty folders will be delete;
+ Files with kirilic name will be __rename to latin name__;
+ if subfolders involve the files with the same name, this files will be rename - __date-time will be added to file's name__;
+ All archives will be unpack with the same name in folder `archive`;
+ if achive is broken, script will continue its work without unpacking this archive. In console you'll see message about this broken archive;
+ When script finishes clean folder you'll see the report;
  
If any questions, please contact to oleksandr.gnatiuk@gmail.com