# @Author: Saadettin Yasir AKEL <developer>
# @Date:   2019-01-03T13:44:02+03:00
# @Email:  yasir@harpiya.com
# @Project: Harpiya Kurumsal Yönetim Sistemi
# @Filename: home.py
# @Last modified by:   developer
# @Last modified time: 2019-01-03T13:46:12+03:00
# @License: MIT License. See license.txt
# @Copyright: Harpiya Yazılım Teknolojileri

from __future__ import unicode_literals
import frappe
from frappe.website.doctype.website_slideshow.website_slideshow import get_slideshow

no_cache = 1
no_sitemap = 1

def get_context(context):
	homepage = frappe.get_doc('Homepage')

	for item in homepage.products:
		route = frappe.db.get_value('Item', item.item_code, 'route')
		if route:
			item.route = '/' + route

	context.title = homepage.title or homepage.company

	# show atleast 3 products
	if len(homepage.products) < 3:
		for i in range(3 - len(homepage.products)):
			homepage.append('products', {
				'item_code': 'product-{0}'.format(i),
				'item_name': frappe._('Product {0}').format(i),
				'route': '#'
			})

	context.homepage = homepage

	if context.slideshow:
		context.update(get_slideshow(self))
