Copy SSH Key to NODE
============

This role copy public ssh key from ansible host to other nodes where ansible host should access.

Requirements
------------


Role Variables
--------------

From this role:

| Name                        | Default value                                 | Description                                                                 |
|-----------------------------|-----------------------------------------------|-----------------------------------------------------------------------------|
| node_passwd                 | ''                                            | This ssh login password(id is ansible_user in hosts file)                   |
|                             |                                               | It assume all nodes has same password                                        |

NOTICE: node_passwd is sensitive information so it recommand to use extra-vars parameter.

Dependencies
------------

Example Execute Command
-----------------------
```
ansible-playbook  ./$ROLE_PLAYBOOK.yaml  -vvv  --extra-vars node_passwd='password'
```

Example Playbook
----------------

```
 - name: Playbook sample
   hosts: all
   gather_facts: false

   roles:
    - { role: conf_copy_ssh_key }
```

Example group_vars
------------------
```
```

License
-------

Apache License Version 2.0

Author Information
------------------

Jooho Lee (jlee@redhat.com)
