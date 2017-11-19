from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_directories(host):
    present = [
        "/etc/ssh"
    ]
    if host.system_info.distribution != 'centos':
        present.append('/var/run/sshd')
    if present:
        for directory in present:
            d = host.file(directory)
            assert d.is_directory
            assert d.exists


def test_files(host):
    present = [
        "/etc/ssh/sshd_config",
        "/etc/issue.net"
    ]
    if present:
        for file in present:
            f = host.file(file)
            assert f.exists
            assert f.is_file


def test_service(host):
    if host.system_info.distribution == 'centos':
        service = 'sshd'
    else:
        service = 'ssh'
    assert host.service(service).is_enabled


def test_packages(host):
    present = [
        "openssh-server"
    ]
    if present:
        for package in present:
            p = host.package(package)
            assert p.is_installed
