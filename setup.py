from distutils.core import setup

setup(
    name='accelerometer_features_evaluation',
    version='0.0.3',
    packages=[
        'accelerometerfeatures.utils',
        'accelerometerfeatures.utils.pytorch',
    ],
    url='',
    license='',
    author='Patrick Westphal',
    author_email='',
    description='',
    install_requires=[
        'matplotlib==3.0.0',
        'scipy==1.1.0',
        'pandas==0.23.4',
        'numpy==1.15.4',
        'torch==1.0.0',
        'torchvision==0.2.1',
    ]
)
