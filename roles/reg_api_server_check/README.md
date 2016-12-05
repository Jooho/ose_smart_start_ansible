Regression Test - OCP SDN tunnelling check
============

This role check if sdn networking work via ping test
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

 - name: Check if sdn networking work via ping test
   hosts: all
   gather_facts: false

   roles:
    - { role: reg_sdn_check }


```

Example Result
--------------
```
master1.example.com 10.1.2.1 0%
master2.example.com 10.1.0.1 0%
```

License
-------

Apache License Version 2.0

Author Information
------------------

Jooho Lee (jlee@redhat.com)
