Regression Test - External Resources Accessiblity Check
============

This role check the accessiblity to external resources such as github.com/gitlab.com from OCP hosts.

Requirements
------------

Role Variables
--------------

From this role:

| Name                    | Default value                                 | Description                                                                 |
|-------------------------|-----------------------------------------------|-----------------------------------------------------------------------------|
| regression_result_path  | /tmp                                          | Regression Test result folder                                               |
| external_resources.url   |  NONE                                     | External Resource URL                                             |
| external_resources.proxy | NONE                                          | set proxy url, if external Resource can be reachable via proxy                                               |
| external_resources.port   | NONE                                          | External Resource port                                                 |


Dependencies
------------

Example Execute Command
-----------------------

Example Playbook
----------------

```
 - name: Check the accessibility to external resources from OCP nodes - github.com , gitlab.com
   hosts: all
   gather_facts: false

   roles:
    - { role: reg_external_resource_access_check  }


```

Example group_vars
------------------
```
external_resources:
  - { url: "github.com", proxy: "", port: "22" }
  - { url: "gitlab.com", proxy: "", port: "22,5000" }
 ```

Example Result (2 files)
--------------
```
master1.example.com github.com 22/tcp open
master1.example.com gitlab.com 22/tcp open
master1.example.com gitlab.com 5000/tcp open

```
To_Do
-----
proxy variable is not working yet.

License
-------

Apache License Version 2.0

Author Information
------------------

Jooho Lee (jlee@redhat.com)
