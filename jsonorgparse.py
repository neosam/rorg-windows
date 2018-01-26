from json import JSONDecoder
from dateutil.parser import parse

def decode(dump):
    encoded_values = JSONDecoder().decode(dump)
    result = {}
    for date in encoded_values['days']:
        entries = encoded_values['days'][date]
        new_entries = []
        for entry in entries:
            from_dttm = parse(entry['clock']['from'])
            to_dttm = parse(entry['clock']['to'])
            new_entries.append({
                'title': entry['title'],
                'body': entry['body'],
                'from_dttm': from_dttm,
                'to_dttm': to_dttm,
                'time_diff': to_dttm - from_dttm,
                'properties': entry['properties']
            })
        result[date] = new_entries
    return result

def decode_file(filename):
    return decode(file(filename).read())

