Regression Test - Deploy App from ImageStream (no build)
============

This role check if OCP deploy app with ImageStream (no build)

Requirements
------------
The host that this role is executed should access to TEST application page(80,443 port)
Default host is the ansible executed vm  and it can be changed with `remote_test_host` variable.


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

It is not recommaneded to save "oc_login_password" in group_var so please use extra_vars.
remote_test_host can be configured when ansible host can not reach to oc api server due to firewall rule.

Dependencies
------------

Example Execute Command
-----------------------
```
ansible-playbook  ./imageStream_deploy.yaml --extra-vars oc_login_password='password'  -vvvv
```

Example Playbook
----------------

```
 - name: Check if deploying application with ImageStream (no build)
   hosts: all
   gather_facts: false

   roles:
    - { role: reg_imageStream_deploy }


```

Example group_vars
------------------
```
internal_registry: {user_id: "OpenShiftAdmin", email: "test@gmail.com", url: "registry.cloudapps.example.com"}
oc_login: {user_id: "OpenShiftAdmin", url: "https://api.example.com:8443"}
oc_login_password: "password"
remote_test_host: dev001.example.com
```

Example Result 
--------------
reg_reg_imageStream_deploy_result_1
```
0 
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
