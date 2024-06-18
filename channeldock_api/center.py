from constants.center_constants import Constants
import requests
import json


class ChannelDockAPI:

    def __init__(self):
        self.headers = Constants.HEADERS

    @staticmethod
    def save_json(path, json_obj):
        with open(path, 'w') as f:
            f.write(json.dumps(json_obj, indent=4))

    def check_credentials(self):
        """
        Check if the credentials are correct
        :return:
        """
        return requests.get(Constants.HOME_URL, headers=self.headers)

    def get_product(self, page=1, **kwargs):
        """
        Get products from ChannelDock API
        :param page: page number - mandatory
        :param kwargs: id, ean, sku, tittle, supplier_id, sort_attr, sort_dir, include_stock_location_data
        id: the product id
        seller_id: the seller id
        center_product_status: the center product status
        ean: the product ean
        sku: the product sku
        product_reference: the product reference
        location: free input - location of the product
        supplier_id: the supplier id
        sort_attr: the attribute to sort by (updated_at, id)
        sort_dir: the direction to sort by (ASC, DESC)
        include_stock_location_data: include stock location data (true or false)

        :return:
        """

        url = f'{Constants.PRODUCTS_URL}?page={page}'
        for key, value in kwargs.items():
            url = f'{url}&{key}={value}'
        return requests.get(url, headers=self.headers)

    def get_all_products(self, **kwargs):
        """
        Get all products from ChannelDock API
        :param kwargs: id, ean, sku, tittle, supplier_id, sort_attr, sort_dir, include_stock_location_data
        id: the product id
        ean: the product ean
        sku: the product sku
        title: the product title
        supplier_id: the supplier id
        sort_attr: the attribute to sort by (updated_at, id)
        sort_dir: the direction to sort by (ASC, DESC)
        include_stock_location_data: include stock location data (true or false)
        :return:
        :return:
        """
        page = 0
        products = []
        while True:
            page += 1
            response = self.get_product(page, **kwargs)
            if response.status_code == 200:
                response = response.json()
                if response['response'] == 'success' and len(response['products']) > 0:
                    products.extend(response['products'])
                else:
                    break
            else:
                break
        return products

    def update_product(self, data):
        """
        For more details on the data format, check the official documentation
        Post product to ChannelDock API
        :param data: product data
        :return:
        """

        url = Constants.PRODUCTS_URL
        data = json.dumps(data, indent=4)
        return requests.post(url, headers=self.headers, data=data)

    def update_stock_amount_bulk(self, data):
        """
        For more details on the data format, check the official documentation
        Post product to ChannelDock API
        :param data: product data
        :return:
        """

        url = Constants.PRODUCTS_STOCK_UPDATE_URL
        data = json.dumps(data, indent=4)
        return requests.post(url, headers=self.headers, data=data)

    def get_orders(self, page=1, **kwargs):
        """
        Get orders from ChannelDock API
        :param page: page number - mandatory
        :param kwargs: id, seller_id, order_status, order_id, shipping_country_code, sort_attr, sort_dir, start_date,
                        end_date, include_raw_order_data
        id: the order id in the system
        seller_id: the seller id
        order_status: the order status
        order_id: the order id
        shipping_country_code: the shipping country code
        sort_attr: the attribute to sort by (updated_at, default: order_date, sync_date, updated_at)
        sort_dir: the direction to sort by (ASC, DESC)
        shipping_address_accurate: the shipping address accurate (default:1, 0, 'ALL')
        start_date: the start date
        end_date: the end date
        include_raw_order_data: include raw order data (true or false)
        :return:
        """

        url = f'{Constants.ORDERS_URL}?page={page}'
        for key, value in kwargs.items():
            url = f'{url}&{key}={value}'
        return requests.get(url, headers=self.headers)

    def get_all_orders(self, **kwargs):
        """
        Get all orders from ChannelDock API
        :param kwargs: order_status, order_id, shipping_country_code, sort_attr, sort_dir, start_date, end_date, id,
                        include_raw_order_data
        order_status: the order status
        order_id: the order id
        shipping_country_code: the shipping country code
        sort_attr: the attribute to sort by (updated_at, default: order_date, sync_date, updated_at)
        sort_dir: the direction to sort by (ASC, DESC)
        start_date: the start date
        end_date: the end date
        id: the order id
        include_raw_order_data: include raw order data (true or false)
        :return:
        """

        page = 0
        orders = []
        while True:
            page += 1
            response = self.get_orders(page, **kwargs)
            if response.status_code == 200:
                response = response.json()
                if len(response['orders']) > 0 and response['response'] == 'success':
                    orders.extend(response['orders'])
                else:
                    break
            else:
                break
        return orders

    def create_order(self, data):
        """
        For more details on the data format, check the official documentation
        Post order to ChannelDock API
        :param data: order data
        :return:
        """

        url = Constants.ORDERS_URL
        data = json.dumps(data, indent=4)
        return requests.post(url, headers=self.headers, data=data)

    def create_stock_location(self, data):
        """
        For more details on the data format, check the official documentation
        Post stock location to ChannelDock API
        :param data: stock location data
        :return:
        """

        url = Constants.CREATE_STOCK_LOCATION_URL
        data = json.dumps(data, indent=4)
        return requests.post(url, headers=self.headers, data=data)

    def update_stock_location(self, data):
        """
        For more details on the data format, check the official documentation
        Update stock location to ChannelDock API
        :param data: stock location data
        :return:
        """

        url = Constants.CREATE_STOCK_LOCATION_URL
        data = json.dumps(data, indent=4)
        return requests.put(url, headers=self.headers, data=data)

    def delete_stock_location(self, data):
        """
        For more details on the data format, check the official documentation
        Delete stock location to ChannelDock API
        :param data: stock location data
        :return:
        """

        url = Constants.CREATE_STOCK_LOCATION_URL
        data = json.dumps(data, indent=4)
        return requests.delete(url, headers=self.headers, data=data)

    def get_shipments(self, page=1, **kwargs):
        """
        Get shipments from ChannelDock API
        :param page: page number - mandatory
        :param kwargs: id, seller_id, status, order_id, sort_attr, sort_dir, start_date, end_date, include_pdf_label
        id: the shipment id in the system
        seller_id: the seller id
        status: the shipment status (registered, distribution, delivered, return)
        order_id: the order id
        sort_attr: the attribute to sort by (updated_at, default: created_at, updated_at)
        sort_dir: the direction to sort by (ASC, DESC)
        start_date: the start date
        end_date: the end date
        include_pdf_label: include pdf label (true or false)
        :return:
        """

        url = f'{Constants.SHIPMENTS_URL}?page={page}'
        for key, value in kwargs.items():
            url = f'{url}&{key}={value}'
        return requests.get(url, headers=self.headers)

    def get_all_shipments(self, **kwargs):
        """
        Get all shipments from ChannelDock API
        :param kwargs: id, seller_id, status, order_id, sort_attr, sort_dir, start_date, end_date, include_pdf_label
        id: the shipment id in the system
        seller_id: the seller id
        status: the shipment status (registered, distribution, delivered, return)
        order_id: the order id
        sort_attr: the attribute to sort by (updated_at, default: created_at, updated_at)
        sort_dir: the direction to sort by (ASC, DESC)
        start_date: the start date
        end_date: the end date
        include_pdf_label: include pdf label (true or false)
        :return:
        """

        page = 0
        shipments = []
        while True:
            page += 1
            response = self.get_shipments(page, **kwargs)
            if response.status_code == 200:
                response = response.json()
                if len(response['shipments']) > 0 and response['response'] == 'success':
                    shipments.extend(response['shipments'])
                else:
                    break
            else:
                break
        return shipments


