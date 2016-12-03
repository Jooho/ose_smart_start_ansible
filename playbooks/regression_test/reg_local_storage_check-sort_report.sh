
#!/usr/bin/bash
result_filename="/tmp/reg_local_storage_check"
raw_filename="/tmp/aoappd-e-mgt001.ctho.asbn.gtwy.dcn//tmp/reg_local_storage_check-raw"
sort_filename="/tmp/aoappd-e-mgt001.ctho.asbn.gtwy.dcn//tmp/reg_local_storage_check_sort"
cat ${raw_filename} | sort --key 5 -g -r > ${sort_filename}
while read -r line
do
    percentage=$(echo $line|awk '{print $5}'|tr -d "%")
    percentage=$(( $percentage + 0 ))
echo $percentage
    if [ $percentage -eq 100  ]
    then
      echo $line |awk '{print $6 " FAIL:" $5}' >> ${result_filename}
    elif [ $percentage -l 100 ] && [ $percentage -gt 80 ] 
    then
      echo $line |awk '{print $6 " WARN:" $5}'  >> ${result_filename}
    elif [ $percentage -l 80 ] && [ $percentage -gt 70 ] 
    then
      echo $line |awk '{print $6 " INFO:" $5}'  >> ${result_filename}
    fi
done < $sort_filename

