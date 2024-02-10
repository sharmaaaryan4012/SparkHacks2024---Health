"""
Project: Super Health App
Creators: Aaryan Sharma, Ayush Bhardwaj
SparkHacks-2024 (University of Illinois at Chicago)
"""

print("Welcome to prescription column!")

pres_name = input("Kindly enter prescription name \n").upper()
num_Meds = input("Kindly enter the number of meds prescribed \n").upper()
meds_name = []
meds_dur = []
meds_empty = []
meds_time = []
meal_time = []

for i in range(int(num_Meds)):
    meds_name.append(input("Kindly enter the name of medicine: ").upper())
    meds_dur.append(input("Kindly enter the Duration of Doses (In Days) for the Medicine: ").upper())
    meds_empty.append(input("Kindly enter whether the medicine is to be taken on an empty or full stomach (Enter E or F):\n").upper())
    meds_time.append(input("Kindly enter the time of the medicine\n Enter M for morning \n Enter A for afternoon \n Enter E for evening \n Enter N for Night\ne.g. me").upper())

for i in range(3):
    meal_time.append(input("Kindly enter the time of your meal (enter 3:00am as 3 and 3:00pm as 15): ").upper())




