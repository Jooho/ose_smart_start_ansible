import os, sys, re, time
import json
from datetime import datetime

STRING_SUCCESS="SUCCESS"
STRING_FAIL="FAIL"
STRING_WARN="WARN"

DOCUMENTATION = '''
---
module: regression_report.py
short_description: 
description:
'''

EXAMPLES = '''
# Default invocation, only notify about expired certificates or certificates which will expire within 30 days from now
#- regression_report:
'''



######################################################################
# This is our module MAIN function after all, so there's bound to be a
# lot of code bundled up into one block
#
# pylint: disable=too-many-locals,too-many-locals,too-many-statements,too-many-branches
def main():
  module = AnsibleModule(
        argument_spec=dict(
            result_path=dict(
                required=True,
                type='str'),
            report_path=dict(
                required=False,
                default="/tmp",
                type='str'),
            backup=dict(
                required=False,
                default=True,
                type='bool'),
            title=dict(
                required=False,
                default="Report",
                type='str')
        )
  )

  ####################
  #Initialze Variable#

  final_json = {}
  final_role = {}
  final_role_list = []
  final_col_data = []
  result_item = []
  result_item_list = []
  report_file_dict = {}
  role_name = ""
  role_list = []
  report_file_dict = {}

  report_result = STRING_SUCCESS
  role_result = STRING_SUCCESS

  result_path = module.params['result_path']
  report_path = module.params['report_path']
  report_title = module.params['title']
  report_backup = module.params['backup']
  report_file = "report.json"


  ######################################################################
  # Sure, why not? Let's enable check mode.
