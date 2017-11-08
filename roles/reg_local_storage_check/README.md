Regression Test - Local Storage Used Size
============

This role check if local storage has enough space
 - 100% : FAIL
 - 99% - 80% : WARN 
 - 79% - 70% : INFO

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
 - name: Check if local storage has enough spaces. Full of /var, /var/log, /var/lib/docker and docker-pool can impact OCP.
   hosts: all
   gather_facts: false

   roles:
    - { role: reg_local_storage_check }

```

Example group_vars
------------------


Example Result 
--------------
reg_reg_imageStream_deploy_result_1
```
master1.example.com /var/log INFO:74%
master2.example.com docker-pool INFO:78%
```

Report Rule
-----------
```
report-rule.yaml.j2
```

License
-------

Apache License Version 2.0

Author Information
------------------

Jooho Lee (jlee@redhat.com)
