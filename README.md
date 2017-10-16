<a href="https://www.openssh.com/">
    <img src="https://upload.wikimedia.org/wikipedia/en/6/65/OpenSSH_logo.png" alt="openssh logo" title="openssh" align="right" height="60" />
</a>

Ansible Role: sshd
==================

[![Build Status](https://travis-ci.org/SoInteractive/ansible-sshd.svg?branch=master)](https://travis-ci.org/SoInteractive/ansible-sshd)  [![License: MIT](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT) [![Ansible Role](https://img.shields.io/badge/ansible%20role-SoInteractive.sshd-blue.svg)](https://galaxy.ansible.com/SoInteractive/sshd/) [![GitHub tag](https://img.shields.io/github/tag/sointeractive/ansible-sshd.svg)](https://github.com/SoInteractive/ansible-sshd/tags) [![Twitter URL](https://img.shields.io/twitter/follow/sointeractive.svg?style=social&label=Follow%20%40SoInteractive)](https://twitter.com/sointeractive)

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
