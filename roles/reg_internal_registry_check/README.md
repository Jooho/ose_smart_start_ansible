Regression Test - Internal  Docker Registry Check
============

This role check integrated docker regitstry - oc login/docker login/docker push/docker pull

Requirements
------------

Role Variables
--------------

From this role:

| Name                    | Default value                                 | Description                                                                 |
|-------------------------|-----------------------------------------------|-----------------------------------------------------------------------------|
| regression_result_path  | /tmp                                          | Regression Test result folder                                               |
| internal_registry.user_id   |  NONE                                     | Internal registry login user id                                             |
| internal_registry.email | NONE                                          | Internal registry login email                                               |
| internal_registry.url   | ' '                                           | Internal registry login url                                                 |
| oc_login.user_id        | NONE                                          | Internal registry login password(NOTE: variable name format different       |
| oc_login.url            | NONE                                          | Internal registry login password(NOTE: variable name format different       |
| oc_login_password       | NONE                                          | Internal registry login password(NOTE: variable name format different       |

It is not recommaneded to save "oc_login_password" in group_var so please use extra_vars.


Dependencies
------------

Example Execute Command
-----------------------
```
ansible-playbook  ./internal_registry_check.yaml  -vvv  --extra-vars=oc_login_password='password'
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
```

Example Result (2 files)
--------------
reg_internal_registry_check_result_1
```
aoappd-e-mgt001.ctho.asbn.gtwy.dcn docker_login:0
aoappd-e-mgt002.ctho.asbn.gtwy.dcn docker_login:0
```

reg_internal_registry_check_result_2
```
aoappd-e-mgt001.ctho.asbn.gtwy.dcn docker_pull:0
aoappd-e-mgt002.ctho.asbn.gtwy.dcn docker_pull:0
```
License
-------

Apache License Version 2.0

Author Information
------------------

Jooho Lee (jlee@redhat.com)
