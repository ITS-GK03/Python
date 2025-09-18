from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.errors import InvalidId

# connection

MONGO_URI = "mongodb+srv://ITS-GK03:gowtham1803@cluster0.ndzmmff.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGO_URI)
database = client["pythonClass"]
collection = database["user"]

userData = {
    "name":"vetri",
    "age":10,
    "skill":"python",
    "email":"vetri@gmail.com",
    "mobile":8365378534
    }

usersData = [
    {
    "name":"dhilip",
    "age":12,
    "skill":"python,mongo",
    "email":"dhilip@gmail.com",
    "mobile":8365378534
    },
      {
    "name":"Gowtham",
    "age":13,
    "skill":"python,mongo",
    "email":"gowtham@gmail.com",
    "mobile":8365378534
    },
]
def createUser(user):
    res = collection.insert_one(user)
    print("user data created: " , res.inserted_id)


# createUser(userData)


def createStudentsData(a):
    print(a)
    res = collection.insert_many(a)
    print("students added!!!")


# createStudentsData(usersData)

def getAllStudents():
    res = collection.find({})
    for i in res:
        print(i)

# getAllStudents()


def getSpecificStudent(id):
    print(type(id))
    res = collection.find_one({"_id":ObjectId(id)})
    print(res)

# getSpecificStudent("68c81951c274b7b3c342d5d6")



# TASK:


single_user = {
    "name": "Sree Jeshva",
    "age": 17,
    "skill": "Defence",
    "email": "sree@gmail.com",
    "mobile": 8365378534
}

def adding_student(student_id):
    try:
        if single_user["name"] == student_id["name"]:
            print("Name is found:", single_user["name"])
        else:
            print("Name is not found")
        result = collection.insert_one(student_id)
        print("Student inserted +id:", result.inserted_id)

    except Exception as e:
        print("Error inserting student:", str(e))
# adding_student(single_user)





students = [
    {
        "name": "Gowtham",
        "age": 13,
        "skill": "python,mongo",
        "email": "gowtham@gmail.com",
        "mobile": 8365378534,
        "id": 101
    },
    {
        "name": "Dhilip",
        "age": 14,
        "skill": "java,c++",
        "email": "dhilip@gmail.com",
        "mobile": 9876543210,
        "id": 102
    },
    {
        "name": "Gokul",
        "age": 15,
        "skill": "c,java",
        "email": "gokul@gmail.com",
        "mobile": 8899776655,
        "id": 105
    },
   
]
def add_selected_students(student_list, names_insert):
    try:
        selected = [s for s in student_list if s["name"] in names_insert]

        if not selected:
            print("Student not found")
            return
        result = collection.insert_many(selected)
        for student, inserted_id in zip(selected, result.inserted_ids):
            print(f"Inserted: {student['name']} (id: {inserted_id})")

    except Exception as e:
        print("Error inserting students:", str(e))
# add_selected_students(students,["Gowtham","Gokul"])

def deleteStudent(id):
    try:
        obj_id = ObjectId(id)

        checkUser = collection.find_one({"_id": obj_id})
        if not checkUser:
            print("User not found")
        else:
            print("User found:", checkUser)

            deleteUser = collection.delete_one({"_id": obj_id})
            if deleteUser.deleted_count > 0:
                print("User deleted successfully")
            else:
                print("Failed to delete user")
    except InvalidId:
        print("Invalid ObjectId")
    except Exception as e:
        print("Database error:", str(e))
# deleteStudent("68cabc4a87647b8372b839a4")




# UPDATE:


update_info={
    "name":"Vetrichelvan",
    "age":17,
    "mobile":1234567890
}

def update_student(id,new_id):
    res=collection.find_one({"_id":ObjectId(id)})
    new_res=collection.update_one({"_id":ObjectId(id)},{"$set":new_id})
    print("Change has been updated:", new_res)

# update_student("68cabdd9ea4fd38c872be9ea", update_info)




# SORT:


def sortData():
    data = collection.find().sort("name",1)
    for i in data:
        print(i)
# sortData()




# QUARY:


def quaryData():
    quary={"age":{"$gt":7}}
    data = collection.find(quary).sort("age", 1)
    for i in data:
        print(i)
# quaryData()



def quaryData():
    quary={"age":{"$lt":15}}
    data = collection.find(quary).sort("age", 1)
    for i in data:
        print(i)
# quaryData()



def quaryData():
    quary={"age":{"$gte":14}}
    data = collection.find(quary).sort("age", -1)
    for i in data:
        print(i)
# quaryData()



def quaryData():
    quary={"age":{"$lte":15}}
    data = collection.find(quary).sort("age", -1)
    for i in data:
        print(i)
# quaryData()


def quaryData():
    quary={"age":17}
    data = collection.find(quary).sort("age", 1)
    for i in data:
        print(i)
# quaryData()



def quaryData():
    quary={"age":{"$ne":15}}
    data = collection.find(quary).sort("age", -1)
    for i in data:
        print(i)
quaryData()