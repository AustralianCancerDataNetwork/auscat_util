"""
Script to remove database connection strings from Pentaho KTR and KJB files, before they can
pushed back to github

Example usage:
    python remove_conn_strs_pentaho.py PATH_TO_PENTAHO_FILES

    where:
        PATH_TO_PENTAHO_FILES: relative or absolute path to the directory that holds the pentaho files
"""

import logging
import os
import sys

from auscatutil.queryfunctions import PentahoConnection

logging.getLogger().setLevel(logging.INFO)

def main():
    if len(sys.argv) != 2:
        logging.error(f" Example usage: `python remove_conn_strs_pentaho.py PATH_TO_PENTAHO_FILES`")
        exit(1)
    elif not os.path.isdir(sys.argv[1]):
        logging.error(" Please provide a valid path to the Pentaho files!")
        exit(1)

    path_to_files_to_strip = sys.argv[1]
    abs_path_to_files_to_strip = os.path.abspath(path_to_files_to_strip)

    try:
        logging.info(f" Attempting to remove sensitive info from {abs_path_to_files_to_strip} files...")
        pentaho_conn = PentahoConnection([path_to_files_to_strip])
        pentaho_conn.remove_connections()
        logging.info(" Done!")
    except Exception as e:
        logging.error(f" Could not remove sensitive info from files in {path_to_files_to_strip}, {e}")
        exit(1)

if __name__ == "__main__":
    main()
