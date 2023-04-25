from api import mongo
from bson.objectid import ObjectId

class Booking:
    def __init__(self, customer, booking_date, booking_time, booking_place, service, status):
        self.customer = customer
        self.booking_date = booking_date
        self.booking_time = booking_time
        self.booking_place = booking_place
        self.service = service
        self.status = status
        data = {'customer': customer,
                'booking_date': booking_date,
                'booking_time': booking_time,
                'booking_place': booking_place,
                'service': service,
                'status': status}
        self._id = str(mongo.db.bookings.insert_one(data).inserted_id)


    @staticmethod
    def get_all():
        return list(mongo.db.bookings.find())

    @staticmethod
    def get_by_id(_id):
        booking_id = ObjectId(_id)
        return mongo.db.bookings.find_one({'_id': booking_id})

    def update(self):
        data = {'customer': self.customer,
                'booking_date': self.booking_date,
                'booking_time': self.booking_time,
                'booking_place': self.booking_place,
                'service': self.service,
                'status': self.status}
        mongo.db.bookings.update_one({'_id': ObjectId(self.booking_id)}, {'$set': data})

    def delete(self):
        mongo.db.bookings.delete_one({'_id': ObjectId(self.booking_id)})
