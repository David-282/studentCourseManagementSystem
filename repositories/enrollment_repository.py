from pydantic import BaseModel

from database import enrollments_collection


class EnrollmentRepository:
    def __init__(self):
        self.collection = enrollments_collection

    async def find_by_id(self, enrollment_id: str):
        return await self.collection.find_one({'enrollment_id': enrollment_id})

    async def save(self, enrollment):
        return await self.collection.insert_one(enrollment)

    async def delete(self, enrollment_id: str):
        return await self.collection.delete_one({'enrollment_id': enrollment_id})

    async def find_by_course_id_and_student_id(self, course_id: str,student_id:str):

        return await self.collection.find_one({"course_id": course_id, "student_id": student_id})

    async def update(self,_id:str, course_grade:str):
        return await self.collection.update_one(
            {"_id": _id},
            {"$set":{"course_grade":course_grade}},

        )

    async def find_by_student_id(self, student_id):
        return await self.collection.find({'student_id': student_id}).to_list(length=None)

    async def find_by_course_code(self, course_code):
        return await self.collection.find({'course_code': course_code}).to_list(length=None)
