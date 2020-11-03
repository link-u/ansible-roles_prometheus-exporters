import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_installed_package(host):
    assert host.package("prometheus-exporter-deck").is_installed

def test_run_help_command(host):
    assert host.run("/usr/sbin/cradle_exporter -h").succeeded
