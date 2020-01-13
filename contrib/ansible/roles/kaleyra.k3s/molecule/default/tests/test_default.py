import os
from pprint import pprint
import sys

import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_hosts_file(host):

    sysctls = host.file('/etc/sysctl.conf')

    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'

    if host.backend.get_hostname() == 'master-1':
        print('masterioso')
    else:
        print(os.environ.get('OS'))
