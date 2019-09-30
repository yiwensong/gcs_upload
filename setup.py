"""setup.py"""
import setuptools

with open('README.md', 'r') as readme:
    README_TEXT = readme.read()

setuptools.setup(
    name='gcs-upload',
    version='0.1.0',
    license='MIT',
    author='yiwen song',
    author_email='songzgy@gmail.com',
    url='https://github.com/yiwensong/gcs_upload',
    description='travis ci wrapper for google cloud storage',
    long_description=README_TEXT,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(exclude=['tests*']),
    install_requires=[
        'Markdown',
    ],
    classifiers=[
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ],
    entry_points={
        'console_scripts': [
            'gcs-upload = gcs_upload:main',
        ],
    },
)
