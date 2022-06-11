# file path browser

from tkinter import filedialog
import os
import PyPDF2
import datetime

import logging
logger = logging.getLogger()
log = logging.getLogger(__name__)


def get_file_path():
    try:
        filename = filedialog.asksaveasfile(title="open")
        return filename
    except Exception as e:
        print(e)
        logging.exception(str(e))

# pdf_merger_function


def merge_pdf(folder_path, pdf_file_list):
    today = datetime.datetime.now()
    date_time = today.strftime("%d%m%Y_%H%M%S_")
    mergeFile = PyPDF2.PdfFileMerger()
    fileList = pdf_file_list
    log.info("merge pdf function : merge pdf")
    try:
        for pdf in pdf_file_list:
            if len(pdf_file_list) > 1:
                mergeFile.append(PyPDF2.PdfFileReader(folder_path + "\\" + pdf, "rb"))
        mergeFile.write(folder_path + "\\" + date_time + "MergeFile.pdf")
        log.info("New Merger PDF created with name: " + date_time + "MergerFile.pdf")
    except Exception as e:
        log.error("Merge pdf function: Error occurred while merging pdf")
        log.exception("Exception occurred" + str(e))

# file listing


def get_all_files(folder_path):
    global all_file_list
    log.info("calling get_all_files function")
    try:
        all_file_list = os.listdir(folder_path)
    except Exception as e:
        log.error("get all_file_function: Error occurred while iterating file name")
        log.exception("Exception occurred" + str(e))
    pdf_file_list = []
    try:
        for file in all_file_list:
            if file.find("pdf") > 0:
                pdf_file_list.append(file)
        return all_file_list, pdf_file_list
    except Exception as e:
        log.error("get_all_file function: Error occurred while iterating file name")
        log.exception("Exception occurred" + str(e))
