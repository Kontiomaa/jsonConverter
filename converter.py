from __future__ import print_function
import csv
#use python3 (utf8 support for csv)

f=open('testdata.csv', 'r')
csvFile=csv.reader(f)

for row in csvFile:
	municipality=open(row[0]+".json", 'w')
	print("{\n\t\"kuntatiedot\":{\n\t\t\"nimi\":\""+row[0]+"\",\n\t\t\"palveluntuottaja\":\"Tuottaja tähän\",\n\t\t\"kunta\":{\n\t\t\t\"kuntaKysymys1\":{\n\t\t\t\t\"vastausEnnen\":\""+row[1]+"\",\n\t\t\t\t\"vastausJalkeen\":\""+row[2]+"\"\n\t\t\t}\n\t\t},\n\t\t\"koti\":{\n\t\t\t\"kotiKysymys1\":{\n\t\t\t\t\"vastausEnnen\":\""+row[1]+"€\",\n\t\t\t\t\"vastausJalkeen\":\""+row[2]+"€\"\n\t\t\t}\n\t\t},\n\t\t\"hoitokoti\":{\n\t\t\t\"hoitokotiKysymys1\":{\n\t\t\t\t\"vastausEnnen\":\""+row[1]+"$\",\n\t\t\t\t\"vastausJalkeen\":\""+row[2]+"$\"\n\t\t\t}\n\t\t},\n\t\t\"osasto\":{\n\t\t\t\"osastoKysymys1\":{\n\t\t\t\t\"vastausEnnen\":\""+row[1]+"£\",\n\t\t\t\t\"vastausJalkeen\":\""+row[2]+"£\"\n\t\t\t}\n\t\t}\n\t}\n}", file=municipality)
	municipality.close();
f.close();
