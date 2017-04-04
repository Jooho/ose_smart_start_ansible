# ORIGIN ANSIBLE
This is angularJS 2 application to display regression report at the moment.

## How to Deploy Application:

** 1.Using Docker ** 
  ```
docker run -d ljhiyh/origin-ansible 
  ```
** 2. Using Source **
  ```
$ sudo yum install nodejs npm   or   sudo yum install nodejs npm --enablerepo=epel
  
$ git clone https://github.com/Jooho/origin_ansible.git
  
$ cd origin_ansible
  
$ npm install
  
$ npm start
  ```
  
## Screenshot

** 1. Open Browser (Go to http://IP:8080) **
![alt text][origin_ansible_first_page]

** 2. Click Data Menu and Put Report Data(report.json) **
![alt text][origin_ansible_data_page]

** 3. Click Report **
![alt text][origin_ansible_report_page]

[origin_ansible_first_page]: ./images/origin_ansible_first_page.JPG
[origin_ansible_data_page]: ./images/origin_ansible_data_page.JPG
[origin_ansible_report_page]: ./images/origin_ansible_report_page.JPG
