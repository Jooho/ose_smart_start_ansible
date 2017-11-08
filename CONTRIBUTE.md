# Guide to Contribute

## Preparation  

*Global Property*
```
export NEW_ANSIBLE_INVENTORY_DIR=contribute
export NEW_PLAYBOOK=ping_test
export NEW_ROLE=reg_ping_test
```

*Clone git repository*
```
git clone https://github.com/Jooho/ose_smart_start_ansible.git
cd ose_smart_start_ansible
```

*Place Test ansible hosts file in inventory folder*
```
cp -R ose_smart_start_ansible/inventories/default  ose_smart_start_ansible/inventories/$NEW_ANSIBLE_INVENTORY_DIR

# Modify hosts file according to your env
vi ose_smart_start_ansible/inventories/$NEW_ANSIBLE_INVENTORY_DIR/hosts
```

## Development Flow Example for regression test role (prefix: reg)

*Copy template playbook to specific playbook name*
```
cp ose_smart_start_ansible/playbooks/template_playbook.yaml ose_smart_start_ansible/playbooks/regression_test/$NEW_PLAYBOOK

#Update playbook
vi ose_smart_start_ansible/playbooks/$NEW_PLAYBOOK
```

*Copy template role to specific role name*
```
cp -R ose_smart_start_ansible/roles/template_role   ose_smart_start_ansible/roles/$NEW_ROLE
```

*Update tasks (groups_var if you need)*
```
vi ose_smart_start_ansible/roles/$NEW_ROLE/tasks/main.yaml

vi ose_smart_start_ansible/inventories/$NEW_ANSIBLE_INVENTORY_DIR/group_vars/all
```

*Execute playbook*
```
$ pwd 
/ose_smart_start_ansible

$ ansible-playbook -i ./inventories/$NEW_ANSIBLE_INVENTORY_DIR/hosts ./playbooks/regression_test/$NEW_PLAYBOOK -vvv
```

*Update ROLE README.md*
```
vi ose_smart_start_ansible/roles/$NEW_ROLE/README.md
```

NOW, you are ready to commit PR!!!

If you have any questions, please send me email(ljhiyh@gmail.com) !!
