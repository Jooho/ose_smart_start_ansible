Regression Test - NODE Status Check
============

This role execute `oc get node` to check node status

Requirements
------------
The host that this role is executed can access OCP api server. Moreover, the oc user need at least `cluster-reader` role. 
Default host is the first vm of masters and it can be changed with `remote_test_host` variable.


Role Variables
--------------

From this role:

| Name                    | Default value                                 | Description                                                                 |
|-------------------------|-----------------------------------------------|-----------------------------------------------------------------------------|
| regression_result_path  | /tmp                                          | Regression Test result folder                                               |
| oc_login.user_id        | NONE                                          | OCP login user id                                                           |
| oc_login_password       | NONE                                          | OCP login password                                                          |
| oc_login.url            | NONE                                          | OCP api server url                                                          |
| remote_test_host        | ' '                                           | Test host can be changed due to firewall rule                               |

It is not recommaneded to save "oc_login_password" in group_var so please use extra_vars.
remote_test_host can be configured when ansible host can not reach to oc api server due to firewall rule.


Dependencies
------------


Example Execute Command
-----------------------
```
ansible-playbook  ./node_status.yaml  -vvv  --extra-vars oc_login_password='password'
```


Example Playbook
----------------

```
 - name: Check if nodes are ready
   hosts: masters[0]
   gather_facts: false

   roles:
    - { role: reg_node_status }

```

License
-------

Apache License Version 2.0

Author Information
------------------

Jooho Lee (jlee@redhat.com)
