from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='WhatsappWebKit',
    packages=find_packages(include=['WhatsappWebKit']),
    version='0.2.0',
    description='A small library helpful for manipulating whatsapp web using selenium',
    author='Devansh Gupta',
    setup_requires=['pytest-runner'],
    tests_require = ['pytest'],
    install_requries = ['selenium', 'schedule'],
    license='MIT',
    test_suite='tests',
    author_email='xyznfc@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)