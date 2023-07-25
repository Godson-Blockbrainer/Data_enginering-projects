# -*- coding: utf-8 -*-
# This is file management code that helps me arranage my files properly

import os
import shutil
from datetime import datetime

def move_files():
    # Define the source directory and target directory
    source_dir = os.path.expanduser('~/Downloads')
    target_dir = os.path.expanduser('~/Documents/PDFs')

    # Create target directory if not exist
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Iterate through the files in the source directory
    for filename in os.listdir(source_dir):
        # If the file is a .pdf, move it to the target directory
        if filename.endswith('.pdf'):
            shutil.move(os.path.join(source_dir, filename), target_dir)

# Run the function
move_files()
