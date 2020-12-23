from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(name='WhatsappWebKit',
      version='1.1.0',
      description='A small library helpful for manipulating whatsapp web using selenium',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/Devansh-bit/WhatsappWebKit',
      author='Devansh Gupta',
      author_email='xyznfc@gmail.com',
      license='MIT',
      packages=['WhatsappWebKit'],
      install_requires=[
          'selenium',
      ],
      zip_safe=False,
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ]
)

