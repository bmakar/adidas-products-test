import requests
import parse
from behave import register_type, given, when, then, step


@parse.with_pattern(r"\d+")
def parse_number(text):
    return int(text)


# -- REGISTER TYPE-CONVERTER: With behave
register_type(Number=parse_number)


@given('{amount:Number} products created')
def step_impl(context, amount):
    for i in range(amount):
        body = {'id': i, 'name': 'product {}'.format(i), 'description': 'product descr {}'.format(i)}
        requests.post('{}/product'.format(context.product_url), data=body)
        context.products_ids.append(i)


@when('user requests GET "/product"')
def step_impl(context):
    context.resp = requests.get('{}/product'.format(context.product_url))


@step('user requests POST "/product" with params')
def step_impl(context):
    body = {}
    for key, value in [(row['key'], row['value']) for row in context.table]:
        body[key] = value
    context.resp = requests.post('{}/product'.format(context.product_url), data=body)
    context.products_ids.append(body['id'])


@step('user requests PUT "/product/{id:Number}" with params')
def step_impl(context, id):
    body = {}
    for key, value in [(row['key'], row['value']) for row in context.table]:
        body[key] = value
    context.resp = requests.put('{}/product/{}'.format(context.product_url, id), data=body)


@step('user requests GET "/product/{id:Number}"')
def step_impl(context, id):
    context.resp = requests.get('{}/product/{}'.format(context.product_url, id))


@step('user requests DELETE "/product/{id:Number}"')
def step_impl(context, id):
    context.resp = requests.delete('{}/product/{}'.format(context.product_url, id))


@then('response with status code {code:Number}')
def step_impl(context, code):
    assert context.resp.status_code == code, f'Actual code {context.resp.status_code} differs from expected {code}'


@then('body contains {amount:Number} products with next fields')
def step_impl(context, amount):
    body = context.resp.json()
    assert body.__len__() == amount, f'actual number of products {body.__len__()} differs from expected {amount}'
    for product in body:
        for key in [row['key'] for row in context.table]:
            field = product.get(key, None)
            assert field is not None, f'{key} is not present in response'


@then('body contains product with next fields and values')
def step_impl(context):
    product = context.resp.json()
    for key, value in [(row['key'], row['value']) for row in context.table]:
        field_value = product.get(key, None)
        assert field_value == value, f'actual value {field_value} for {key} differs from expected {value}'
