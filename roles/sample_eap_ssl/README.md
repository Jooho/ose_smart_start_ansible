Sample Application - EAP SSL
============

This role deploy eap ssl application which use self signed cert

Requirements
------------

Role Variables
--------------

From this role:

| Name                        | Default value                                 | Description                                                                 |
|-----------------------------|-----------------------------------------------|-----------------------------------------------------------------------------|
| regression_result_path      | /tmp                                          | If it set, Regression Test result folder will be used to save files         |
| oc_login.user_id            | NONE                                          | OCP login user id                                                           |
| oc_login_password           | NONE                                          | OCP login password                                                          |
| oc_login.url                | NONE                                          | OCP api server url                                                          |
| remote_test_host            | ' '                                           | Test Host to execute oc commands                                          |


It is not recommaneded to save "oc_login_password" in group_var so please use extra_vars.
remote_test_host can be configured when ansible host can not reach to oc api server due to firewall rule.

Dependencies
------------

Example Execute Command
-----------------------
```
ansible-playbook  playbooks/sample_app/eap_ssl.yaml   --extra-vars '{oc_login: {"url":"https://master1.example.com:8443", "user_id":"test"}}' --extra-vars oc_login_password='password' -vvvv
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
oc_login: {user_id: "OpenShiftAdmin", url: "https://api.example.com:8443"}
oc_login_password: "password"
remote_test_host: dev001.example.com
```
Test URL
--------
```
http://eap-app-test.sbx.cloudapps.ao.dcn/index.jsf
https://secure-eap-app-test.sbx.cloudapps.ao.dcn/index.jsf
```
License
-------

Apache License Version 2.0

Author Information
------------------

Jooho Lee (jlee@redhat.com)
