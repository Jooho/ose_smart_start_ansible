# OpenShift Smart Start Ansible Script
This ansible script is developed for who use Openshift. This project is based on [ose_smart_start](https://github.com/Jooho/ose_smart_start) which is developed by bash shell. Mainly, it contains regression test, sample applications, ad-hoc and so on. Each role can be executable independently and it can be executed in a playbook.

# Playbooks
## Regression Test (playbooks/regression_test)
This playbook check Openshift environment and show it has any problems or not.

### Top Level Playbook(playbooks/)
This playbook includes seveal regression test playbooks

- regression.yaml

### Playbook
Indepentant playbook

- api_server_check.yaml
- default_project_check.yaml
- dns_check.yaml
- external_registry_check.yaml
- external_resource_access_check.yaml
- imageStream_deploy.retry
- imageStream_deploy.yaml
- internal_registry_check.yaml
- local_storage_check.yaml
- node_status.yaml
- openshift_ex_diagnostic.yaml
- s2i_build.yaml
- sdn_check.yaml
- squid_status.yaml

## Sample applications (playbooks/sample_app)
These playbooks deploy sample applications like eap ssl/hello openshift(ssl/non ssl)

### Playbook
- eap_ssl.yaml  
- hello_openshift.yaml 

# Roles
## Template Role
- template_role

## Regression Test (prefix: reg) 
- reg_api_server_check
- reg_default_project_check
- reg_dns_check
- reg_external_registry_check
- reg_external_resource_access_check
- reg_imageStream_deploy
- reg_internal_registry_check
- reg_local_storage_check
- reg_node_status
- reg_openshift_diagnostics_cmd
- reg_s2i_build
- reg_sdn_check
- reg_squid_status

## Sample Application (prefix: sample)

- sample_eap_ssl
- sample_hello_openshift
