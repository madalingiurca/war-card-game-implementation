"""
py2app build script for MyApplication

Usage:
    python setup.py py2app
"""

from setuptools import setup

# DATA_FILES = [('assets/cards', ['assets/cards/2_clover.png'])]

# DATA_FILES = [
#     ('assets/cards', glob('images/*.jpg')),
#     ('assets/sound', glob('sound/*')),
# ]

setup(
    app=["main.py"],
    setup_requires=["py2app"],
    # data_files=DATA_FILES,
    include_package_data=True
)
