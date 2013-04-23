from setuptools import setup, find_packages
 
setup(
    name='snowwhite',
    version='0.1',
    description='An implicit and explicit sentiment analyzer.',
    author='Maksim Tsvetovat, @maksim2042',
    author_email='maksim@tsvetovat.org',
    packages=find_packages(),
    package_data={'snowwhite': ['data/*.*']},
    include_package_data=True,
    install_requires=["guess-language >= 0.02",
        "networkx >= 1.6",
        "numpy >= 1.6",
        "nltk >= 2.0",
        "hottie >= 0.1"
        ]
)
