import re
import string


def is_header_tag_in(tags: tuple | list | set, txt: str) -> bool:
    """
    checks if header tag is in a sentence - returns True if so or False otherwise
    :param tags: collection of keywords that fn should search for
    :param txt: the text in which the value is searched for
    :return: bool value
    """
    for tag in tags:
        if tag in txt.lower():
            return True
    return False


def clear_emails(txt: str) -> str:
    """
    fn removes e-mail addresses from passed text
    :param txt: string that will be checked if it contains an e-mail address
    :return: the same text without email addresses
    """
    return re.sub(r"\S*@\S*\s?", "", txt)


def clear_txt_with_digits(txt: str) -> str:
    """
    removes words like "aaa123bbb", "j23", and also numbers from passed string
    :param txt: string that will be checked if it contains words with digits or numbers
    :return: clean text
    """
    return re.sub(r"\S*[0-9]+\S*\s?", "", txt)


def clear_punctuation(txt_to_clean: str) -> str:
    """
    create dict where keys are symbols from '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~' with None as the values
    and then replaces the punctuation signs with these Nones
    :param txt_to_clean: the string to be cleared
    :return: clean text
    """
    table = str.maketrans({key: None for key in string.punctuation})
    return txt_to_clean.translate(table)
