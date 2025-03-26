from setuptools import setup, find_packages

setup(
    name="mylibrary",  # Package name
    version="0.1.0",  # Version
    packages=find_packages(),  # Automatically finds "mylibrary"
    install_requires=[],  # Add dependencies here if needed
    author="Your Name",
    author_email="your.email@example.com",
    description="A short description of your library",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/mylibrary",  # Change if hosted
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.6",  # Specify Python version requirement
)
