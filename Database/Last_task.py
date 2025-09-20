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


def createStudentsData(a):
    print(a)
    res = collection.insert_many(a)
    print("students added!!!")

# createStudentsData(studentsData)



def get_all_students():
    try:
        students = collection.find()
        for student in students:
            print(f"ID: {student['_id']}")
    except Exception as e:
        print("Error while fetching students:", e)

# get_all_students()



def calculate_total_and_average():
    try:
        students = collection.find()
        for student in students:
            scores = student.get("score", [])
            if scores:
                total = sum(scores)
                average = total / len(scores)
                print(f"Name: {student['name']}")
                # print(f"Scores: {scores}")
                print(f"Total: {total}")
                print(f"Average: {average:.2f}")
                print("\n")
    except Exception as e:
        print("Error while calculating total and average:", e)

calculate_total_and_average()
