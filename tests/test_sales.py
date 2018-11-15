'''tests for sales'''

import json

from .basetest import BaseTestCase

class SalesTestCase(BaseTestCase):
    '''class for sales tests'''

    def test_attendant_create_sale(self):
        '''test attendant can create a sale order'''

        res_1 = self.client.post(self.p_url,
            data=json.dumps(self.new_product), headers=self.authHeaders)
        result1 = json.loads(res_1.data.decode())

        self.assertEqual(res_1.status_code, 201)
        self.assertEqual(result1['message'], 'Product created successfully')

        res_2 = self.client.get(self.p_url, headers=self.authHeaders)
        self.assertEqual(res_2.status_code, 200)
        result2 = json.loads(res_2.data.decode())
        self.assertEqual(result2['message'], "success")

        product_id = result2['products'][0]['id']

        new_sale = {"product_id": product_id, "quantity": 3}


        res_3 = self.client.post('api/v2/sales',
            data=json.dumps(new_sale), headers=self.attHeaders)
        result3 = json.loads(res_3.data.decode())

        self.assertEqual(res_3.status_code, 201)
        self.assertEqual(result3['message'], 'Sale record created successfully')

    def test_admin_get_all_sales(self):
        '''test that an admin can get all sales'''
        response = self.client.get('api/v2/sales', headers=self.authHeaders)
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data.decode())
        self.assertEqual(result['message'], 'success')

    def test_attendant_cannot_view_sales(self):
        '''test that a store attendant cannot view sales'''
        response = self.client.get('api/v2/sales', headers=self.attHeaders)
        self.assertEqual(response.status_code, 403)
        result = json.loads(response.data.decode())
        self.assertEqual(result['message'], "You don't have access to this page")

    def test_view_single_sale(self):
        '''test view single sale order'''

        res_1 = self.client.post(self.p_url,
            data=json.dumps(self.new_product), headers=self.authHeaders)

        res_2 = self.client.get(self.p_url, headers=self.authHeaders)
        self.assertEqual(res_2.status_code, 200)
        result2 = json.loads(res_2.data.decode())

        product_id = result2['products'][0]['id']

        new_sale = {"product_id": product_id, "quantity": 3}


        res_3 = self.client.post('api/v2/sales',
            data=json.dumps(new_sale), headers=self.attHeaders)
        result3 = json.loads(res_3.data.decode())

        self.assertEqual(res_3.status_code, 201)
        self.assertEqual(result3['message'], 'Sale record created successfully')

        res_4 = self.client.get('api/v2/sales', headers=self.authHeaders)
        self.assertEqual(res_4.status_code, 200)
        result4 = json.loads(res_4.data.decode())
        sale_id = int(result4['Sales'][0]['id'])

        res_5 = self.client.get('api/v2/sales/{}'.format(sale_id), headers=self.authHeaders)
        result5 = json.loads(res_5.data.decode())
        self.assertEqual(result5['message'], 'success')
        self.assertEqual(res_5.status_code, 200)


    def test_get_unavailable_single_sale(self):
        '''test fetch unavailable sale'''
        response = self.client.get('api/v2/sales/1', headers=self.authHeaders)
        result = json.loads(response.data.decode())
        self.assertEqual(response.status, '404 NOT FOUND')
        self.assertEqual(result["message"], "Sale record unavailable")

    def test_admin_cannot_create_a_sale(self):
        '''test an admin cannot make a sale'''
        new_sale = {"product_id": 1, "quantity": 30}
        res_2 = self.client.post('api/v2/sales',
            data=json.dumps(new_sale), headers=self.authHeaders)
        result = json.loads(res_2.data.decode())
        self.assertEqual(res_2.status, '403 FORBIDDEN')
        self.assertEqual(result["message"], "You don't have access to this page")