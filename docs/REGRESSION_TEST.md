## Full Regression Test ##

1. Copy ansible hosts file to ose_smart_start_ansible/inventories/default/
  ```
cp $YOUR_ANSIBLE_HOSTS_FILE ose_smart_start_ansible/inventories/default/.
  ```

2. Update group_vars according to your environment. 
  ```
# vi ose_smart_start_ansible/blob/master/inventories/default/group_vars/all

regression_result_path: "/tmp/example"
squid_vms:
  - master1.example.com

firewall_between_master_node: yes
external_registry: {user_id: "test", email: "test@gmail.com", url: "external.docker-registry.com:5000"}
internal_registry: {user_id: "OpenShiftAdmin", email: "test@gmail.com", url: "registry.cloudapps.example.com"}
oc_login: {user_id: "OpenShiftAdmin", url: "https://master1.example.com:8443"}

external_resources:
  - { url: "github.com", proxy: "", port: "443" }
  - { url: "external.docker-registry.com", proxy: "", port: "22,443,5000" }  

hello_openshift_certs: { path: "/etc/origin/master", hostname: "secure-hello-openshift.cloudapps.example.com" }
remote_test_host: 'node1.example.com'
  ```

3. Execute Ansible Playbook
  ```
# cd ose_smart_start_ansible
# ansible-playbook -i ../inventories/default/$YOUR_ANSIBLE_HOSTS_FILE   --extra-vars external_registry_password='$JENIE_PASSWORD'  --extra-vars oc_login_password='$OpenShiftAdmin_PASSWORD'  -M ../library/  -vvv
Check Result Files:
   egrep -v  "SUCCESS|started| 0%|Ready|INFO|WARN|open|Warnings" /tmp/example/reg*result*
  ```

## Custom Regression Test ##

1. Copy ansible hosts file to ose_smart_start_ansible/inventories/default/
  ```
cp $YOUR_ANSIBLE_HOSTS_FILE ose_smart_start_ansible/inventories/default/.
  ```
  
2. Customize Regression Test Playbook (Choose only some regression roles)
  ```
vi ose_smart_start_ansible/playbooks/regression.yaml

# Regression Test Playbook

   - include: ./regression_test/set_up.yaml
   - include: ./regression_test/internal_registry_check.yaml      <======= only one Role!!

...
..
  ```
      
3. Update group_vars for selected roles
  ```
# vi ose_smart_start_ansible/blob/master/inventories/default/group_vars/all

internal_registry: {user_id: "OpenShiftAdmin", email: "test@gmail.com", url: "registry.cloudapps.example.com"}
oc_login: {user_id: "OpenShiftAdmin", url: "https://master1.example.com:8443"}

  ```
  
4. Excute Ansible Playbook

  ```
# cd ose_smart_start_ansible
# ansible-playbook -i ../inventories/default/$YOUR_ANSIBLE_HOSTS_FILE   --extra-vars external_registry_password='$JENIE_PASSWORD'  --extra-vars oc_login_password='$OpenShiftAdmin_PASSWORD'  -M ../library/  -vvv
  ```

## Result 

All parameters are defined in group_vars
Result Path : `{{ regression_result_path }}`

Report Path : `{{ regression_report_path if regression_report_path is defined else regression_report_path }}`

Report file : `{{ regression_report_path if regression_report_path is defined else regression_result_path }}/report.json`

### Check if Regression Test Result:
#### Option1. Using Command:
 Execute following command. Then if you see nothing, it means regression test success. 
  ```
egrep -v  "SUCCESS|started| 0%|Ready|INFO|WARN|open|Warnings" {{ regression_result_path }}/reg*result*
  ```
  
#### Option2. Using Application:
  [How to deploy Regression Web application?](https://github.com/Jooho/ose_smart_start_ansible/blob/master/docs/ORIGIN_ANSIBLE.md)
