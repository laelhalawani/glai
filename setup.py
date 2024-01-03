from setuptools import setup, find_packages

setup(
    name="glai",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        'llama-cpp-python',
        'requests>=2.31.0',
        'beautifulsoup4>=4.9.3',
    ],
    package_data={'glai': ['back_end/model_db/gguf_models/*.json']},
    include_package_data=True,
    author="Łael Al-Halawani",
    author_email="laelhalawani@gmail.com",
)