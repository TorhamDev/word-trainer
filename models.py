from orm import Model


class Words(Model):
    """
    Words database model
    """

    word = str
    meaning = str
    is_learned = bool
