%if issues:
<table border="1" cellpadding="1" cellspacing="0">
<thead>
<tr>
    <th>Key</th> <th>Created</th> <th>Summary</th> <th>Description</th>
</tr>
</thead>
<tbody>
%for i in issues:
<tr>
    <td> <a href="${plugin_config["server"]}/browse/${i["key"]}">${i["key"]}</a> </td>
    <td> ${i["fields"]["created"].replace("T"," ")} </td>
    <td> ${i["fields"]["summary"]} </td>
    <td> ${i["fields"]["description"]} </td>
</tr>
%endfor
%endif
