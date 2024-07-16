import setuptools

version = "0.3.0"

with open("aix360/version.py", "w") as f:
    f.write('# generated by setup.py\nversion = "{}"\n'.format(version))

extra_requires = {
    "default": [
        "numpy",
        "pandas",
        "scikit-learn",
        "matplotlib",
    ],
    "rbm": [
        "matplotlib",
        "pandas<2.0.0",
        "scipy>=0.17,<=1.10.1",
        "scikit-learn<1.2.0",
        "cvxpy>=1.1",
        "numpy<=1.24.3",
    ],
    "profwt": [
        "keras==2.3.1",
        "scipy>=0.17",
        "tensorflow==1.14",
    ],
    "cofrnet": [
        "pandas<2.0.0",
        "torch",
        "tqdm",
    ],
    "ted": [
        "pandas",
        "scikit-learn",
    ],
    "dipvae": [
        "matplotlib",
        "torch",
        "torchvision",
    ],
    "rule_induction": [
        "matplotlib",
        "numba",
        "pandas<2.0.0",
        "scikit-learn",
        "nyoka",
        "cvxpy",
        "xmltodict==0.12.0",
    ],
    "lime": [
        "lime",
        "tqdm",
        "pandas",
    ],
    "matching": ["otoc @ git+https://github.com/IBM/otoc@main#egg=otoc"],
    "protodash": [
        "scikit-learn",
        "xport",
        "scipy>=0.17,<=1.10.1",
        "cvxpy",
        "requests",
    ],
    "contrastive": [
        "keras==2.3.1",
        "tensorflow==1.14",
        "requests",
        "scipy>=0.17",
        "scikit-image",
        "torch",
        "h5py<3.0.0",  # to resolve keras error: 'str' object has no attribute 'decode'
    ],
    "shap": [
        "keras==2.3.1",
        "tensorflow==1.14",
        "matplotlib",
        "numba",
        "pandas<2.0.0",
        "shap",
        "tqdm",
    ],
    "nncontrastive": [
        "pandas<2.0.0",
        "tensorflow==2.9.3",
    ],
    "tsice": [
        "pandas<2.0.0",
        "scipy",
        "plotly",  # required for units
        "ipython",  # required for units
        "kaleido",  # required for units
        "requests",  # required for dataset and units
    ],
    "tssaliency": [
        "pandas<2.0.0",
        "requests",  # required for dataset and units
    ],
    "imd": [
        "numpy<2.0.0",
        "pandas",
        "scikit-learn",
        "matplotlib",
        "networkx",
        "graphviz",
        "pygraphviz",  # for creating graph visualization
    ],
    "tslime": [
        "pandas<2.0.0",
        "scipy",
        "requests",  # required for dataset and units
    ],
    "gce": [
        "pandas<2.0.0",
        "shap",
        "numba<=0.56",
        "requests",  # required for dataset and units
    ],
    "ecertify": [
        "numpy<2.0.0",
        "pandas",
        "scikit-learn",
        "matplotlib",
        "zoopt",
        "lime",
        "shap==0.42.1",
    ],
}

# minimal dependencies in install_requires
install_requires = extra_requires["default"]  # ted is supported by default.

setuptools.setup(
    name="aix360",
    version=version,
    description="IBM AI Explainability 360",
    authos="aix360 developers",
    url="https://github.com/IBM/AIX360",
    author_email="aix360@us.ibm.com",
    packages=setuptools.find_packages(),
    license="Apache License 2.0",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    install_requires=install_requires,
    extras_require=extra_requires,
    package_data={
        "aix360": [
            "data/*",
            "data/*/*",
            "data/*/*/*",
            "models/*",
            "models/*/*",
            "models/*/*/*",
        ]
    },
    include_package_data=True,
    zip_safe=False,
)
