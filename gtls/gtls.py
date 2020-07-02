import os
import re
import logging


def logUtils(Msg: str, Level: str = "INFO"):
    """A easy-to-use log tool.

    Args:
        Msg (str): message. Defaults to None.
        level (str, optional): log level. Defaults to "INFO".
    """

    if Level.upper() == "WARN":
        logging.basicConfig(
            level=logging.WARN, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        logging.warn(Msg)
    elif Level.upper() == "WARNING":
        logging.basicConfig(
            level=logging.WARNING, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        logging.warning(Msg)
    elif Level.upper() == "INFO":
        logging.basicConfig(
            level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        logging.info(Msg)
    elif Level.upper() == "ERROR":
        logging.basicConfig(
            level=logging.ERROR, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        logging.error(Msg)


def getSubFile(basedir: str, file_suffix: str = None):
    """Get the list of files with the same suffix in the specified directory.

    Args:
        basedir (str): The specified directory.
        file_suffix (str, optional): file suffix. Defaults to None.

    Returns:
        [list]: file list
    """

    if file_suffix is None:
        pattern = re.compile(r".")
    else:
        pattern = re.compile("{}$".format(file_suffix))
    try:
        FileList = [os.path.join(basedir, subfile) for subfile in os.listdir(basedir) if re.search(
            pattern, subfile) and os.path.isfile(os.path.join(basedir, subfile))]
        return FileList
    except NotADirectoryError:
        logUtils(Msg="The basedir is not a direcotry", Level='ERROR')
