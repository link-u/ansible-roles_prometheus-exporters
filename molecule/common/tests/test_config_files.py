import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_has_config_file(host):
    assert host.file("/etc/gazer/config.yml").exists
    assert host.file("/etc/gazer/conf.d/cradle-self-monitor").exists
