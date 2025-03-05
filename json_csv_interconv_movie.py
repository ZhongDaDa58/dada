import sys
import json
import csv

def csv_to_json(file):
    data=[]
    headers=["movie_id","movie_name","movie_rating","movie_author1","movie_author2",
    "movie_type","movie_language","movie_imdb","movie_date","movie_area"]
        
    with open(file,'r',encoding='utf-8') as csvfile:
        reader =csv.DictReader(csvfile,fieldnames=headers)
        next(reader)        
        
        for line in reader:
            json_dict={}
            for key,value in line.items():
                if key=="movie_author1":
                    json_dict["movie_author"]=[value]
                elif key=="movie_author2":
                    if value!="":
                        json_dict["movie_author"].append(value)
                elif key=="movie_rating":
                    json_dict[key]=float(value)
                else:
                    json_dict[key]=value
            data.append(json_dict)
    newfile=file.replace(".csv",".json")
    with open(newfile,'w',encoding='utf-8') as jsonfile:
        json_data=json.dumps(data,ensure_ascii=False,indent=4)
        jsonfile.write(json_data)
        


        
def json_to_csv(file):
    jsondata=[]
    with open(file,'r',encoding='utf-8') as jsonfile:
        data=json.load(jsonfile)
        for line in data:
            json_dict={}
            for key,value in line.items():
                if key=="movie_author":
                    json_dict["movie_author1"]=value[0]
                    if(len(value)==2):
                        json_dict["movie_author2"]=value[1]
                    else:
                        json_dict["movie_author2"]=''
                
                
                else:
                    json_dict[key]=value
            jsondata.append(json_dict)
    newfile=file.replace(".json",".csv")
    with open(newfile,"w",encoding="utf-8") as csvfile:
    
        headers=["movie_id","movie_name","movie_rating","movie_author1","movie_author2","movie_type",
        "movie_language","movie_imdb","movie_date","movie_area"]
        writer=csv.DictWriter(csvfile,fieldnames=headers)
        writer.writeheader()
        for row in jsondata:
            writer.writerow(row)
            
       
if sys.argv[1]=="-b":
        csv_file=sys.argv[2]
        csv_to_json(csv_file)
elif sys.argv[1]=="-p":
        json_file=sys.argv[2]
        json_to_csv(json_file)
    
