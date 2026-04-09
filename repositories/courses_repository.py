from database import courses_collection


class CoursesRepository:
    def __init__(self):
        self.collection = courses_collection

    async def find_by_course_code(self, course_code: str):
        return await self.collection.find_one({'course_code': course_code})

    async def find_by_facilitator_id(self, facilitator_id: str):
        courses = await self.collection.find({"facilitator_id": facilitator_id}).to_list(length=None)
        return {
            "courses":[course["course_code"] for course in courses]
        }

    async def save(self, course):
        saved_course = await self.collection.insert_one(course)

        course["_id"] = str(saved_course.inserted_id)

        return course

    async def update_course(self, course_code,course:dict):
        return await self.collection.update_one(
            {"course_code": course_code},
            {"$set": course}

        )

    async def delete(self, course_code: str):
        return await self.collection.delete_one({'course_code': course_code})