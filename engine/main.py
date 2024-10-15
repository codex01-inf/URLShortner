import sys
import os
from pathlib import Path
from fastapi import FastAPI
from pydantic import BaseModel, Field, HttpUrl

sys.path.append(os.path.join(str(Path(__file__).absolute()).partition('engine')[0], 'engine'))

from Utilities.helper_functions import shorten_url, create_dynamic_function
from DBRouter import DBManager

app = FastAPI()


class Item(BaseModel):
    # url: str = Field(..., example="www.some_domain.com")
    url: HttpUrl
    custom: str | None = Field(None, description="Custom shorten url if Client wants.", max_length=90)


@app.get("/{special_key}")
async def new(special_key):
    my_function = create_dynamic_function()
    return my_function(special_key)


@app.post("/entrypoint")
async def entrypoint(payload: Item):
    db_obj = DBManager()
    client_url = str(payload.url)

    # print('HELLO')
    # db_obj.ping_db()
    # print('BYE')

    if db_obj.check_existence(client_url):
        return {"message": "Short URL for the given Client URL already exists. If redirect URL not working, "
                           "please raise a query."}

    # shorten URL logic
    new_url, size = shorten_url(payload.url, payload.custom)

    if isinstance(new_url, dict):
        return new_url

    print(f"New URL = {new_url}")
    response = db_obj.insert([client_url, new_url, size])
    print(response)
    return {"status": "Success", "new_url": new_url}

# if __name__ == "__main__":
#     uvicorn.run(app, host="localhost", port=8086)
