from setuptools import setup

setup(
    name='flask_boiler',
    include_package_data=True,
    packages=['src'],
    version="1.0.0",
    install_requires=[
        'flask',
    ],
)

