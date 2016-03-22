from flask import jsonify


def build_json(response):
    entries = []
    out = {}

    if len(response) == 0:
        return {"status":"ok", "message":"No entries found", "entries":[], "count":0}

    if 'Error' in str(response[0][0]):
        return {'status': 'error', 'message': response[0][0]}

    for row in response:
        entries.append(dict(row))

    return {'status': 'ok', 'message': 'ok', 'entries': entries, 'count': len(entries)}

