#!/usr/bin/python3
"""
Get all hosts for your organization returns "OK" response
"""

# Install the library and its dependencies 
pip3 install datadog-api-client

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.hosts_api import HostsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = HostsApi(api_client)
    response = api_instance.list_hosts(
        filter="env:ci",
    )

    print(response)
