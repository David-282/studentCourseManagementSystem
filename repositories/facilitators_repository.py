from database import facilitators_collection


class FacilitatorsRepository:

    def __init__(self):
        self.collection = facilitators_collection


    async def find_by_id(self,facilitator_id: str):
        return await self.collection.find_one({'facilitator_id': facilitator_id})


    async def save(self,facilitator):
        return await self.collection.insert_one(facilitator)


    async def delete(self, facilitator_id: str):
        return await self.collection.delete_one({'facilitator_id': facilitator_id})

    async def find_by_email(self, email):
        return await self.collection.find_one({'email': email})