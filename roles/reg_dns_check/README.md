Regression Test - Check DNS Entries
============

This role check if DNS can resolve all hostname in OCP cluster

Requirements
------------

Role Variables
--------------

From this role:

| Name                    | Default value                                 | Description                                                                 |
|-------------------------|-----------------------------------------------|-----------------------------------------------------------------------------|
| regression_result_path  | /tmp                                          | Regression Test result folder                                               |

Dependencies
------------


Example Playbook
----------------

```
- name: Check if DNS can resolve all hostname((master/etcd/master/lb/nfs[if nfs group exist]) in OCP cluster
  hosts: all
  gather_facts: false

   roles:
    - { role: reg_dns_check}

```
Example group_vars
------------------
```
regression_result_path: "/home/oseadmin"
```
License
-------

Apache License Version 2.0

Author Information
------------------

Jooho Lee (jlee@redhat.com)
