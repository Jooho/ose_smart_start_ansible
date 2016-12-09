Regression Test - OCP API Server Health Check
============

This role check if api server is running via health check url
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

 - name: Check if api server is running via health check url
   hosts: all
   gather_facts: false

   roles:
    - { role: reg_api_server_check  }


```

Example Result
--------------
```
master1.example.com ok
master2.example.com ok
```

License
-------

Apache License Version 2.0

Author Information
------------------

Jooho Lee (jlee@redhat.com)
