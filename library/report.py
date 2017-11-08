import os, sys,re
import json

STRING_SUCCESS="SUCCESS"
STRING_FAIL="FAIL"
STRING_WARN="WARN"

report_title="Regression Test Report"
report_result=STRING_SUCCESS
role_result=STRING_SUCCESS

final_json={}
final_role={}
final_role_list=[]
final_col_data=[]
result_item=[]
result_item_list=[]
#final_result_data=[]

# Open a file
path = '/tmp/pnp'
dirs = os.listdir( path )

role_name=""
final_json = {}
report_file_dict = {} 
role_list = []
role_rule_file_list = [] 
role_result_file_list = []
role_raw_file_list = []
raw_file_list = []
# This would print all the files and directories
for file in dirs:
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

  for file in dirs:
    if re.match(role+'_rule',file) != None:
      role_rule_file_list.append(file)

    if re.match(role+'_result',file) != None and re.match('(.*)temp(.*)',file) == None:
      role_result_file_list.append(file)
         
    if re.match(role+'_raw',file) != None and  re.match('(.*)lock$',file) == None:
      role_raw_file_list.append(file)
  report_file_dict[role]=[list(role_rule_file_list), list(role_result_file_list), list(role_raw_file_list)]
#debug
#print report_file_dict



# Important variable
# role_rule_result_order :
# role_rule_result_type :
# role_rule_task_list :
# role_result_dict
for role in role_list:
  final_role={}
  final_col_data=[]
  final_result_data={}
  final_result_data_list=[]
  role_rule=report_file_dict[role][0]
  role_result_file_list=report_file_dict[role][1]

  # Load Rule files (load one time because role is always one)
  # Role Rule Full Path
  if len(role_rule) > 0:
    role_rule_path=path + "/" + role_rule[0]

    # Convert rule json to rule dict 
    with open(role_rule_path) as rule_json:
      rule_dict = json.load(rule_json)
  else:
 #   continue
    print "Role rule does not exist"
    sys.exit(1)
  for file_num in range(0,len(role_result_file_list)):
      
      layer_final_result_data_list=[]
      result_item_list=[]
      # Role Result Full Path
      role_result_path=path + "/" + role_result_file_list[file_num]

      # debug
      #print role_rule_path

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
     
      #combine_result_row_count = len(role_result_dict)
      #combined_data_start_index = len(result_item)/len(role_result_dict)
      #combined_data_increase_size = combined_data_start_index + 1

     #print role_rule_result_file_col_order
     #print role_result_dict 
     
     ## Column count from result file have to be same as coloumn order item count from rule
      if len(role_result_dict[0]) != len(role_rule_result_file_col_order):
        print "role(%s) rule colmn count(%d) is different from real result count(%d)" % (role,   len(role_rule_result_file_col_order), len(role_result_dict[0]))
        sys.exit(1)

      if role_rule_report_result_combine == 'true': 
        temp_final_result_data=[]


    ##ROW
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
                   print "The result type(%s) is not defined in the rule" % (role_result_dict[result_row_num][result_col_num])
                   sys.exit(1)
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
              result_item_list.append(result_item)               #col layer

      final_result_data['result_data']=result_item_list         #row layer

      final_result_data.update({'col': role_rule_result_file_col_order})    #file layer
      layer_final_result_data_list.append(dict(final_result_data))
      final_result_data_list.append(layer_final_result_data_list)
  final_role['role_name'] = role
  final_role['title'] = role_rule_title
  final_role['role_result'] = role_result
  final_role["col_data"] = list(final_col_data)
  final_role["result_data_list"]= final_result_data_list
  final_role_list.append(final_role)    



######## Json formatting ##########

final_json["title"]=report_title
final_json["result"]=report_result
final_json["role_list"]=final_role_list

jsonString = json.dumps(final_json)

print jsonString

# Test json
#with open('/home/oseadmin/jooho/report-rule.json.j2') as json_data:
#    rule_dict = json.load(json_data)
#print rule_dict['result_type']['SUCCESS']
#  print "%s : %d" % (role, len(role_result))
