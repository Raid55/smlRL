from setuptools import setup, find_packages


requires = [
    'Flask',
    'SQLAlchemy'
]


setup(
    name='smlRL',
    version='0.1',
    author='Raid55',
    author_email='boutboulnicholas@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires
)
