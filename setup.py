import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rocketlaunchlive", 
    packages=["rocketlaunchlive"],
    version="0.0.1",
    license='apache-2.0',
    author="Tim Empringham",
    author_email="tim.empringham@live.ca",
    description="Rocket Launch Live - Next 5 Launches API Wrapper.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/djtimca/spacex-api",
    download_url = 'https://github.com/djtimca/rocketlaunchlive-api/archive/v_001.tar.gz',
    keywords = ['Rocket', 'Launch'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    python_requires='>=3.8',
)