from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="kurumi-lang",
    version="2.0.0",
    author="Kurumi Team",
    author_email="truongnpnps40833@gmail.com",
    description="Kurumi - Ngôn ngữ lập trình API hiện đại",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kurumi-2004/ngon-ngu-lap-trinh-API-kurumi",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "kurumi_lang": ["*.md", "*.kuru"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "click>=7.0",
        "colorama>=0.4.3",
    ],
    entry_points={
        "console_scripts": [
            "kurumi=kurumi_lang.cli:main",
        ],
    },
)