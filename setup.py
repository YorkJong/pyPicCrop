from setuptools import setup, find_packages

setup(
    name = 'PicCrop',
    version = '1.0',
    description = 'Picture Cropping',
    license = 'Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description = open('README.md').read(),
    author = 'Jiang Yu-Kuan',
    author_email = 'yukuan.jiang@gmail.com',
    url = 'https =//bitbucket.org/YorkJong/pypiccrop',
    packages = find_packages(),
    install_requires = ['Image', 'ImageDraw'],
)

