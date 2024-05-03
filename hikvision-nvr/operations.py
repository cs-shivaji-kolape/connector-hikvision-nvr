"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""

import json
from os.path import join, splitext

import requests
import xmltodict
from connectors.core.connector import get_logger, ConnectorError
from connectors.cyops_utilities.builtins import upload_file_to_cyops
from django.conf import settings

from .constants import (DEFAULT_EXTENSION, LOG_SEARCH_XML_PAYLOAD, GET_VIDEO_RECORDING_XML_PAYLOAD)

error_msgs = {
    400: 'Bad/Invalid Request',
    401: 'Unauthorized: Invalid credentials or token provided failed to authorize',
    403: 'Access Denied',
    404: 'Not Found',
    500: 'Internal Server Error',
    503: 'Service Unavailable'
}

logger = get_logger('hikvision-nvr')


class hikvision(object):
    def __init__(self, config, *args, **kwargs):
        self.username = config.get('username')
        self.password = config.get('password')
        self.verify_ssl = config.get('verify_ssl')
        self.url = config.get('server_url', '').strip('/')
        if not self.url.startswith('https://') and not self.url.startswith('http://'):
            self.url = 'http://{0}'.format(self.url)
        elif self.url.startswith('https://'):
            self.url = self.url.replace('https://', 'http://')
        else:
            self.url = self.url

    def make_rest_call(self, endpoint, headers=None, params=None, data=None, method='GET'):
        try:
            url = self.url + endpoint
            logger.debug('Rest API Endpoint {0}'.format(url))
            auth = requests.auth.HTTPDigestAuth(self.username, self.password)
            response = requests.request(method, url, auth=auth, data=data, verify=self.verify_ssl)
            logger.debug('Rest API Status Code: {0}'.format(response.status_code))
            try:
                from connectors.debug_utils.curl_script import make_curl
                make_curl(method, url, headers=headers, params=params, data=data, verify_ssl=self.verify_ssl)
            except Exception:
                pass
            if response.ok:
                content_type = response.headers.get('Content-Type')
                if response.content != "" and 'application/xml' in content_type:
                    return json.loads(json.dumps(xmltodict.parse(response.content.decode('utf-8'))))
                if 'json' in str(content_type):
                    return response.json()
                else:
                    return response.content
            else:
                raise ConnectorError("{0}".format(error_msgs.get(response.status_code), response.text))
        except requests.exceptions.SSLError:
            raise ConnectorError('SSL certificate validation failed')
        except requests.exceptions.ConnectTimeout:
            raise ConnectorError('The request timed out while trying to connect to the server')
        except requests.exceptions.ReadTimeout:
            raise ConnectorError(
                'The server did not send any data in the allotted amount of time')
        except requests.exceptions.ConnectionError:
            raise ConnectorError('Invalid endpoint or credentials')
        except Exception as err:
            raise ConnectorError(str(err))


def login(config, params):
    hik = hikvision(config)
    endpoint = '/ISAPI/System/Network/interfaces'
    response = hik.make_rest_call(endpoint=endpoint, method='GET')
    return response


def get_channel(config, params):
    hik = hikvision(config)
    endpoint = '/ISAPI/Streaming/channels'
    return hik.make_rest_call(endpoint=endpoint, method='GET')


def get_interface(config, params):
    hik = hikvision(config)
    endpoint = '/ISAPI/System/Network/interfaces'
    return hik.make_rest_call(endpoint=endpoint, method='GET')


def search_log(config, params):
    hik = hikvision(config)
    endpoint = '/ISAPI/ContentMgmt/logSearch'
    start_time = params.get('start_date')
    end_time = params.get('enddate')
    limit = params.get('limit')
    if params.get('metaid') != 'All':
        metaID = "log.std-cgi.com/" + str(params.get('metaid'))
    else:
        metaID = "log.std-cgi.com"
    payload = LOG_SEARCH_XML_PAYLOAD.format(metaID=metaID.strip(), start_time=start_time, end_time=end_time, limit=limit)
    return hik.make_rest_call(endpoint=endpoint, method='POST', data=payload)


def get_http_listening_servers(config, params):
    hik = hikvision(config)
    endpoint = '/ISAPI/Event/notification/httpHosts'
    return hik.make_rest_call(endpoint=endpoint, method='GET')


def get_device_info(config, params):
    hik = hikvision(config)
    endpoint = '/ISAPI/System/deviceInfo'
    return hik.make_rest_call(endpoint=endpoint, method='GET')


def get_ntp_details(config, params):
    hik = hikvision(config)
    endpoint = '/ISAPI/System/time/capabilities'
    return hik.make_rest_call(endpoint=endpoint, method='GET')


def get_video_recording_details(config, params):
    hik = hikvision(config)
    endpoint = '/ISAPI/ContentMgmt/search'
    start_time = params.get('start_date')
    end_time = params.get('enddate')
    trackid = params.get('trackid')
    limit = params.get('limit', '')
    payload = GET_VIDEO_RECORDING_XML_PAYLOAD.format(trackid=trackid, start_time=start_time, end_time=end_time, limit=limit)
    return hik.make_rest_call(endpoint=endpoint, method='POST', data=payload)


def download_video(config, params):
    hik = hikvision(config)
    url = config.get('server_url').replace("http://", "")
    url_final = url.replace("https://", "")
    file_name = str(params.get('videoname'))
    playbackURI = "rtsp://" + str(url_final) + "/Streaming/tracks/" + str(params.get('trackid')) + "/?&amp;name="
    endpoint = "/ISAPI/ContentMgmt/download?playbackURI=" + playbackURI + file_name
    video_content = hik.make_rest_call(endpoint=endpoint, method='GET')
    base, extension = splitext(file_name)
    if not extension:
        file_name += DEFAULT_EXTENSION
    path = join(settings.TMP_FILE_ROOT, file_name)
    with open(path, 'wb') as fp:
        fp.write(video_content)
    attach_response = upload_file_to_cyops(file_path=file_name, filename=file_name,
                                           name=file_name, create_attachment=True)
    return attach_response


def _check_health(config):
    try:
        res = login(config, params={})
        if res:
            return True
    except Exception as err:
        logger.exception("{0}".format(str(err)))
        raise ConnectorError("{0}".format(str(err)))


operations = {
    'get_interface': get_interface,
    'search_log': search_log,
    'get_http_listening_servers': get_http_listening_servers,
    'get_channel': get_channel,
    'get_video_recording_details': get_video_recording_details,
    'download_video': download_video,
    'get_device_info': get_device_info,
    'get_ntp_details': get_ntp_details
}
