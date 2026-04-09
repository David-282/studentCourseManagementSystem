from motor.motor_asyncio import AsyncIOMotorClient


client = AsyncIOMotorClient("mongodb://localhost:27017")


db = client["school_management_database"]


students_collection = db["students"]
courses_collection = db["courses"]
facilitators_collection = db["facilitators"]
enrollments_collection = db["enrollments"]

