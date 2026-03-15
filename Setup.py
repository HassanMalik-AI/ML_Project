from setuptools import find_packages, setup
from typing import List

HYPHEN_E_dot = "-e ."
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.replace("\n", "") for req in requirements]
        if HYPHEN_E_dot in requirements:
            requirements.remove(HYPHEN_E_dot)
    return requirements

setup(
    name="ML-Project",
    version="0.0.1",
    packages=find_packages(),  
    author="Hassan",
    author_email="hassan.softwarengineer@gmail.com",
    #packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)