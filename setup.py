from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='fact_checking',
      version='0.0.3',
      url='http://github.com/fractalego/fact_checking',
      author='Alberto Cetoli',
      author_email='alberto@nlulite.com',
      description="Check a claim consistency against the provided evidence",
      long_description=long_description,
      long_description_content_type="text/markdown",
      packages=['fact_checking',
                ],
      install_requires=[
          'numpy',
          'transformers',
          'torch',
          'jupyterlab',
      ],
      classifiers=[
          'License :: OSI Approved :: MIT License',
      ],
      include_package_data=True,
      zip_safe=False)
