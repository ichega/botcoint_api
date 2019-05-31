from setuptools import setup

setup(
    name="botcoint_api",
    version="0.0.1",
    description="Botcoint API module for bots :)",
    url="https://github.com/ichega/botcoint_api",
    author="Pavel Katskov",
    author_email="pasha_kackov@mail.ru",
    license="MIT",
    packages=[
        "botcoint"
    ],
    install_requires=[
        "requests",
        "addict",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 3 - Alpha"
    ]
)

