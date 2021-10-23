import json
import os

import requests


def before_all(context):
    userdata = context.config.userdata
    context.configfile = userdata.get('configfile', 'products_api_tests/resources/config/local.json')
    if os.path.exists(context.configfile):
        assert context.configfile.endswith(".json"), 'configfile is not json type'
        more_userdata = json.load(open(context.configfile))
        context.config.update_userdata(more_userdata)
    context.product_url = context.config.userdata.get("product_url")
    context.products_ids = []


def after_scenario(context, scenario):
    delete_created_products(context.products_ids, context.product_url)


def delete_created_products(products_ids, product_url):
    for pr_id in products_ids:
        requests.delete('{}/product/{}'.format(product_url, pr_id))
