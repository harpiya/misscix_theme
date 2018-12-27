# @Author: Saadettin Yasir AKEL <developer>
# @Date:   2018-12-27T11:09:22+03:00
# @Email:  yasir@harpiya.com
# @Project: Harpiya Kurumsal Yönetim Sistemi
# @Filename: setup.py
# @Last modified by:   developer
# @Last modified time: 2018-12-27T11:11:32+03:00
# @License: MIT License. See license.txt
# @Copyright: Harpiya Yazılım Teknolojileri



from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='misscix_theme',
    version=version,
    description='Miss Cix Toptan Alışveriş Sitesi',
    author='Frappe',
    author_email='https://harpiya.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
