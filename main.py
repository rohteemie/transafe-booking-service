from api import app
from flask_restful import Api
from api.controllers import BookingList, BookingDetail, BookingCreate

api_route = Api(app)

api_route.add_resource(BookingList, '/bookings')
api_route.add_resource(BookingDetail, '/bookings/<_id>')
api_route.add_resource(BookingCreate, '/bookings/new')

if __name__ == '__main__':
    app.run(debug=True)
