Regression Test - NODE Status Check
============

This role execute `oc get node` to check node status

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
 - name: Check if nodes are ready
   hosts: masters[0]
   gather_facts: false

   roles:
    - { role: reg_node_status }

```

License
-------

Apache License Version 2.0

Author Information
------------------

Jooho Lee (jlee@redhat.com)
