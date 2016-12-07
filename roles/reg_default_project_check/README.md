Regression Test - OCP Default project pod status
============

This role check pods status in default project

Requirements
------------

Role Variables
--------------

From this role:

| Name                    | Default value                                 | Description                                                                 |
|-------------------------|-----------------------------------------------|-----------------------------------------------------------------------------|
| regression_result_path  | /tmp                                          | Regression Test result folder                                               |



Dependencies
------------

Example Execute Command
-----------------------

Example Playbook
----------------

```
 - name: Check if pods in default project are running
   hosts: masters[0]
   gather_facts: false

   roles:
    - { role: reg_default_project_check }

```

Example group_vars
------------------

Example Result 
--------------
```
docker-registry-5-zvng7 1/1 Running 1  SUCCESS
router-1-bmbcx 1/1 Running 1  SUCCESS
router-1-w4lpd 1/1 Running 1  SUCCESS
```
License
-------

Apache License Version 2.0

Author Information
------------------

Jooho Lee (jlee@redhat.com)
