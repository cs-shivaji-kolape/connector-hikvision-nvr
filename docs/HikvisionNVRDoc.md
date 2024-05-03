## About the connector
Hikvision's Network Video Recorders (NVRs) provide advanced artificial intelligence capabilities for any connected data stream, even those from conventional security cameras
<p>This document provides information about the Hikvision NVR Connector, which facilitates automated interactions, with a Hikvision NVR server using FortiSOAR&trade; playbooks. Add the Hikvision NVR Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Hikvision NVR.</p>

### Version information

Connector Version: 1.0.0

Contributors: Islam Baker

Authored By: Fortinet SE KSA 

Certified: No
## Installing the connector
<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>
<pre>yum install cyops-connector-hikvision-nvr</pre>

## Prerequisites to configuring the connector
- You must have the credentials of Hikvision NVR server to which you will connect and perform automated operations.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Hikvision NVR server.

## Minimum Permissions Required
- Not applicable

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Hikvision NVR</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations</strong> tab enter the required configuration details:</p>
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Server URL</td><td>Specify the URL of the Hikvision NVR server to connect and perform automated operations</td>
</tr><tr><td>Username</td><td>Specify the username to access the Hikvision NVR server to which you will connect and perform automated operations</td>
</tr><tr><td>Password</td><td>Specify the password to access the Hikvision NVR server to which you will connect and perform automated operations</td>
</tr></tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations:
<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Get NVR Device Details</td><td>Retrieves detailed information about a Network Video Recorder (NVR) device.</td><td>get_device_info <br/>Investigation</td></tr>
<tr><td>Get NVR Time</td><td>Retrieves the current time settings of a Network Video Recorder (NVR) device</td><td>get_ntp_details <br/>Investigation</td></tr>
<tr><td>Get HTTP Listening Servers</td><td>Retrieves information about the HTTP servers running on a device.</td><td>get_http_listening_servers <br/>Investigation</td></tr>
<tr><td>Get Management Interface</td><td>Retrieves information about the management interface settings of a device</td><td>get_interface <br/>Investigation</td></tr>
<tr><td>Get Channels</td><td>Retrieves information about the channels available on a device</td><td>get_channel <br/>Investigation</td></tr>
<tr><td>Search Log</td><td>Retrieves for specific logs or event records within a device's log database based on various criteria such as time range, log type parameters</td><td>search_log <br/>Investigation</td></tr>
<tr><td>Get Videos Recording Details</td><td>Retrieve detailed information about video recordings stored on a Hikvision device, such as a Network Video Recorder (NVR)</td><td>get_video_recording_details <br/>Investigation</td></tr>
<tr><td>Download Videos Recording</td><td>Download recorded video footage from a Hikvision device, such as a Network Video Recorder (NVR), and save it in the FortiSOAR attachments module</td><td>download_video <br/>Investigation</td></tr>
</tbody></table>

### operation: Get NVR Device Details
#### Input parameters
None.
#### Output
The output contains the following populated JSON schema:

<pre>{
    "DeviceInfo": {
        "model": "",
        "@xmlns": "",
        "@version": "",
        "deviceID": "",
        "deviceName": "",
        "deviceType": "",
        "macAddress": "",
        "manufacturer": "",
        "serialNumber": "",
        "telecontrolID": "",
        "encoderVersion": "",
        "firmwareVersion": "",
        "hardwareVersion": "",
        "encoderReleasedDate": "",
        "firmwareReleasedDate": ""
    }
}</pre>
### operation: Get NVR Time
#### Input parameters
None.
#### Output
The output contains the following populated JSON schema:

<pre>{
    "Time": {
        "@xmlns": "",
        "@version": "",
        "timeMode": {
            "@opt": "",
            "#text": ""
        },
        "timeType": {
            "@opt": "",
            "#text": ""
        },
        "timeZone": "",
        "localTime": ""
    }
}</pre>
### operation: Get HTTP Listening Servers
#### Input parameters
None.
#### Output
The output contains the following populated JSON schema:

<pre>{
    "HttpHostNotificationList": {
        "@xmlns": "",
        "@version": "",
        "HttpHostNotification": {
            "id": "",
            "url": "",
            "@xmlns": "",
            "portNo": "",
            "@version": "",
            "ipAddress": "",
            "Extensions": {
                "@xmlns": "",
                "intervalBetweenEvents": ""
            },
            "protocolType": "",
            "parameterFormatType": "",
            "addressingFormatType": "",
            "httpAuthenticationMethod": ""
        }
    }
}</pre>
### operation: Get Management Interface
#### Input parameters
None.
#### Output
The output contains the following populated JSON schema:

<pre>{
    "NetworkInterfaceList": {
        "@xmlns": "",
        "@version": "",
        "NetworkInterface": {
            "id": "",
            "Link": {
                "MTU": {
                    "@max": "",
                    "@min": "",
                    "#text": ""
                },
                "speed": "",
                "@xmlns": "",
                "duplex": "",
                "@version": "",
                "MACAddress": "",
                "autoNegotiation": ""
            },
            "@xmlns": "",
            "@version": "",
            "Discovery": {
                "UPnP": {
                    "enabled": ""
                },
                "@xmlns": "",
                "@version": "",
                "Zeroconf": {
                    "enabled": ""
                }
            },
            "IPAddress": {
                "@xmlns": "",
                "@version": "",
                "DNSEnable": "",
                "ipAddress": "",
                "ipVersion": "",
                "PrimaryDNS": {
                    "ipAddress": ""
                },
                "subnetMask": "",
                "SecondaryDNS": {
                    "ipAddress": ""
                },
                "DefaultGateway": {
                    "ipAddress": ""
                },
                "addressingType": ""
            },
            "defaultConnection": ""
        }
    }
}</pre>
### operation: Get Channels
#### Input parameters
None.
#### Output
The output contains the following populated JSON schema:

