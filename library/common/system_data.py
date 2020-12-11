from datetime import datetime


def transform_unix_time(unix_time: float, full_time: bool) -> str:
    """
    Transform unix type time into common
    :param full_time: If true: func returns '%Y-%m-%d %H:%M:%S' format, else '%Y-%m-%d'
    :param unix_time: usual unix format time
    :return: %Y-%m-%d
    """
    return datetime.utcfromtimestamp(unix_time).strftime('%Y-%m-%d %H:%M:%S' if full_time else '%Y-%m-%d')
