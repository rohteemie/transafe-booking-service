from flask_restful import Resource, reqparse
from api.models import Booking

parser = reqparse.RequestParser()
parser.add_argument('customer_id', type=str, required=True)
parser.add_argument('booking_date', type=str, required=True)
parser.add_argument('booking_time', type=str, required=True)
parser.add_argument('booking_place', type=str, required=True)
parser.add_argument('service', type=str, required=True)
parser.add_argument('status', type=str, required=True)

class BookingList(Resource):
    def get(self):
        all_booking = Booking.get_all()

        results = []
        for booking in all_booking:
            booking['_id'] = str(booking['_id'])
            results.append(booking)
        return results

class BookingDetail(Resource):
    def get(self, booking_id):
        return Booking.get_by_id(booking_id)

class BookingCreate(Resource):
    def post(self):
        args = parser.parse_args()
        booking = Booking(args)
        return {'booking_id': booking.booking_id}