<pre>{
    "StreamingChannelList": {
        "@xmlns": "",
        "@version": "",
        "StreamingChannel": [
            {
                "id": "",
                "Video": {
                    "enabled": "",
                    "GovLength": "",
                    "SmartCodec": {
                        "enabled": ""
                    },
                    "vbrLowerCap": "",
                    "vbrUpperCap": "",
                    "fixedQuality": "",
                    "maxFrameRate": "",
                    "videoScanType": "",
                    "videoCodecType": "",
                    "snapShotImageType": "",
                    "videoResolutionWidth": "",
                    "videoResolutionHeight": "",
                    "dynVideoInputChannelID": "",
                    "videoQualityControlType": ""
                },
                "@xmlns": "",
                "enabled": "",
                "@version": "",
                "Transport": {
                    "ControlProtocolList": {
                        "ControlProtocol": {
                            "streamingTransport": ""
                        }
                    }
                },
                "channelName": ""
            }
        ]
    }
}</pre>
### operation: Search Log
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Log Type</td><td>Select type of log you want to retrieves
</td></tr><tr><td>Start Date</td><td>Specify the starting date from which data should be retrieved.
</td></tr><tr><td>End Date</td><td>Specify the end date for data retrieval, up to the specified date
</td></tr><tr><td>Limit</td><td>Specify the maximum number of items or records that should be returned in result
</td></tr></tbody></table>
#### Output
The output contains the following populated JSON schema:

<pre>{
    "CMSearchResult": {
        "@xmlns": "",
        "@version": "",
        "searchID": "",
        "matchList": {
            "searchMatchItem": [
                {
                    "logDescriptor": {
                        "metaId": "",
                        "localID": "",
                        "localId": "",
                        "paraType": "",
                        "userName": "",
                        "ipAddress": "",
                        "StartDateTime": "",
                        "additionInformation": ""
                    }
                }
            ]
        },
        "numOfMatches": "",
        "responseStatus": "",
        "responseStatusStrg": ""
    }
}</pre>
### operation: Get Videos Recording Details
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Channel ID</td><td>Specify the ID of the channel from which you want to retrieve video recording details
</td></tr><tr><td>Start Date</td><td>Specify the starting date from which data should be retrieved.
</td></tr><tr><td>End Date</td><td>Specify the end date for data retrieval, up to the specified date
</td></tr><tr><td>Limit</td><td>Specify the maximum number of items or records that should be returned in result
</td></tr></tbody></table>
#### Output
The output contains the following populated JSON schema:

<pre>{
    "CMSearchResult": {
        "@xmlns": "",
        "@version": "",
        "searchID": "",
        "matchList": {
            "searchMatchItem": [
                {
                    "trackID": "",
                    "sourceID": "",
                    "timeSpan": {
                        "endTime": "",
                        "startTime": ""
                    },
                    "metadataMatches": {
                        "metadataDescriptor": ""
                    },
                    "mediaSegmentDescriptor": {
                        "codecType": "",
                        "contentType": "",
                        "playbackURI": ""
                    }
                }
            ]
        },
        "numOfMatches": "",
        "responseStatus": "",
        "responseStatusStrg": ""
    }
}</pre>
### operation: Download Videos Recording
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Channel ID</td><td>Specify the ID of the channel from which you want to download the video recording.
</td></tr><tr><td>Video Name</td><td>Specify the name of the video recording which you want to download
</td></tr></tbody></table>
#### Output
The output contains the following populated JSON schema:

<pre>{
    "id": "",
    "@id": "",
    "cVEs": [],
    "file": {
        "id": "",
        "@id": "",
        "size": "",
        "uuid": "",
        "@type": "",
        "assignee": "",
        "filename": "",
        "metadata": [],
        "mimeType": "",
        "thumbnail": "",
        "uploadDate": ""
    },
    "name": "",
    "type": "",
    "uuid": "",
    "@type": "",
    "tasks": [],
    "alerts": [],
    "assets": [],
    "owners": [],
    "people": [],
    "@context": "",
    "assignee": "",
    "comments": [],
    "warrooms": [],
    "incidents": [],
    "createDate": "",
    "createUser": {
        "id": "",
        "@id": "",
        "name": "",
        "uuid": "",
        "@type": "",
        "avatar": "",
        "userId": "",
        "userType": "",
        "createDate": "",
        "createUser": "",
        "modifyDate": "",
        "modifyUser": ""
    },
    "indicators": [],
    "modifyDate": "",
    "modifyUser": {
        "id": "",
        "@id": "",
        "name": "",
        "uuid": "",
        "@type": "",
        "avatar": "",
        "userId": "",
        "userType": "",
        "createDate": "",
        "createUser": "",
        "modifyDate": "",
        "modifyUser": ""
    },
    "recordTags": [],
    "userOwners": [],
    "workspaces": [],
    "description": "",
    "vulnerabilities": []
}</pre>
