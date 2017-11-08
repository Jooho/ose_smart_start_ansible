#ANSIBLE HINT DOC
This doc give some practical examples can be used in a real world. 


## Extra Variable
**Example 1**
~~~
ansible-playbook  $PLAYBOOK   --extra-vars '{oc_login: {"url":"https://master1.example.com:8443", "user_id":"test"}}' --extra-vars oc_login_password='password' -vvvv
~~~
