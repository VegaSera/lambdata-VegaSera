from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="VegaSera_lambdata",
    version="0.0.3",
    author="Wesley Mountford",
    author_email="goe_horus@hotmail.com",
    description="Educationamalism",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    #url="https://github.com/s2t2/lambdata-12y",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)