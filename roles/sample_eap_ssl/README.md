Regression Test - Sample Application - EAP SSL
============

This role deploy eap ssl application which use self signed cert

Requirements
------------

Role Variables
--------------

From this role:

| Name                        | Default value                                 | Description                                                                 |
|-----------------------------|-----------------------------------------------|-----------------------------------------------------------------------------|
| regression_result_path      | /tmp                                          | Regression Test result folder                                               |
| oc_login.user_id            | NONE                                          | OCP login user id                                                           |
| oc_login_password           | NONE                                          | OCP login password                                                          |
| oc_login.url                | NONE                                          | OCP api server url                                                          |
| internal_registry_test_host | ' '                                           | Test host can be changed due to firewall rule                               |

It is not recommaneded to save "oc_login_password" in group_var so please use extra_vars.


Dependencies
------------

Example Execute Command
-----------------------
```
ansible-playbook  playbooks/sample_app/eap_ssl.yaml  -vvv  --extra-vars oc_login_password='password'
```

Example Playbook
----------------

```
 - name: Deploy SSL EAP Test Application
   hosts: masters[0]
   gather_facts: false
   sudo: true

   roles:
    - { role: sample_eap_ssl }

```

Example group_vars
------------------
```
oc_login: {user_id: "OpenShiftAdmin", url: "https://api.sbx.cloudapps.ao.dcn:8443"}
oc_login_password: "password"
internal_registry_test_host: dev001.example.com
```

License
-------

Apache License Version 2.0

Author Information
------------------

Jooho Lee (jlee@redhat.com)
