
from database import students_collection


class StudentRepository:

    def __init__(self):
        self.collection = students_collection

    async def find_by_id(self,student_id:str):
        return await self.collection.find_one({'student_id': student_id})


    async def save(self,student):
        return await self.collection.insert_one(student)

    async def delete(self, student_id: str):
        return await self.collection.delete_one({'student_id': student_id})

    async def update_student (self,student_id,student:dict):
        return await self.collection.update_one(
            {"student_id": student_id},
            {"$set":student}

        )

    async def find_by_email(self, email:str):
        return await self.collection.find_one({'email': email})


