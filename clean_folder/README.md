### Clean-folder script package.

![](https://img.shields.io/github/watchers/OleksandrGnatiuk/clean_folder_script?style=social)

---

This script can clean any folders, it sorts all files in folder according to file's extensions.

> How to install this package?
>
> > Please run from the command line: `pip install /path/to/clean-folder_script/folder`  
> >  _(where is setup.py)_

> How to use clean-folder script?
>
> > You have to run from the command line: `clean-folder /path/to folder/you want to clean/`

- [x] if this folder is not exists, you'll see a message in console.
- [x] The script sorts files according to file's extensions.
- [x] Default folders are `documents`, `images`, `video`, `audio` and `archives`.
- [x] if you want to set your own rules of sorting files you have to change __extension_dict__:
  ```python
  extension_dict = {
    "documents": [".doc", ".docx", ".xls", ".xlsx", ".txt", ".pdf"],
    "audio": [".mp3", ".ogg", ".wav", ".amr"],
    "video": [".avi", ".mp4", ".mov", ".mkv"],
    "images": [".jpeg", ".png", ".jpg", ".svg"],
    "archives": [".zip", ".gz", ".tar"],
    }
  ```
- [x] All files with relevant extensions will be moved to these folders;
- [x] Other files will be moved to folder `other`;
- [x] if these folders were not exist its will be created;
- [x] The script recursively checks all subfolders and it moves all files to the main folder;
- [x] Empty folders will be deleted;
- [x] Files with kirilic name will be **renamed to latin name**;
- [x] if subfolders involve the files with the same name, these files will be renamed - **date-time will be added to file's name**;
- [x] All archives will be unpacked to subfolder with the name as archive's name in folder `archive`;
- [x] if archive is broken, script will continue its work without unpacking this archive. In console you'll see message about this broken archive;
- [x] When script finishes to clean folder you'll see the report.

If any questions, please contact to oleksandr.gnatiuk@gmail.com
