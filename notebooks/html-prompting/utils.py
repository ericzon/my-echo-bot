import os

from pathlib import Path

from IPython.display import display, HTML


def load_file(subpath):
    """
    Loads the file from the subpath from the root of the project in jupyter
    
    Args:
        subpath (string): subpath relative to the jupyter root project
            
    Returns
        the content as string
    """
    notebook_path = os.getcwd()    

    file_path=f"{notebook_path}/{subpath}"    

    html_content = Path(file_path).read_text()

    return html_content