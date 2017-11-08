Regression Test - Template ROLE
============

$description

Requirements
------------


Role Variables
--------------

From this role:

| Name                        | Default value                                 | Description                                                                 |
|-----------------------------|-----------------------------------------------|-----------------------------------------------------------------------------|
| regression_result_path      | /tmp                                          | Regression Test result folder                                               |


Dependencies
------------

Example Execute Command
-----------------------
```
ansible-playbook  ./$ROLE_PLAYBOOK.yaml  -vvv  --extra-vars oc_login_password='password'
```

Example Playbook
----------------

```
 - name: Playbook sample
   hosts: all
   gather_facts: false

   roles:
    - { role: $ROLE_NAME }


```

Example group_vars
------------------
```
$SAMPLE_GROUP_VARS
```

Example Result 
--------------
$RESULT_FILE_NAME
```
$RESULT VALUE
```

Report Rule
-----------
```
$RESULT_RULE
```

License
-------

Apache License Version 2.0

Author Information
------------------

Jooho Lee (jlee@redhat.com)
