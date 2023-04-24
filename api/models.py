from api import mongo

class Booking:
    def __init__(self, data):
        self.customer_id = data.get('customer_id')
        self.booking_date = data.get('booking_date')
        self.booking_time = data.get('booking_time')
        self.booking_place = data.get('booking_place')
        self.service = data.get('service')
        self.status = data.get('status')
        self.booking_id = str(mongo.db.bookings.insert_one(data).inserted_id)

    @staticmethod
    def get_all():
        return list(mongo.db.bookings.find())

    @staticmethod
    def get_by_id(booking_id):
        return mongo.db.bookings.find_one({'booking_id': booking_id})
