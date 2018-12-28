# -*- coding: utf-8 -*-
# @Author: Saadettin Yasir AKEL <developer>
# @Date:   2018-12-27T11:09:22+03:00
# @Email:  yasir@harpiya.com
# @Project: Harpiya Kurumsal Yönetim Sistemi
# @Filename: desktop.py
# @Last modified by:   developer
# @Last modified time: 2018-12-28T22:13:01+03:00
# @License: MIT License. See license.txt
# @Copyright: Harpiya Yazılım Teknolojileri



from __future__ import unicode_literals
from frappe import _

def get_data():
	return {
		"MissCix Theme": {
			"color": "orange",
			"icon": "fa fa-globe",
			"label": _("Miss Cix Site Şablonu")
		}
	}
