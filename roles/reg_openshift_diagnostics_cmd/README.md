Regression Test - OCP cluster diagnostic by openshift command
============

This role execute `openshift ex diagnotics` and show Warnings and Errors

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
 - name: Execute Openshift diagnostics command
   hosts: masters[0]

   roles:
    - { role: reg_openshift_diagnostics_cmd }

```

License
-------

Apache License Version 2.0

Author Information
------------------

Jooho Lee (jlee@redhat.com)
