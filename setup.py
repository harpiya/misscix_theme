# -*- coding: utf-8 -*-
# @Author: Saadettin Yasir AKEL <developer>
# @Date:   2018-12-27T11:09:22+03:00
# @Email:  yasir@harpiya.com
# @Project: Harpiya Kurumsal Yönetim Sistemi
# @Filename: setup.py
# @Last modified by:   developer
# @Last modified time: 2018-12-28T22:14:05+03:00
# @License: MIT License. See license.txt
# @Copyright: Harpiya Yazılım Teknolojileri



from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='misscix_theme',
    version=version,
    description=u'Miss Cix Toptan Alışveriş Sitesi',
    author=u'Harpiya Yazılım Teknolojileri',
    author_email='https://harpiya.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
