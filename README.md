# transafe-booking-service


Below is the response when the api is queried

```
{
  "bookings": [
    {
      "booking_id": "123456789",
      "booking_date": "2023-04-13",
      "booking_time": "14:00",
      "booking_place": "online",
      "service": "Train",
      "customer": {
        "name": "John Doe",
        "email": "johndoe@example.com",
        "phone": "123-456-7890"
      },
      "status": "confirmed",
      "options": {
        "class": "first class",
        "seat": "5",
        "payment_method": "credit_card"
      },
      "departure": {
        "location_id": "987654321",
        "location_name": "Lekki Phase 1",
        "station name": "Transafe lekki",
        "availability": "available",
        "departure_time": "14:20"
      },
      "destination": {
        "stop_location": "Lekki Phase 1",
        "availability": "available"
      }
    },
    {
      "booking_id": "987654321",
      "booking_date": "2023-04-14",
      "booking_time": "10:30",
      "booking_place": "counter",
      "service": "Train",
      "customer": {
        "name": "Jane Smith",
        "email": "janesmith@example.com",
        "phone": "987-654-3210"
      },
      "status": "pending",
      "options": {
        "class": "economy class",
        "seat": "3",
        "payment_method": "cash"
      },
      "departure": {
        "location_id": "987654321",
        "location_name": "Lekki Phase 1",
        "station name": "Transafe lekki",
        "availability": "available",
        "departure_time": "14:20"
      },
      "destination": {
        "stop_location": "Agege",
        "availability": "available"
      }
    }
  ]
}
```
