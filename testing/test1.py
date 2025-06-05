name = "ujwal"
age = 29 # int
gpa = 5.0

interests = ["book reading", "coding", "sleeping"]

personal_info = {
   "name": "ujwal",
   "weight": 75,
   "mobile": "9757083770",
   "dob": "18/04/1996",
   "city": "Mumbai",
   "state": "Maharashtra"
}

'''
personal_info_list = [{
   "name": "ujwal",
   "weight": 75,
   "mobile": "9757083770",
   "dob": "18/04/1996",
   "city": "Mumbai",
   "state": "Maharashtra"
},{
   "name": "saudagar",
   "weight": 73,
   "mobile": "9757083770",
   "dob": "18/04/1996",
   "city": "Mumbai",
   "state": "Maharashtra"
}]

add unique id for each person in the dict
'''

employees = [
{
   "name": "ujwal",
   "weight": 75,
   "mobile": "9757083770",
   "dob": "18/04/1996",
   "city": "Mumbai",
   "state": "Maharashtra"
},{
   "name": "Saudagar",
   "weight": 73,
   "mobile": "9757083770",
   "dob": "18/04/1996",
   "city": "Mumbai",
   "state": "Maharashtra"
}
]

for personal_i in employees:
   print(personal_i["name"])
   print(personal_i["weight"])
   personal_i["uid"] = "abc"

ujwals_age = personal_info["dob"]

current_date = "20/11/2024"

current_year = int(current_date.split("/")[-1]) # type conversion

ujwals_year = int(ujwals_age.split("/")[-1])
normal_weight = 80

if current_year - ujwals_year >= 21 and personal_info["weight"] > normal_weight: 
   # if personal_info["weight"] > normal_weight:
      # print("join gym")
   print("yes")
elif current_year - ujwals_year <= 5:
   print("enjoy childhood")
else:
   print("no")	


