import collections
import shutil
import sys
from datetime import datetime
from pathlib import Path

# Dictionary for set the rules of sorting files:
extension_dict = {
    "documents": [".doc", ".docx", ".xls", ".xlsx", ".txt", ".pdf"],
    "audio": [".mp3", ".ogg", ".wav", ".amr"],
    "video": [".avi", ".mp4", ".mov", ".mkv"],
    "images": [".jpeg", ".png", ".jpg", ".svg"],
    "archives": [".zip", ".gz", ".tar"],
}

# Create rule of chanding Cyrillic letters to Latin letters
CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ?<>,!@#[]#$%^&*()-=; "
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_","_", "_")
TRANS = {}
for c, t in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = t
    TRANS[ord(c.upper())] = t.upper()


def normalize(name):
    """Change Cyrillic letters to Latin letters"""
    global TRANS
    return name.translate(TRANS)


def is_file_exists(file, to_dir):
    """ if the file is exists with same name, this file will be renamed - 
    date-time will be added to file's name"""

    if file in to_dir.iterdir():
        add_name = datetime.now().strftime("%d_%m_%Y_%H_%M_%S_%f")
        new_name = file.resolve().stem + f"_{add_name}_" + file.suffix
        new_name_path = Path(to_dir, new_name)
        return new_name_path
    return file


def is_fold_exists(file, to_dir):
    """ Перевіряємо чи існує необхідна папка, якщо немає - створюємо;
    file - посилання на файл, який переміщаємо;    dr - посилання на папку, куди необхідно перемістити файл."""
    if to_dir.exists():
        folder_sort(file, to_dir) 
    else:
        Path(to_dir).mkdir()
        folder_sort(file, to_dir)
    

def folder_sort(file, to_dir):
    """ змінює назву файла та переміщає в необхідну папку.
    file - посилання на файл,  який переміщаємо;    dr - посилання, на папку, куди необхідно перемістити файл."""
    latin_name = normalize(file.name)    
    new_file = Path(to_dir, latin_name) 
    file_path = is_file_exists(new_file, to_dir) 
    file.replace(file_path) 


def show_result(p):
    total_dict = collections.defaultdict(list)  # collect file's suffix
    files_dict = collections.defaultdict(list)  # collect file's name

    for item in p.iterdir():
        if item.is_dir():
            for file in item.iterdir():
                if file.is_file():
                    total_dict[item.name].append(file.suffix)
                    files_dict[item.name].append(file.name) 
    for k, v in files_dict.items():
        print()
        print(f" Folder '{k}' contains files: ")
        print(f" ---- {v}")

    print()
    print("               *** File sorting completed successfully! ***   ")
    print("---------------------------------------------------------------------------")
    print("| {:^14} |{:^9}| {:^40} ".format("Folder", "files,pcs", "file's extensions"))
    print("---------------------------------------------------------------------------")

    for key, value in total_dict.items():
        k, a, b = key, len(value), ", ".join(set(value))
        print("| {:<14} |{:^9}| {:<40} ".format(k, a, b))

    print("----------------------------------------------------------------------------")
    print()



def sort_file(folder, p):
    """ Check extension of files, subfolders and sort it"""
    for i in p.iterdir():
        if i.name in ("documents", "audio", "video", "images", "archives", "other"): # script ignors these folders.
            continue
        if i.is_file():
            flag = False  # if flag stay False - file's extension is not in extension_dict and we need move this file to "other"
            for f, suf in extension_dict.items():
                if i.suffix.lower() in suf:
                    to_dir = Path(folder, f)
                    is_fold_exists(i, to_dir)
                    flag = True  # if file's extension was founded in extension_dict, flag == True
                else:
                    continue
            if not flag: 
                # if flag == False: extension of file was not founded in extension_dict. We need move this file to "other"
                to_dir = Path(folder, "other")
                is_fold_exists(i, to_dir)
        elif i.is_dir():
            if len(list(i.iterdir())) != 0:
                sort_file(folder, i) # if folder is not empty, recursively sort_file()
            else:
                shutil.rmtree(i)  # delete empty folders

    for j in p.iterdir():
        # unpacking archives
        if j.name == "archives" and len(list(j.iterdir())) != 0:
            for arch in j.iterdir():
                if arch.is_file() and arch.suffix in (".zip", ".gz", ".tar"):
                    try:
                        arch_dir_name = arch.resolve().stem  # створюємо назву папки, куди розпаковуємо архів (за назвою самого архіва)
                        path_to_unpack = Path(p, "archives", arch_dir_name) # створюємо шлях до папки розпаковки архіва
                        shutil.unpack_archive(arch, path_to_unpack)
                    except:
                        print(f"Attention: Error unpacking the archive '{arch.name}'!\n")
                    finally:
                        continue
                else:
                    continue
        elif j.is_dir() and not len(list(j.iterdir())):
            # delete empty folders:
            shutil.rmtree(j)
    


def main():
    path = sys.argv[1]  # run from the command line: `clean-folder /path/to folder/you want to clean/`
    # path = r"/home/oleksandr/Стільниця/trash"
    folder = Path(path)
    p = Path(path)
    try:
        sort_file(folder, p)
    except FileNotFoundError:
        print("\nThe folder was not found. Check the folder's path and run the command again!.\n")
        return
    return show_result(p)


if __name__ == "__main__":
    main()
