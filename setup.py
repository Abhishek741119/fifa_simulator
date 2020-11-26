from setuptools import setup
with open('README.md') as r:
    desc=r.read()
setup(
    name="fifa_simulator",
    version="1.0.1",
    description='A Python Package for Simulation of fifa-like tournament fifa_simulator',
    long_description=desc,
    long_description_content_type='text/markdown',
    url='https://github.com/Abhishek741119/fifa_simulator',
    license="MIT",
    author="Marupaka Sai Abhishek",
    author_email="abhishekabhishek83414@gmail.com",
    classifiers=[
                 'Programming Language :: Python :: 3',
                 ],
    python_requires='>=3.0',
    packages=['fixtures'],
    include_package_data=True,
    install_requires=["pandas"],
)