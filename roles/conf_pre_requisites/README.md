Pre requisites tasks for Openshift
============

This role execute several basic tasks that need for Openshift.
 - Register Satellite/rhn
    - rhel-7-server-rpms
    - rhel-7-server-satellite-tools-6.1-rpms
    - rhel-7-server-extras-rpms
    - rhel-7-server-ose-3.3-rpms

 - Update Selinux
    - virt_use_nfs
    - virt_sandbox_use_nfs 

 - Install Essential Packages
    - "wget"
    - "git"
    - "net-tools"
    - "bind-utils"
    - "iptables-services"
    - "bridge-utils"
    - "bash-completion"
    - "nfs-utils"


Requirements
------------
For Satellite registeration, please customize tasks in main.yaml

Role Variables
--------------

From this role:

| Name                        | Default value                 | Required               | Description                                                                 |
|-----------------------------|-------------------------------|------------------------|-----------------------------------------------------------------------------|
| rhn_passwd                  | ''                            |    yes/no              | This is rhn password(If using rhn server, it is required)                   |
| yum_repolist                |   refer Example group_vars    |                        | Yum repositories for Openshift                                              |
| enssential_package_list     |   refer Example group_vars    |                        | Essential package list that will be installed                               |
| docker_version              |   refer Example group_vars    |                        | docker version will be installed                                            |

NOTICE: rhn_passwd is sensitive information so it recommand to use extra-vars parameter.

Dependencies
------------

Example Execute Command
-----------------------
```
ansible-playbook  ./pre_quisites.yaml  -vvv  --extra-vars rhn_passwd='password'
```

Example Playbook
----------------

```
 - name: Playbook sample
   hosts: all
   gather_facts: false

   roles:
    - { role: conf_pre_requisites }


```

Example group_vars
------------------
```
yum_repolist:
  - rhel-7-server-rpms
  - rhel-7-server-satellite-tools-6.1-rpms
  - rhel-7-server-extras-rpms
  - rhel-7-server-ose-3.3-rpms

essential_package_list:
  - wget
  - git
  - net-tools
  - bind-utils
  - iptables-services
  - bridge-utils
  - bash-completion
  - nfs-utils

docker_version: '1.9.1'
```

License
-------

Apache License Version 2.0

Author Information
------------------

Jooho Lee (jlee@redhat.com)
