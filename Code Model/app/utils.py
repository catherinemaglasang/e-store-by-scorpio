import json

def build_json(response):
    entries = []
    out = {}

    if len(response) == 0:
        return {"status": "ok", "message": "No entries found", "entries": [], "count": 0}

    if 'Error' in str(response[0][0]):
        return {'status': 'error', 'message': response[0][0]}

    for row in response:
        entries.append(dict(row))

    return {'status': 'ok', 'message': 'ok', 'entries': entries, 'count': len(entries)}


class DatetimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%dT%H:%M:%SZ')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)