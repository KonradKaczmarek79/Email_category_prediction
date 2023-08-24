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
