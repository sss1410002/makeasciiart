from setuptools import setup, find_packages


setup(
    name             = 'img2ascii',
    version          = '0.2',
    description      = 'Convert image to ascii art',
    long_description_content_type='text/markdown',
    long_description = open('README.md').read(),
    author           = 'SSS',
    author_email     = 'sss1410002@gmail.com',
    url              = 'https://github.com/sss1410002/asciiart',
    license          = 'MIT',
    install_requires = ['opencv-python','numpy'],
    packages         = ['img2ascii'],
    keywords         = ['opencv', 'ascii', 'ascii art'],
    python_requires  = '>=3',
    zip_safe=False,
    classifiers      = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ]
)