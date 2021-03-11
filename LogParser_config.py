

#key_list=["DAIW","STCA","MSAW"]
#DAIW_range={"Date":line[0:8],"Time":line[8:18],"IdNo":line[18:22],"Status":line[22:31],"Action":line[31:36],"Time2":line[36:45],"CharCode1":line[45:53],"ACode":line[53:59],"PCode":line[59:66],"charCode2":line[66:74],
#"DynamicValues":line[74:-1].split(" ")}
#STCA_range={"Date":line[0:8],"Time":line[8:18],"IdNo":line[18:22],"Status":line[22:31],"Action":line[31:36],"Time2":line[36:45],"CharCode1":line[45:53],"ACode":line[53:59],"PCode":line[59:66],"charCode2":line[66:74],
#"ACode2":line[74:80],"PCode2":line[80:86],"DynamicValues":line[86:-1].split(" ")}
#MSAW_range={"Date":line[0:8],"Time":line[8:18],"IdNo":line[18:22],"Status":line[22:31],"Action":line[31:36],"Time2":line[36:45],"CharCode1":line[45:53],"ACode":line[53:59],"PCode":line[59:66],
#"DynamicValues":line[66:-1].split(" ")}
#DAIW={"Date":DAIW_range["Date"],"Time":DAIW_range["Time"],"IdNo":DAIW_range["IdNo"],"Status":DAIW_range["Status"],"Action":DAIW_range["Action"],"Time2":DAIW_range["Time2"],"CharCode1":DAIW_range["CharCode1"],"ACode":DAIW_range["ACode"],"PCode":DAIW_range["PCode"],"charCode2":DAIW_range["charCode2"],
#"DynamicValues":DAIW_range["DynamicValues"]}
#STCA={"Date":STCA_range["Date"],"Time":STCA_range["Time"],"IdNo":STCA_range["IdNo"],"Status":STCA_range["Status"],"Action":STCA_range["Action"],"Time2":STCA_range["Time2"],"CharCode1":STCA_range["CharCode1"],"ACode":STCA_range["ACode"],"PCode":STCA_range["PCode"],"charCode2":STCA_range["charCode2"],"ACode2":STCA_range["ACode2"],"PCode2":STCA_range["PCode2"],
#"DynamicValues":STCA_range["DynamicValues"]}
#MSAW={"Date":MSAW_range["Date"],"Time":MSAW_range["Time"],"IdNo":MSAW_range["IdNo"],"Status":MSAW_range["Status"],"Action":MSAW_range["Action"],"Time2": MSAW_range["Time2"],"CharCode1":MSAW_range["CharCode1"],"ACode":MSAW_range["ACode"],"PCode":MSAW_range["PCode"],
#"DynamicValues":MSAW_range["DynamicValues"]}

keys_ranges={"DAIW":{"Date":[0,8],"Time":[8,18],"IdNo":[18,22],"Status":[22,31],"Action":[31,36],"Time2":[36,45],"CharCode1":[45,53],"ACode":[53,59],"PCode":[59,66],"charCode2":[66,74],
"DynamicValues":[74,-1]},"STCA":{"Date":[0,8],"Time":[8,18],"IdNo":[18,22],"Status":[22,31],"Action":[31,36],"Time2":[36,45],"CharCode1":[45,53],"ACode":[53,59],"PCode":[59,66],"charCode2":[66,74],
"ACode2":[74,80],"PCode2":[80,86],"DynamicValues":[86,-1]},"MSAW":{"Date":[0,8],"Time":[8,18],"IdNo":[18,22],"Status":[22,31],"Action":[31,36],"Time2":[36,45],"CharCode1":[45,53],"ACode":[53,59],"PCode":[59,66],
"DynamicValues":[66,-1]}}
             




