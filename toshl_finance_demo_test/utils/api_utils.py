import json
import logging
import os

import allure
import curlify
from allure_commons._allure import step
from allure_commons.types import AttachmentType
from requests import Session, Response

from config import config

cookie_tu = ''
cookies = ''
def load_schema(name: str, api_location: str):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),os.pardir, os.pardir, f'resources/json_schemas/{api_location}/', name)
    with open(path) as file:
        json_schema = json.loads(file.read())
    return json_schema

class CustomSession(Session):
    def __init__(self, base_url):
        self.base_url = base_url

        super().__init__()

    def request(self, method, url, *args, **kwargs) -> Response:
        print(f' Url  {url}' )
        print(f' json  {json}')

        if url != '/oauth2/login':
            kwargs['cookies'] = {'tu': cookie_tu}

        response = super(CustomSession, self).request(method=method, url=self.base_url + url,  *args,  **kwargs)
        attach_request_and_response_data(response)
        log_request_and_response_data_to_console(response)
        curl = curlify.to_curl(response.request)
        logging.info(curl)
        with step(f'{method} {url}'):
            allure.attach(body=curl, name="Request curl", attachment_type=AttachmentType.TEXT, extension='txt')
            return response


reqres_session = CustomSession(config.API_URL)


def attach_request_and_response_data(r, *args, **kwargs):
    allure.attach(
        name="Request url",
        body=r.request.url,
        attachment_type=AttachmentType.TEXT)
    allure.attach(
        name="Request headers",
        body=str(r.request.headers),
        attachment_type=AttachmentType.TEXT)
    request_body = as_pretty_json(r.request.body)
    if request_body:
        allure.attach(
            name="Request body",
            body=request_body,
            attachment_type=AttachmentType.JSON,
            extension="json")
    allure.attach(
        name='Response status code',
        body=str(r.status_code),
        attachment_type=allure.attachment_type.TEXT,
        extension='txt'
    )
    response_body = as_pretty_json(r.text)
    if response_body:
        allure.attach(
            name="Response body",
            body=response_body,
            attachment_type=AttachmentType.JSON,
            extension="json")


def log_request_and_response_data_to_console(r, *args, **kwargs):
    logging.info("Request: " + r.request.url)
    request_body = as_pretty_json(r.request.body)
    if request_body:
        logging.info("INFO Request body: " + request_body)
    logging.info("Request headers: " + str(r.request.headers))
    logging.info("Response code " + str(r.status_code))
    response_body = as_pretty_json(r.text)
    if response_body:
        logging.info("Response: " + response_body)


def as_pretty_json(data):
    if not data:
        return None
    try:
        return json.dumps(json.loads(data), indent=4, ensure_ascii=True)
    except json.JSONDecodeError:
        return None