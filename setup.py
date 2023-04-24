import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'pynse',
    packages=setuptools.find_packages(),
    version = '0.1.0',
    include_package_data=True,
    description = 'Python library to fetch NSE data',
    long_description=long_description,
    long_description_content_type="text/markdown",  author = 'Anirudh Prakash',
    author_email = 'anirudh.prakash05@gmail.com',
    url = 'https://github.com/anirudh-777/pynse',
    install_requires=['pandas>=1.5.3', 'requests>=2.25.1'],
    extras_requires={
        'dev': ['pytest>=7.0', 'twine>=3.4.2', 'wheel>=0.36.2'],
    },
    keywords = ['nseindia', 'nse', 'python', 'sdk', 'trading', 'stock markets'],
    classifiers=[
      'Intended Audience :: Developers',
      'Natural Language :: English',
      'Operating System :: OS Independent',
      'Programming Language :: Python',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: Implementation :: PyPy',
      'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    python_requires='>=3.8',
)
