from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_directories(File, SystemInfo):
    present = [
        "/etc/ssh"
    ]
    if SystemInfo.distribution != 'centos':
        present.append('/var/run/sshd')
    if present:
        for directory in present:
            d = File(directory)
            assert d.is_directory
            assert d.exists


def test_files(File):
    present = [
        "/etc/ssh/sshd_config",
        "/etc/issue.net"
    ]
    if present:
        for file in present:
            f = File(file)
            assert f.exists
            assert f.is_file


def test_service(Service, SystemInfo):
    if SystemInfo.distribution == 'centos':
        service = 'sshd'
    else:
        service = 'ssh'
    assert Service(service).is_enabled


def test_packages(Package):
    present = [
        "openssh-server"
    ]
    if present:
        for package in present:
            p = Package(package)
            assert p.is_installed
