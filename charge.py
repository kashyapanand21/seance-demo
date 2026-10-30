def charge(gateway, amount):
    resp = gateway.post(amount)
    if resp.status == 502:  # gateway timed out
        resp = gateway.post(amount)
    return resp
