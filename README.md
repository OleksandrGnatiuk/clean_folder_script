## Clean-folder script package

<p> This script can sort all files in folder. It sorts all files according to file's extensions. <br>
Files with Cyrillic name will be renamed to Latin name. <br>
All files will be replaced to folders: "document", "music", "video", "images", "archives", "other", etc.
You can change the list of these folders and set your own rules of sorting files.</p>

## Installation

Download package, unpack it and use next command to install it from unpacked folder:

```bash
pip install -e .
```

## How to use clean-folder script?

You have to run from the command line: <br>

```bash
clean-folder <path to folder you want to clean>
```

- [x] if this folder is not exists, you'll see a message in console.
- [x] The script sorts files according to file's extensions.
- [x] Default folders are `documents`, `images`, `video`, `audio` and `archives`.
- [x] if you want to set your own rules of sorting files you have to change **extension_dict**:

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
- [x] Other files will be replaced to folder `other`;
- [x] if these folders were not exist its will be created;
- [x] The script recursively checks all subfolders and it moves all files to the main folder;
- [x] Empty folders will be deleted;
- [x] Files with Cyrillic name will be **renamed to Latin name**;
- [x] if subfolders involve the files with the same name, these files will be renamed - **date-time will be added to file's name**;
- [x] All archives will be unpacked to subfolder with the name as archive's name in folder `archive`;
- [x] if archive is broken, script will continue its work without unpacking this archive. In console you'll see message about this broken archive;
- [x] When script finishes to clean folder, you'll see the report.

If any questions, please contact to oleksandr.gnatiuk@gmail.com
