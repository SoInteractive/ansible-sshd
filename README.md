sshd
========

Ansible role to manage SSH server settings

Requirements
------------

None

Examples
--------

Use it in a playbook as follows:
```yaml
- hosts: all
  become: true
  roles:
    - sshd
```

Have a look at [defaults/main.yml](defaults/main.yml) for role variables
that can be overridden.
