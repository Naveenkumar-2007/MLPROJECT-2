
from setuptools import find_packages,setup
from typing import List

hyper_meter='-e .'
def get_hyper(filepath:str)->List[str]:
    requirement=[]
    with open(filepath) as file:
        requirement=file.readlines()
        requirement=[req.replace('/n','') for req in requirement]
        if hyper_meter in requirement:
            requirement.remove(hyper_meter)
    return requirement
setup(
name='mlproject-2',
version='0.0.1',
author='naveen',
author_email='naveenkumar686@gmail.com',
packages=find_packages(),
install_requires=get_hyper('requirements.txt')
)
