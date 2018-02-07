import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_vault_group(host):
    host.group('vault').exists


def test_vault_user(host):
    host.user('vault').exists


def test_vault_binary(host):
    vault_binary = host.file('/usr/local/bin/vault')

    assert vault_binary.exists
