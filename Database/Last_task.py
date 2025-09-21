from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.errors import InvalidId

# connection

MONGO_URI = "mongodb+srv://ITS-GK03:gowtham1803@cluster0.ndzmmff.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGO_URI)
database = client["pythonClass"]
collection = database["final"]



studentsData = [
    {
        "name": "Nikhil",
        "age": 17,
        "score": [82, 79, 91, 87, 85],
        "email": "nikhil@gmail.com",
        "mobile": 9876501234
    },
    {
        "name": "Sneha",
        "age": 17,
        "score": [90, 88, 84, 92, 89],
        "email": "sneha@gmail.com",
        "mobile": 9765432109
    },
    {
        "name": "Aditya",
        "age": 17,
        "score": [78, 85, 80, 83, 77],
        "email": "aditya@gmail.com",
        "mobile": 9654321098
    },
    {
        "name": "Meera",
        "age": 17,
        "score": [88, 91, 89, 90, 92],
        "email": "meera@gmail.com",
        "mobile": 9543210987
    },
    {
        "name": "Kiran",
        "age": 17,
        "score": [75, 70, 72, 78, 74],
        "email": "kiran@gmail.com",
        "mobile": 9432109876
    },
    {
        "name": "Rhea",
        "age": 17,
        "score": [85, 87, 90, 86, 88],
        "email": "rhea@gmail.com",
        "mobile": 9321098765
    },
    {
        "name": "Vikram",
        "age": 17,
        "score": [80, 83, 85, 81, 79],
        "email": "vikram@gmail.com",
        "mobile": 9210987654
    },
    {
        "name": "Anjali",
        "age": 17,
        "score": [92, 95, 91, 94, 93],
        "email": "anjali@gmail.com",
        "mobile": 9109876543
    },
    {
        "name": "Rahul",
        "age": 17,
        "score": [77, 80, 75, 79, 76],
        "email": "rahul@gmail.com",
        "mobile": 8998765432
    },
    {
        "name": "Priya",
        "age": 17,
        "score": [89, 87, 90, 88, 91],
        "email": "priya@gmail.com",
        "mobile": 8887654321
    }
]

result = collection.delete_many({})
print(f"Deleted {result.deleted_count} documents")

def Insert_students(data):
    res = collection.insert_many(data)
    print("Students added in the Database","\n")
Insert_students(studentsData)

def get_student_rankings():
    students = collection.find()
    student_list = []
    for student in students:
        total = sum(student["score"])
        average = total / len(student["score"])
        student_list.append({
            "Name": student["name"],
            "Total": total,
            "Average": average
        })

    sorted_list = []
    while student_list:
        highest = student_list[0]
        for k in student_list:
            if k["Total"] > highest["Total"]:
                highest = k
        student_list.remove(highest)
        sorted_list.append(highest)

    for i in range(len(sorted_list)):
        sorted_list[i]["Rank"] = i + 1
    return sorted_list

ranked_students = get_student_rankings()

print("[")
for student in ranked_students:
    print("  {")
    print(f"    Name: {student['Name']}")
    print(f"    Total: {student['Total']}")
    print(f"    Average: {student['Average']:.2f}")
    print(f"    Rank: {student['Rank']}")
    print("  },")
print("]")