#  if module.check_mode:
#      check_results['final_json'] = []
#      module.exit_json(
#          check_results=check_results,
#          msg="Checked 0 report title: $s, result_path: %s" % (module.params['title'], module.params['path']),
#          rc=0,
#          changed=False
#      )

  
  # Open a file
  if not os.path.exists(result_path):
    module.fail_json(msg='result folder(%s) does not exist' % (result_path))
  elif not os.path.exists(report_path):
    module.fail_json(msg='report folder(%s) does not exist' % (report_path))
  else: 
    report_dirs = os.listdir( result_path )
    if report_backup and os.path.exists(report_path + "/" + report_file):
      modifiedTime = os.path.getmtime(report_path + "/" + report_file)
      timeStamp =  datetime.fromtimestamp(modifiedTime).strftime('%Y%m%d_%H%M%S')
      os.rename(report_path + "/" + report_file,report_path + "/" + report_file + "_" +timeStamp) 

  # This would print all the files and directories
  
  for file in report_dirs:
    if re.match('reg_(.*)_result',file) != None:
      start = file.find('reg_')
      end = file.find('_result',start)
      role_name=file[start:end]
      if role_name not in role_list:
        role_list.append(role_name)
           
  for role in role_list:
    role_rule_file_list = []
    role_result_file_list = []
    role_raw_file_list = []
  
    for file in report_dirs:
      if re.match(role+'_rule$',file) != None:
        role_rule_file_list.append(file)
  
      if re.match(role+'_result',file) != None and re.match('(.*)temp(.*)',file) == None:
        role_result_file_list.append(file)

      if re.match(role+'_raw',file) != None and  re.match('(.*)lock$',file) == None:
        role_raw_file_list.append(file)
    report_file_dict[role]=[list(role_rule_file_list), list(role_result_file_list), list(role_raw_file_list)]
  
  
  
  # Mapping json to python   (JSON var ==> Python var)
  #
  # final_json {
  #   tile: " ",
  #   result: "",
  #   role_list: {     ==> final_role
  #      title: "",  
  #      role_name: "",
  #      role_result: "",
  #      col_data: {     ==> final_col_data
  #         name: "",
  #         desc: "",
  #         display: "",
  #         type: ""
  #      },
  #      result_data_list: [      ==> final_result_data_list
  #        [
  #          {
  #            result_data: [     ==> final_result_data
  #              [
  #                {
  #                   name: "",   ==>  result_each_key_value['name']= col_name      -+| --> result_item     --+
  #                   value: ""                                                     -+|                       |
  #                 },                                                                                        |
  #                 {                                                                                         +-----> result_item_list
  #                   name: "",                                                                               |
  #                   value: ""                                                                             --+
  #                 }
  #               ]
  #            ],
  #            "col": [           ==> role_rule_result_file_col_order
  #               "api_server",
  #               "health_check_result"
  #             ]
  #          }
  #        ],  
  #        [
  #          {
  #            final_result_data: [
  #              [
  #                {
  #                   name: "",
  #                   value: ""
  #                 },
  #                 {
  #                   name: "",
  #                   value: ""
  #                 }
  #               ]
  #            ],
  #            "col": [
  #               "api_server",
  #               "health_check_result"
  #             ]
  #          }
  #        ]
  #     ]
  #

  #
  # Varible naming pattern
  #  
  # role_rule_result_file_cole_order 
  #   eg. dns_check role.
  #
  #    This parameter get following information
  #    role : dns_check 
  #      rule : dns_chekc rule
  #        result_file : 
  #          cole_order:

  for role in role_list:
    # Reset var by role based.
    final_role={}
    final_col_data=[]
    final_result_data={}
    final_result_data_list=[]
    role_rule=report_file_dict[role][0]
    role_result_file_list=report_file_dict[role][1]
  
    # Load Rule files (load one time because role is always one)
    # Role Rule Full Path
    if len(role_rule) > 0:
      role_rule_path=result_path + "/" + role_rule[0]
  
      # Convert rule json to rule dict 
      with open(role_rule_path) as rule_json:
        rule_dict = json.load(rule_json)
    else:
      module.fail_json(msg='Rule file does not exist for Role(%s)' % (role))

    for file_num in range(0,len(role_result_file_list)):
        
        layer_final_result_data_list=[]
        result_item_list=[]

        # Role Result Full Path
        role_result_path=result_path + "/" + role_result_file_list[file_num]
  
  
        ## Read result_order from rule
        role_rule_result_file_col_order=rule_dict['result_files'][str(file_num+1)]['col_order']
        role_rule_title=rule_dict['title']
        role_rule_col_list=rule_dict['col_list']
  
        role_rule_result_type={}
        if 'result_type' in rule_dict:
          role_rule_result_type=rule_dict['result_type']
  
        role_rule_report_result_combine='false'
        if 'report' in rule_dict:
          if rule_dict['report'].has_key('result_combine'):
            role_rule_report_result_combine=rule_dict['report']['result_combine']

        # Convert result txt to result dict  
        role_result_dict=[]
        with open(role_result_path) as result:
          for line in result:
            splitWord = line.split()
            newDict=[]
            for word in splitWord:
              newDict.append(word)
            role_result_dict.append(newDict)

       # To-Do combine 2 result files to 1 report if all column names are same except result_type of column. 
        #combine_result_row_count = len(role_result_dict)
        #combined_data_start_index = len(result_item)/len(role_result_dict)
        #combined_data_increase_size = combined_data_start_index + 1
  
        #print role_rule_result_file_col_order
        #print role_result_dict 
        #print role
       #print role_result_dict[0]

       ## Column count from result file have to be same as coloumn order item count from rule
        if len(role_result_dict[0]) != len(role_rule_result_file_col_order):
          module.fail_json(msg='Column counts are different between Rule-col_order(%d) and Result(%d) in Role(%s)' % (len(role_rule_result_file_col_order),len(role_result_dict[0]), role))
  
        if role_rule_report_result_combine == 'true': 
          temp_final_result_data=[]
  
  
      #ROW
      ## role_result_dict List example:
      ## [ 
      ##   [rule, [result1, result2], [raw1, raw2]],
      ##   [rule, [result1, result2], [raw1, raw2]]
      ## ] 
        for result_row_num in range(0, len(role_result_dict)):
          result_item=[]
          for result_col_num in range(0, len(role_result_dict[result_row_num])):
            for col in  role_rule_col_list:
              result_each_key_value={}
              col_value=""
              role_result = STRING_SUCCESS
              if col['name'] == role_rule_result_file_col_order[result_col_num]:
                if col['type'] == 'result':   #task_type check
                  if role_rule_result_type.has_key(role_result_dict[result_row_num][result_col_num]):
                    col_value = role_rule_result_type[role_result_dict[result_row_num][result_col_num]]
                  elif role_result_dict[result_row_num][result_col_num].lower() == STRING_SUCCESS.lower():
                    col_value = STRING_SUCCESS 
                  elif role_result_dict[result_row_num][result_col_num].lower() == STRING_FAIL.lower():
                    col_value = STRING_FAIL
                    report_result = STRING_FAIL
                    role_result = STRING_FAIL
                  elif role_result_dict[result_row_num][result_col_num].lower() == STRING_WARN.lower():
                    col_value = STRING_WARN
                  else:
                     module.fail_json(msg="The result type(%s) is not defined in the %s_rule" % (role_result_dict[result_row_num][result_col_num],role))
                elif col['type'] == 'info':
                  col_value = role_result_dict[result_row_num][result_col_num]
  
                #check col_data is duplicated
                col_non_exist=True
                for col_data in final_col_data:
                  if col_data['name'] == col['name']:
                     col_non_exist=False
                if col_non_exist:
                   final_col_data.append(col)
  
                result_each_key_value['name']= col['name']
                result_each_key_value['value']= col_value
                result_item.append(result_each_key_value)
 
              # To-do  
              # Combine 2 result files to 1 result   
              #  if role_rule_report_result_combine == 'true' and file_num != 0  and col['type'] == 'info':
              #     continue
              #  elif role_rule_report_result_combine == 'true' and file_num != 0  and col['type'] == 'result':
              #    if len(role_result_dict) ==  int(combine_result_row_count):
              #       inserted_index=int(combined_data_start_index)
              #       combine_result_row_count = combine_result_row_count - 1
              #    else:
              #       inserted_index= inserted_index + int(combined_data_increase_size) 
              #    print inserted_index
              #    temp_final_result_data.insert(inserted_index, result_each_key_value )
              #    print temp_final_result_data.insert
              #  else:
              #    result_item.append(result_each_key_value)
              #print result_item_list 
              if result_item not in result_item_list:
                result_item_list.append(result_item)                         #col layer
  
        ######## Json formatting ##########
        # assemble result json data

        final_result_data['result_data']=result_item_list                     #row layer
        final_result_data.update({'col': role_rule_result_file_col_order})    #file layer
        layer_final_result_data_list.append(dict(final_result_data))
        final_result_data_list.append(layer_final_result_data_list)
    final_role['role_name'] = role
    final_role['title'] = role_rule_title
    final_role['role_result'] = role_result
    final_role["col_data"] = list(final_col_data)
    final_role["result_data_list"]= final_result_data_list
    final_role_list.append(final_role)    
  final_json["title"]=report_title
  final_json["result"]=report_result
  final_json["role_list"]=final_role_list
  
  jsonString = json.dumps(final_json)
  
  #print jsonString
  report_name=report_path + "/report.json"
  report = open(report_name, 'w')
  report.write(jsonString)
  
  msg = "Successfully Generate Report '{msg_report_title}' into '{msg_report_path}/report.json'".format(
        msg_report_title=report_title,
        msg_report_path=report_path,
        msg_report_result=report_result)
  

  # This module will never change anything, but we might want to
  # change the return code parameter if there is some catastrophic
  # error we noticed earlier
  module.exit_json(
      msg=msg,
      report_file='report.json',
      report_path=report_path,
      result_path=result_path,
      title=report_title,
      backup=report_backup,
      rc=0,
      changed=False
  )


  # Test json
  #with open('/home/oseadmin/jooho/report-rule.json.j2') as json_data:
  #    rule_dict = json.load(json_data)
  #print rule_dict['result_type']['SUCCESS']
  #  print "%s : %d" % (role, len(role_result))

######################################################################
# It's just the way we do things in Ansible. So disable this warning
#
# pylint: disable=wrong-import-position,import-error
from ansible.module_utils.basic import AnsibleModule
if __name__ == '__main__':
  main()
