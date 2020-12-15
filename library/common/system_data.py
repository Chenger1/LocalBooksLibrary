from datetime import datetime
import pytz

utc = pytz.UTC


def transform_unix_time(unix_time: float) -> datetime:
    """
    Transform unix type time into common
    :param unix_time: usual unix format time
    :return: datetime
    """
    return transform_to_utc(datetime.utcfromtimestamp(unix_time))


def transform_to_utc(naive_datetime: datetime) -> datetime:
    return naive_datetime.replace(tzinfo=utc)

