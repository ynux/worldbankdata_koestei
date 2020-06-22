import csv,sys
init_data={"keys":["GDP","POP_REF_ORIGIN","POP_REF_DESTIN","POP_TOT","FILE_SYSTEM"]}
print("Starting Configuration")
try:
    with open("init.txt",newline="") as file:
        csvReader=csv.reader(file,delimiter=';')
        for row in csvReader:
            if row[0] not in init_data["keys"]:
                sys.exit("Key not found: "+row[0])
            if row[0] in init_data:
                sys.exit("Key duplicate: "+row[0])
            init_data[row[0]]=row[1]
except FileNotFoundError:
    raise FileNotFound("Configuration failed: no initialisation file found")
del init_data["keys"]
if len(init_data)!=5 or len(init_data)==4 and "FILE_SYSTEM" in init_data:
    print("Initialisation file incomplete. Trying to retrieve configuration from last startup")
    try:
        with open("startup.che","r",newline="") as file:
            csvReader=csv.reader(file,delimiter=";")
            for row in csvReader:
                if row[0] not in init_data:
                    init_data[row[0]]=row[1]
    except FileNotFoundError:
        raise FileNotFoundError("Configuration failed: no prior startup")
if "FILE_SYSTEM" in init_data and init_data["FILE_SYSTEM"] not in ["ANUAL","SINGLE"]:
    print("Returns both anual and single file because of unknown parameter:",
          init_data["FILE_SYSTEM"])
    del init_data["FILE_SYSTEM"]
print("Configuration successfully completed")
data=dict()
with open("startup.che","w",newline="") as file:
    csvWriter=csv.writer(file,delimiter=";",quoting=csv.QUOTE_NONE)
    for key,value in init_data.items():
        csvWriter.writerow([key,value])
        if key!="FILE_SYSTEM":
            data[key]=[n for n in
                       csv.reader(open(value,"r",newline=""),delimiter=",",quotechar='"')][5:]
            for i in range(len(data[key])):
                for j in range(4,len(data[key][i])):
                    if data[key][i][j]=="":
                        data[key][i][j]=0
                    try:
                        data[key][i][j]=int(data[key][i][j])
                    except ValueError:
                        data[key][i][j]=float(data[key][i][j])
dataSorted=dict()
for i in range(4,len(data["GDP"][0])):
    dataSorted[1956+i]={"TOTAL":{"GDP":0,"POP_REF_ORIGIN":0,"POP_REF_DESTIN":0,"POP_TOT":0,"COLOR_CODE":0}}
    for key in ["GDP","POP_REF_ORIGIN","POP_REF_DESTIN","POP_TOT"]:
        for j in data[key]:
            if j[1] not in dataSorted[1956+i]:
                dataSorted[1956+i][j[1]]={"GDP":0,"POP_REF_ORIGIN":0,"POP_REF_DESTIN":0,"POP_TOT":0,"COLOR_CODE":0}
            dataSorted[1956+i][j[1]][key]=j[i]
            dataSorted[1956+i]["TOTAL"][key]+=j[i]
for key1,value in dataSorted.items():
    if value["TOTAL"]["GDP"]==0 or value["TOTAL"]["POP_TOT"]==0 or value["TOTAL"]["POP_REF_DESTIN"]==0:
        continue
    for key in value.keys():
        if value[key]["GDP"]==0 and value[key]["POP_TOT"]==0:
            continue
        if key=="USA":
            print(value["USA"]["GDP"],value["USA"]["POP_TOT"])
        #print(2*value[key]["GDP"]/(3*value["TOTAL"]["GDP"])+value[key]["POP_TOT"]/(3*value["TOTAL"]["POP_TOT"])*value["TOTAL"]["POP_REF_DESTIN"])
        dataSorted[key1][key]["COLOR_CODE"]=value[key]["POP_REF_DESTIN"]/((2*value[key]["GDP"]/(3*value["TOTAL"]["GDP"])+
                                                               value[key]["POP_TOT"]/(3*value["TOTAL"]["POP_TOT"]))*value["TOTAL"]["POP_REF_DESTIN"])
if "FILE_SYSTEM" not in init_data or init_data["FILE_SYSTEM"]=="ANUAL":
    for key,value in dataSorted.items():
        with open("data_"+str(key)+".csv","w",newline="") as file:
            csvWriter=csv.writer(file,delimiter=";")
            csvWriter.writerow(["Country","Color code"])
            for country,data in value.items():
                csvWriter.writerow([country,data["COLOR_CODE"]])
