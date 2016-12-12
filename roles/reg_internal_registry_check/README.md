Regression Test - Internal  Docker Registry Check
============

This role check integrated docker regitstry - oc login/docker login/docker push/docker pull

Requirements
------------
The host that this role is executed need certs file for integrated docker regitstry under /etc/docker/certs.d/{{internal_registry.url }}
Default host is the first vm of masters and it can be changed with `remote_test_host` variable.


Role Variables
--------------

From this role:

| Name                        | Default value                                 | Description                                                                 |
|-----------------------------|-----------------------------------------------|-----------------------------------------------------------------------------|
| regression_result_path      | /tmp                                          | Regression Test result folder                                               |
| internal_registry.user_id   | NONE                                          | Internal registry login user id                                             |
| internal_registry.email     | NONE                                          | Internal registry login email                                               |
| internal_registry.url       | ' '                                           | Internal registry login url                                                 |
| oc_login.user_id            | NONE                                          | OCP login user id                                                           |
| oc_login_password           | NONE                                          | OCP login password                                                          |
| oc_login.url                | NONE                                          | OCP api server url                                                          |
| remote_test_host            | ' '                                           | Test host can be changed due to firewall rule                               |

It is not recommaneded to save "oc_login_password" in group_var so please use extra_vars.
remote_test_host can be configured when ansible host can not reach to oc api server due to firewall rule.

Dependencies
------------

Example Execute Command
-----------------------
```
ansible-playbook  ./internal_registry_check.yaml  -vvv  --extra-vars oc_login_password='password'
```

Example Playbook
----------------

```
 - name: Check internal registry via router - oc login/docker login/docker push/docker pull
   hosts: all
   gather_facts: false

   roles:
    - { role: reg_internal_registry_check }


```

Example group_vars
------------------
```
internal_registry: {user_id: "OpenShiftAdmin", email: "test@gmail.com", url: "registry.sbx.cloudapps.ao.dcn"}
oc_login: {user_id: "OpenShiftAdmin", url: "https://api.sbx.cloudapps.ao.dcn:8443"}
oc_login_password: "password"
remote_test_host: dev001.example.com
```

Example Result 
--------------
reg_internal_registry_check_result_1
```
0 0 0 0 0 0 0 0 0
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
