%for i in issues:
${i["key"]} - ${i["fields"]["created"].replace("T"," ")} - ${i["fields"]["summary"]} - ${i["fields"]["description"]}
%endfor
