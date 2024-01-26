import logging

import allure
from allure_commons.types import AttachmentType
import json


def screenshot(browser):
    allure.attach(
        body=browser.driver.get_screenshot_as_png(),
        name='screenshot',
        attachment_type=AttachmentType.PNG,
        extension='.png')


def logs(browser):
    log = "".join(f'{text}\n' for text in browser.driver.get_log(log_type='browser'))
    allure.attach(log, 'browser_logs', AttachmentType.TEXT, '.log')


def html(browser):
    page_html = browser.driver.page_source
    allure.attach(page_html, 'page_source', AttachmentType.HTML, '.html')


def video(browser):
    video_url = "https://selenoid.autotests.cloud/video/" + browser.driver.session_id + ".mp4"
    page_html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
                + video_url \
                + "' type='video/mp4'></video></body></html>"
    allure.attach(page_html, 'video_' + browser.driver.session_id, AttachmentType.HTML, '.html')


def screen_xml_dump(browser):
    allure.attach(
        body=browser.driver.page_source,
        name='screen xml dump',
        attachment_type=allure.attachment_type.XML,
    )


def bstack_video(session_id, bs_username, bs_password):
    import requests
    bstack_session = requests.get(
        f'https://api.browserstack.com/app-automate/sessions/{session_id}.json',
        auth=(bs_username, bs_password),
    ).json()
    video_url = bstack_session['automation_session']['video_url']

    allure.attach(
        '<html><body>'
        '<video width="100%" height="100%" controls autoplay>'
        f'<source src="{video_url}" type="video/mp4">'
        '</video>'
        '</body></html>',
        name='video recording',
        attachment_type=allure.attachment_type.HTML,
    )





