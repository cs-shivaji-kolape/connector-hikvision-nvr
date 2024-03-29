"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""

DEFAULT_EXTENSION = '.mp4'

LOG_SEARCH_XML_PAYLOAD = """<?xml version: \"1.0\" encoding=\"utf-8\"?><CMSearchDescription><searchID>CA9B76C3-E890-0011-B657-C8E047E01E64</searchID><metaId>{metaID}</metaId><timeSpanList><timeSpan><startTime>{start_time}</startTime><endTime>{end_time}</endTime></timeSpan></timeSpanList><maxResults>{limit}</maxResults></CMSearchDescription>"""

GET_VIDEO_RECORDING_XML_PAYLOAD = """<?xml version: \"1.0\" encoding=\"utf-8\"?><CMSearchDescription><searchID>CAA56F7B-4170-0001-9D79-19E020301367</searchID><trackList><trackID>{trackid}</trackID></trackList><timeSpanList><timeSpan><startTime>{start_time}</startTime><endTime>{end_time}</endTime></timeSpan></timeSpanList><maxResults>{limit}</maxResults><searchResultPostion>0</searchResultPostion><metadataList><metadataDescriptor>recordType.meta.std-cgi.com</metadataDescriptor></metadataList></CMSearchDescription>"""
