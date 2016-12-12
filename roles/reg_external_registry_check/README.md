Regression Test - External Docker Registry Check
============

If external docker regitstry is used instread of registry.access.redhat.com, this role help check if it is accessible from OCP hosts and be possible to download images.

Requirements
------------
The host that this role is executed need certs file for external docker regitstry under /etc/docker/certs.d/{{external_registry.url }}
Default host is the first vm of masters and it can be changed with `remote_test_host` variable.

Role Variables
--------------

From this role:

| Name                    | Default value                                 | Description                                                                 |
|-------------------------|-----------------------------------------------|-----------------------------------------------------------------------------|
| regression_result_path  | /tmp                                          | Regression Test result folder                                               |
| external_registry.user_id   |  NONE                                     | External registry login user id                                             |
| external_registry.email | NONE                                          | External registry login email                                               |
| external_registry.url   | NONE                                          | External registry login url                                                 |
| external_registry_password  | NONE                                      | External registry login password(NOTE: variable name format different       |
| remote_test_host        | ' '                                           | Test host can be changed due to firewall rule                               |

It is not recommaneded to save "external_registry_password" in group_var so please use extra_vars.
remote_test_host can be configured when ansible host can not reach to oc api server due to firewall rule.




Dependencies
------------

Example Execute Command
-----------------------
```
ansible-playbook  ./external_registry_check.yaml    --extra-vars=external_registry_password='password' -vvv
```

Example Playbook
----------------

```
 - name: Check external registry : docker login/docker pull
   hosts: all
   gather_facts: false

   roles:
    - { role: reg_external_registry_check }


```

Example group_vars
------------------
```
external_registry: {user_id: "user", email: "test@gmail.com", url: "external-registry.com:5000"}
```

Example Result (2 files)
--------------
reg_external_registry_check_result_1
```
master1.example.com docker_login:0
node1.example.com docker_login:0
```

reg_external_registry_check_result_2
```
master1.example.com docker_pull:0
node1.example.com docker_pull:0
```
License
-------

Apache License Version 2.0

Author Information
------------------

Jooho Lee (jlee@redhat.com)
