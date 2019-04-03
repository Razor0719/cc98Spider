import datetime
import re

import pytz


class Cc98parse(object):
    @staticmethod
    def parse_tz(item, date):
        date_match = re.match(r'(\d{4}(-|/|.)\d{1,2}\2\d{1,2})T((\d{1,2}:\d{1,2}:\d{1,2})(\.(\d{1,3}))?)', date)
        date_format = '%Y-%m-%dT%H:%M:%S.%f'
        if date_match.group(5) is None:
            date_format = '%Y-%m-%dT%H:%M:%S'
        item['time'] = datetime.datetime.strptime(
            date_match.group(),
            date_format
        ).astimezone(pytz.timezone('Asia/Shanghai'))
