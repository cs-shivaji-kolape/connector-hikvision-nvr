"""
Copyright start
Copyright (C) 2008 - 2022 Fortinet Inc.
All rights reserved.
FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
Copyright end
"""
import base64, json, requests

from connectors.core.connector import get_logger, ConnectorError
import pytz
from datetime import datetime,timedelta
import xmltodict


logger = get_logger('hikvision')

class hikvision(object):
    def __init__(self, config, *args, **kwargs):
        self.username = config.get('username')
        self.password = config.get('password')
        self.url = config.get('server_url')
        if  not self.url.startswith('https://') and not self.url.startswith('http://'):
            self.url = 'http://{0}'.format(self.url)
        elif self.url.startswith('https://'):
            self.url = self.url.replace('https://','http://')
        else:
            self.url = self.url

    def make_rest_call(self, endpoint, headers=None, params=None, data=None, method='GET'):
        try:
            url = self.url + endpoint
            auth = requests.auth.HTTPDigestAuth(self.username, self.password)
            headers = {'Content-Type': 'application/json'
                       }
            response = requests.request(method, url, auth=auth, data=data)
            if response.ok or response.status_code == 200:
                logger.info('Successfully got response for url {0}'.format(url))
                if 'json' in str(response.headers):
                    return response.json()
                else:
                    return response.content
            else:
                raise ConnectorError("{0}".format(errors.get(response.status_code, '')))
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
    response = hik.make_rest_call(endpoint=endpoint, method='GET')
    result = xmltodict.parse(response)
    return json.dumps(result)


def get_interface(config, params):
    hik = hikvision(config)
    endpoint = '/ISAPI/System/Network/interfaces'
    response = hik.make_rest_call(endpoint=endpoint, method='GET')
    result = xmltodict.parse(response)
    return json.dumps(result)


def search_log(config, params):
  hik = hikvision(config)
  endpoint = '/ISAPI/ContentMgmt/logSearch'
  Timestart = params.get('start_date')
  timeend = params.get('enddate')
  if params.get('metaid') != 'All':
  	metaID= "log.std-cgi.com/" + str(params.get('metaid'))
  else:
    metaID= "log.std-cgi.com"
  payload = "<?xml version: \"1.0\" encoding=\"utf-8\"?><CMSearchDescription><searchID>CA9B76C3-E890-0011-B657-C8E047E01E64</searchID><metaId>"+ metaID +"</metaId><timeSpanList><timeSpan><startTime>" + str(Timestart) + "</startTime><endTime>" + str(timeend) + " </endTime></timeSpan></timeSpanList><maxResults>"+str(params.get('limit'))+"</maxResults></CMSearchDescription>"
  response = hik.make_rest_call(endpoint=endpoint, method='POST', data=payload)
  result = xmltodict.parse(response)
  return json.dumps(result)


def get_http_listening_servers(config, params):
    hik = hikvision(config)
    endpoint = '/ISAPI/Event/notification/httpHosts'
    response = hik.make_rest_call(endpoint=endpoint, method='GET')
    result = xmltodict.parse(response)
    return json.dumps(result)

  

def get_device_info(config, params):
    hik = hikvision(config)
    endpoint = '/ISAPI/System/deviceInfo'
    response = hik.make_rest_call(endpoint=endpoint, method='GET')
    result = xmltodict.parse(response)
    return json.dumps(result)
  
  
def get_ntp_details(config, params):
    hik = hikvision(config)
    endpoint = '/ISAPI/System/time/capabilities'
    response = hik.make_rest_call(endpoint=endpoint, method='GET')
    result = xmltodict.parse(response)
    return json.dumps(result)
  
  
def search_video(config, params):
  hik = hikvision(config)
  endpoint = '/ISAPI/ContentMgmt/search'
  Timestart = params.get('start_date')
  timeend = params.get('enddate')
  trackid = params.get('trackid')
  limit = params.get('limit')
  payload = "<?xml version: \"1.0\" encoding=\"utf-8\"?><CMSearchDescription><searchID>CAA56F7B-4170-0001-9D79-19E020301367</searchID><trackList><trackID>"+str(trackid)+"</trackID></trackList><timeSpanList><timeSpan><startTime>"+str(Timestart)+"</startTime><endTime>"+str(timeend)+"</endTime></timeSpan></timeSpanList><maxResults>"+str(limit)+"</maxResults><searchResultPostion>0</searchResultPostion><metadataList><metadataDescriptor>//recordType.meta.std-cgi.com</metadataDescriptor></metadataList></CMSearchDescription>"
  response = hik.make_rest_call(endpoint=endpoint, method='POST', data=payload)
  result = xmltodict.parse(response)
  return json.dumps(result)

  
def download_video(config, params):
  hik = hikvision(config)
  url = config.get('server_url').replace("http://","")
  url_final = url.replace("https://","")
  videoname = str(params.get('videoname'))
  playbackURI = "rtsp://" + str(url_final) + "/Streaming/tracks/"+ str(params.get('trackid')) +"/?&amp;name="
  endpoint = "/ISAPI/ContentMgmt/download?playbackURI=" + playbackURI + videoname
  response = hik.make_rest_call(endpoint=endpoint, method='GET')
  file = open('/tmp/example.mp4', 'wb')
  file.write(response)
  file.close()
  return "The Video has been downloaded successfully at /tmp folder"

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
    'get_channel':get_channel,
    'search_video':search_video,
  	'download_video':download_video,
  	'get_device_info':get_device_info,
  	'get_ntp_details':get_ntp_details
}
