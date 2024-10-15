from math import floor
from pydantic import HttpUrl
from Utilities.globals import Constants


def check_url_health(url: HttpUrl) -> bool:
    return True


def shorten_url(old_url, custom=None):
    if custom is not None and custom.strip() not in ('null', ''):
        return custom.strip(), len(custom.strip())
    else:
        domain = old_url.host.split('.')[1]
        path = f"{old_url.path}{old_url.query}"

        if path == '':
            return {"message": "URL is already shortened. Nothing to shorten here."}, 0

        suffix = hash_url_encode(path)
        return f"{domain}_{suffix}", len(suffix)


def hash_url_encode(val, base=62, limit=7):
    base_62_values = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    val = int("".join([str(ord(c)) for c in str(val)]))
    while val > 0:
        r = val % base
        result = f"{base_62_values[r]}" + result
        val = floor(val / base)
    return result[:limit]


def create_dynamic_function():
    func_code = f'''def redirectional_function(key):
        from fastapi.responses import RedirectResponse
        from DBRouter import DBManager
        obj = DBManager()
        
        redirect_url = obj.get_value(key)
        if isinstance(redirect_url, dict):
            return redirect_url
        
        return RedirectResponse(redirect_url, status_code=302)
    '''

    exec(func_code, globals())
    redirectional_function = globals()['redirectional_function']
    return redirectional_function

