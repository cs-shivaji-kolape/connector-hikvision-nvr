# FortiSOAR_Hikvision
Hikvision's Network Video Recorders (NVRs) provide advanced artificial intelligence capabilities for any connected data stream, even those from conventional security cameras
## About the connector
Hikvision's Network Video Recorders (NVRs) provide advanced artificial intelligence capabilities for any connected data stream, even those from conventional security cameras
<p>This document provides information about the Hikvision NVR Connector, which facilitates automated interactions, with a Hikvision NVR server using FortiSOAR&trade; playbooks. Add the Hikvision NVR Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Hikvision NVR.</p>
### Version information

Connector Version: 1.0.2


Authored By: Islam Baker

Certified: No
## Installing the connector
<p>From FortiSOAR&trade; 5.0.0 onwards, use the <strong>Connector Store</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.<br>You can also use the following <code>yum</code> command as a root user to install connectors from an SSH session:</p>
`yum install cyops-connector-hikvision`

## Prerequisites to configuring the connector
- You must have the URL of Hikvision NVR server to which you will connect and perform automated operations and credentials to access that server.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Hikvision NVR server.

## Minimum Permissions Required
- N/A

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Hikvision NVR</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations&nbsp;</strong> tab enter the required configuration details:&nbsp;</p>
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Server URL<br></td><td><br>
<tr><td>Username<br></td><td><br>
<tr><td>Password<br></td><td><br>
</tbody></table>
## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function<br></th><th>Description<br></th><th>Annotation and Category<br></th></tr></thead><tbody><tr><td>Get NVR Device Details <br></td><td>Retrieve NVR Device Details <br></td><td>get_device_info <br/>Investigation<br></td></tr>
<tr><td>Get NVR Time <br></td><td>Retrieve NVR Current Time<br></td><td>get_ntp_details <br/>Investigation<br></td></tr>
<tr><td>Get HTTP Listening Servers<br></td><td>Get parameters of all HTTP listening servers.<br></td><td>get_http_listening_servers <br/>Investigation<br></td></tr>
<tr><td>Get Management Interface<br></td><td>Retrieve NVR Management Interface<br></td><td>get_interface <br/>Investigation<br></td></tr>
<tr><td>Get Channels<br></td><td>Retrieves Channels ID For All Cameras<br></td><td>get_channel <br/>Investigation<br></td></tr>
<tr><td>Search Log<br></td><td>Retrieves Logs<br></td><td>search_log <br/>Investigation<br></td></tr>
<tr><td>Search Videos Recording Details<br></td><td>Retrieves all Recorded Video<br></td><td>search_video <br/>Investigation<br></td></tr>
<tr><td>Download Videos Recording<br></td><td>Download Video and store it at tmp folder<br></td><td>download_video <br/>Investigation<br></td></tr>
</tbody></table>
### operation: Get NVR Device Details 
#### Input parameters
None.
#### Output

 The output contains a non-dictionary value.
### operation: Get NVR Time 
#### Input parameters
None.
#### Output

 The output contains a non-dictionary value.
### operation: Get HTTP Listening Servers
#### Input parameters
None.
#### Output

 The output contains a non-dictionary value.
### operation: Get Management Interface
#### Input parameters
None.
#### Output

 The output contains a non-dictionary value.
### operation: Get Channels
#### Input parameters
None.
#### Output

 The output contains a non-dictionary value.
### operation: Search Log
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Meta ID<br></td><td>Choose Log Type by default All<br>
</td></tr><tr><td>Start Date<br></td><td><br>
</td></tr><tr><td>End Date<br></td><td><br>
</td></tr><tr><td>Limit<br></td><td>Maximum Retrieve Result<br>
</td></tr></tbody></table>
#### Output

 The output contains a non-dictionary value.
### operation: Search Videos Recording Details
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Channel ID<br></td><td><br>
</td></tr><tr><td>Start Date<br></td><td><br>
</td></tr><tr><td>End Date<br></td><td><br>
</td></tr><tr><td>Limit<br></td><td>Maximum Retrieve Result<br>
</td></tr></tbody></table>
#### Output

 The output contains a non-dictionary value.
### operation: Download Videos Recording
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Channel ID<br></td><td><br>
</td></tr><tr><td>Video Name<br></td><td><br>
</td></tr></tbody></table>
#### Output

 The output contains a non-dictionary value.
## Included playbooks
The `Sample - hikvision - 1.0.2` playbook collection comes bundled with the Hikvision NVR connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR<sup>TM</sup> after importing the Hikvision NVR connector.

- Add Group
- Add Policy
- Delete Specific Group
- Get All Groups Details
- Get All Policies on Specific Group
- Get Host Details
- Get Host Group Static Info
- Get Host List
- Get Products Installed
- Get Software Installed on Specefic Host
- Get Specific Policy
- Move Host to Specific Group

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection, since the sample playbook collection gets deleted during connector upgrade and delete.

