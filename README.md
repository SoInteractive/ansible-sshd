<a href="https://www.openssh.com/">
    <img src="https://upload.wikimedia.org/wikipedia/en/6/65/OpenSSH_logo.png" alt="openssh logo" title="openssh" align="right" height="60" />
</a>

Ansible Role: sshd
==================

[![Build Status](https://ci.devops.sosoftware.pl/buildStatus/icon?job=SoInteractive/sshd/master)](https://ci.devops.sosoftware.pl/job/SoInteractive/sshd/master) [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT) [![Ansible Role](https://img.shields.io/ansible/role/18224.svg)](https://galaxy.ansible.com/SoInteractive/sshd/) [![Twitter URL](https://img.shields.io/twitter/follow/sointeractive.svg?style=social&label=Follow%20%40SoInteractive)](https://twitter.com/sointeractive)

Ansible role to manage SSH server settings

Examples
--------

Use it in a playbook as follows:
```yaml
- hosts: all
  become: true
  roles:
    - SoInteractive.sshd
```

Have a look at [defaults/main.yml](defaults/main.yml) for role variables that can be overridden.
