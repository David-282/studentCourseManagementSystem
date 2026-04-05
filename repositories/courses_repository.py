from database import courses_collection


class CoursesRepository:
    def __init__(self):
        self.collection = courses_collection

    async def find_by_course_code(self, course_code: str):
        return await self.collection.find_one({'course_code': course_code})

    async def find_by_facilitator_id(self, facilitator_id: str):
        return await self.collection.find({"facilitator_id": facilitator_id}).to_list(length=None)

    async def save(self, course):
        saved_course = await self.collection.insert_one(course)

        course["_id"] = str(saved_course.inserted_id)

        return course


    async def delete(self, course_code: str):
        return await self.collection.delete_one({'course_code': course_code})