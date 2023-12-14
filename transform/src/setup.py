import setuptools

setuptools.setup(
    name="boxball-schemas",
    version="0.0.8",
    author="David Roher",
    description="Schemas for the Boxball project that can be used for extension or code completion",
    url="https://github.com/droher/boxball",
    packages=["boxball_schemas"],
    python_requires='>=3.6',
    install_requires=["sqlalchemy>=1.3.3"]
)
