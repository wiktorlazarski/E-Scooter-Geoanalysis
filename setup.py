import setuptools

# Parse requirements
install_requires = [line.strip() for line in open("requirements.txt").readlines()]

# Get long description
with open("README.md", "r", encoding="UTF-8") as fh:
    long_description = fh.read()

version = "1.0.0"

# Setup package
setuptools.setup(
    name="geoanalysis_app",
    version=version,
    author="Wiktor Łazarski, Ula Tworzydło, Zosia Matyjewska",
    description="E-scooter geoanalysis streamlit application.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wiktorlazarski/E-Scooter-Geoanalysis",
    packages=["geoanalysis_app"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=install_requires,
    entry_points={
        "console_scripts": ["geoapp-run = geoanalysis_app.cli:run"]
    },
)