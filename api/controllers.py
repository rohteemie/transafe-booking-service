from flask_restful import Resource, reqparse
from api.models import Booking
from api.utils import get_customer_data

parser = reqparse.RequestParser()
parser.add_argument('customer_info', type=dict, required=True, help='Customer information must be a dictionary')
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


class BookingCreate(Resource):
    def post(self):
        args = parser.parse_args()
        customer_info = args.get('customer_info')
        customer_id = customer_info.get('id')
        customer_data = get_customer_data(customer_id)
        if customer_data:
            booking = Booking(customer=customer_data, # Pass customer_data as dictionary
                              booking_date=args.get('booking_date'),
                              booking_time=args.get('booking_time'),
                              booking_place=args.get('booking_place'),
                              service=args.get('service'),
                              status=args.get('status'))
            return {'booking_id': booking.booking_id}
        else:
            return {'error': 'Failed to fetch customer data'}, 400


class BookingDetail(Resource):
    def get(self, _id):
        booking = Booking.get_by_id(_id)
        if booking:
            booking['_id'] = str(booking['_id'])
            return booking
        else:
            return {'error': 'Booking not found'}, 404

    def put(self, _id):
        booking = Booking.get_by_id(_id)
        if booking:
            args = parser.parse_args()
            customer_info = args.get('customer_info')
            customer_id = customer_info.get('id')
            customer_data = get_customer_data(customer_id)
            if customer_data:
                booking.customer = customer_data
                booking.booking_date = args.get('booking_date')
                booking.booking_time = args.get('booking_time')
                booking.booking_place = args.get('booking_place')
                booking.service = args.get('service')
                booking.status = args.get('status')
                booking.save()
                return {'message': 'Booking updated successfully'}
            else:
                return {'error': 'Failed to fetch customer data'}, 400
        else:
            return {'error': 'Booking not found'}, 404

    def delete(self, _id):
        booking = Booking.get_by_id(_id)
        if booking:
            booking.delete()
            return {'message': 'Booking deleted successfully'}
        else:
            return {'error': 'Booking not found'}, 404
