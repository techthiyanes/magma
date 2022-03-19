import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements_for_setup.txt") as f:
    required = f.read().splitlines()

setuptools.setup(
    name="magma",
    version="0.0.1",
    author="Aleph-Alpha",
    author_email="",
    description="A GPT-style multimodal model that can understand any combination of images and language",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Aleph-Alpha/magma",
    packages=setuptools.find_packages(),
    install_requires=required,
    python_requires=">=3.9",
    include_package_data=True,
    dependency_links = [
        'https://github.com/finetuneanon/transformers.git#egg=transformers',
        'https://github.com/openai/CLIP.git'
    ],
    classifiers=[
        "Natural Language :: English",
        "Programming Language :: Python :: 3.8",
    ],
)