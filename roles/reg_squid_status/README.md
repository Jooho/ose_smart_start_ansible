Regression Test - Squid Test
============

This role test squid related information
 - squid is started
 - svc/eq exist

Requirements
------------

Role Variables
--------------

From this role:

| Name                    | Default value                                 | Description                                                                 |
|-------------------------|-----------------------------------------------|-----------------------------------------------------------------------------|
| regression_result_path  | /tmp                                          | Regression Test result folder                                               |
| squid_vms               | null                                          | If squid is used, squid vms can be listed                                   |


*squid_vms example*
~~~
squid_vms:
  - master1.example.com
  - master2.example.com
~~~

Dependencies
------------


Example Playbook
----------------

```

---
 - include: ../common/master_config_facts.yaml
 - name: Check if squid service is Runnig and svc/ep exist
   hosts: all
   gather_facts: false

   roles:
    - { role: reg_squid_status }

```

Example Result
-------------

```


```

License
-------

Apache License Version 2.0

Author Information
------------------

Jooho Lee (jlee@redhat.com)
