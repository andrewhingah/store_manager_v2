'''tests for all products'''

import json

from .basetest import BaseTestCase

class ProductTestCase(BaseTestCase):
    '''Class for all tests for products'''
    def test_admin_create_new_product(self):
        '''test admin can create a new product'''

        response = self.client.post(self.p_url,
            data=json.dumps(self.new_product), headers=self.authHeaders)
        result = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 201)
        self.assertEqual(result['message'], 'Product created successfully')

    def test_admin_get_all_products(self):
        '''test admin can get all available products'''
        response = self.client.get(self.p_url, headers=self.authHeaders)
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data.decode())
        self.assertEqual(result['message'], "success")

    def test_attendant_get_all_products(self):
        '''test a store attendant can get all available products'''
        response = self.client.get(self.p_url, headers=self.attHeaders)
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data.decode())
        self.assertEqual(result['message'], "success")

    def test_create_prduct_with_invalid_data(self):
        '''test admin can not create new product with invalid data'''
        response = self.client.post(self.p_url,
            data=json.dumps(self.invalid_prod), headers=self.authHeaders)
        result = json.loads(response.data.decode())

        self.assertEqual(response.status_code, 400)
        self.assertEqual(result['message']['name'], 'Name must be provided')


    def test_attendant_cannot_create_new_product(self):
        '''test a normal attendant cannot create a new product'''
        response = self.client.post(self.p_url,
            data=json.dumps(self.new_product), headers=self.attHeaders)
        result = json.loads(response.data.decode())
        self.assertEqual(response.status, '403 FORBIDDEN')
        self.assertEqual(result["message"], "You don't have access to this page")

    def test_admin_delete_product(self):
        '''test admin can delete a product'''
        response = self.client.post(self.p_url,
            data=json.dumps(self.new_product), headers=self.authHeaders)
        result = json.loads(response.data.decode())

        response2 = self.client.delete('api/v2/products/1', headers=self.authHeaders)
        self.assertEqual(response2.status_code, 200)

    def test_attendant_cannot_delete_product(self):
        '''test a store attendant cannot delete a product'''
        response = self.client.post(self.p_url,
            data=json.dumps(self.new_product), headers=self.authHeaders)
        result = json.loads(response.data.decode())

        response2 = self.client.delete('api/v2/products/1', headers=self.attHeaders)
        self.assertEqual(response2.status_code, 403)

    def test_admin_edit_product(self):
        '''test admin can update a product details'''
        response = self.client.post(self.p_url,
            data=json.dumps(self.new_product), headers=self.authHeaders)
        result = json.loads(response.data.decode())

        response2 = self.client.put('api/v2/products/1', data=json.dumps(self.edit_product),
            headers=self.authHeaders)
        self.assertEqual(response2.status_code, 201)

    def test_attendant_cannot_edit_product(self):
        '''test attendant cannot update a product details'''
        response = self.client.post(self.p_url,
            data=json.dumps(self.new_product), headers=self.authHeaders)
        result = json.loads(response.data.decode())

        response2 = self.client.put('api/v2/products/1', data=json.dumps(self.edit_product),
            headers=self.attHeaders)
        self.assertEqual(response2.status_code, 403)