# -*- coding: utf-8 -*-
# @Author: Saadettin Yasir AKEL <developer>
# @Date:   2018-12-27T11:09:22+03:00
# @Email:  yasir@harpiya.com
# @Project: Harpiya Kurumsal Yönetim Sistemi
# @Filename: hooks.py
# @Last modified by:   developer
# @Last modified time: 2018-12-28T22:14:33+03:00
# @License: MIT License. See license.txt
# @Copyright: Harpiya Yazılım Teknolojileri



from __future__ import unicode_literals
app_name = "misscix_theme"
app_title = u"Miss Cix Website Şablonu"
app_publisher = u"Harpiya Yazılım Teknolojileri"
app_description = u"Miss Cix Websitesi Şablonu"
app_icon = "fa fa-globe"
app_color = "orange"
app_email = "info@harpiya.com"
app_url = "https://harpiya.com"
app_version = "0.0.1"
hide_in_installer = True
home_page = "home"


# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/misscix_theme/css/misscix_theme.css"
# app_include_js = "/assets/misscix_theme/js/misscix_theme.js"

# include js, css files in header of web template
# web_include_css = "/assets/misscix_theme/css/misscix_theme.css"
# web_include_js = "/assets/misscix_theme/js/misscix_theme.js"

# Installation
# ------------

# before_install = "misscix_theme.install.before_install"
# after_install = "misscix_theme.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "misscix_theme.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.core.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.core.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"misscix_theme.tasks.all"
# 	],
# 	"daily": [
# 		"misscix_theme.tasks.daily"
# 	],
# 	"hourly": [
# 		"misscix_theme.tasks.hourly"
# 	],
# 	"weekly": [
# 		"misscix_theme.tasks.weekly"
# 	]
# 	"monthly": [
# 		"misscix_theme.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "misscix_theme.install.before_tests"
