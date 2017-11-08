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
| oc_login.user_id        | NONE                                          | OCP login user id                                                           |
| oc_login_password       | NONE                                          | OCP login password                                                          |
| oc_login.url            | NONE                                          | OCP api server url                                                          |
| remote_test_host        | ' '                                           | Test host can be changed due to firewall rule                               |



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

Example group_vars
------------------
```
squid_vms:
  - master1.example.com
  - master2.example.com
oc_login: {user_id: "OpenShiftAdmin", url: "https://api.example.com:8443"}
oc_login_password: "password"
remote_test_host: dev001.example.com
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
