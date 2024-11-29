from setuptools import find_packages, setup

package_name = 'simple_pub_sub'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='hegde-aryan',
    maintainer_email='hegdearyandeveloper@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'talker = simple_pub_sub.publisher:main',
            'listener = simple_pub_sub.subscriber:main',

        ],
    },
)
