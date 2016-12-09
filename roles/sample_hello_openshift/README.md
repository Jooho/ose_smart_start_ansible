Regression Test - Sample Application - Hello Openshift
============

This role deploy Hello Openshift ssl/non-ssl application which use self signed cert

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
| remote_test_host            | ' '                                           | Test host can be changed due to firewall rule                               |
| hello_openshift_certs       | NONE                                          | Specify certificate path and hostname for ssl                               |

It is not recommaneded to save "oc_login_password" in group_var so please use extra_vars.


Dependencies
------------

Example Execute Command
-----------------------
```
ansible-playbook  playbooks/sample_app/hello-openshift.yaml  -vvv  --extra-vars oc_login_password='password'
```

Example Playbook
----------------

```
 - name: Deploy Hello Openshift SSL/NON-SSL application
   hosts: masters[0]
   gather_facts: false
   sudo: true

   roles:
    - { role: sample_hello_openshift }

```

Example group_vars
------------------
```
oc_login: {user_id: "OpenShiftAdmin", url: "https://api.sbx.cloudapps.ao.dcn:8443"}
oc_login_password: "password"
hello_openshift_certs: { path: "/etc/origin/master", hostname: "secure-hello-openshift.sbx.cloudapps.ao.dcn" }
remote_test_host: dev001.example.com
```

License
-------

Apache License Version 2.0

Author Information
------------------

Jooho Lee (jlee@redhat.com)
