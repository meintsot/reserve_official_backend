from .models import Company, Schedule, Notification
from.serializers import NotificationSerializer


class ListingService:
    @staticmethod
    def get_listing(params):
        query = f"""
            SELECT c.id, name, city, store_type, attachment_id, stars, stars_count, has_parties, has_deals,
             minimum_reservation_price, minimum_reservation_persons, is_open FROM COMPANY c JOIN schedule s on c.id = s.company_id
            WHERE store_type = {params["storeType"]} AND date = '{params["currentDate"]}'
        """
        if "hasParties" in params:
            query += f" AND has_parties = {params['hasParties']}"
        if "hasDeals" in params:
            query += f" AND has_deals = {params['hasDeals']}"

        table = Company.objects.raw(query)
        data = []

        for row in table:
            data.append({
                'id': row.id,
                'name': row.name,
                'city': row.city,
                'stars': row.stars,
                'starsCount': row.stars_count,
                'hasParties': True if row.has_parties == 1 else False,
                'hasDeals': True if row.has_deals == 1 else False,
                'attachmentId': row.attachment_id,
                'minimumReservationPrice': row.minimum_reservation_price,
                'minimumReservationPersons': row.minimum_reservation_persons,
                'storeType': row.store_type,
                'isOpen': True if row.is_open == 1 else False
            })

        return data


class NotificationService:
    @staticmethod
    def retrieve_notifications():
        queryset = Notification.objects.order_by('-time')
        notification_serializer = NotificationSerializer(queryset, many=True)
        return notification_serializer.data
