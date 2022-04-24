import re
from pathlib import Path


def clean_text_inside_file(file_path: str):
    """
    Load file as generator and clean the file as removing unwanted unicode characters
    """
    file_obj = Path(file_path)
    if not file_obj.is_file():
        # Not a correct 
        raise TypeError("Provided input is not a file. Please provide a correct text file")
    
    text_info = file_obj.read_text()
    
    if not text_info:
        raise ValueError("There is no information available on the file. Cannot be summarized")
    
    file_list = text_info.split('.')
    
    basic_text_list = [textf.strip().lower() for textf in file_list if (textf and isinstance(textf, str) and not textf.isspace())]
    
    clean_punctution_text = [re.sub(r"[^\w\s]", "", text_elem) for text_elem in basic_text_list]
           
    return clean_punctution_text
    
    