contacts={"number":4,
          "students":[
              {'name':'name1','email':'email1'},
              {'name':'name2','email':'email2'},
              {'name':'name3','email':'email3'},
              {'name':'name4','email':'email4'}
          ]

}
#capture only the email ids of all students
for i in contacts["students"]:
    print(i) #this will print both name and email ids

for i in contacts["students"]:
    print(i["email"])