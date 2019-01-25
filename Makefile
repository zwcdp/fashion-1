# help function
help:
	@echo ""
	@echo "install-venv"
	@echo "	Install virtual python environment"
	@echo "pip-packages"
	@echo "	install packages using pip"
	@echo "pip-freeze"
	@echo "	Write current packages to requirements.txt"
	@echo "download-data:"
	@echo "	download data to data/raw/"
	@echo "show-single:"
	@echo "	print a single image from the raw data"

# Use virtualenv to install a virtual environment
install-venv:
	virtualenv venv

# pip install packages
pip-packages:
	pip install -r requirements.txt

# Write current packages to requirements.txt
pip-freeze:
	pip freeze > requirements.txt

# Download data by calling get_data
download-data: src/data/get_data.sh
	bash src/data/get_data.sh

# Call data reader script and show single image in dataset
show-single: src/data/data_reader.py
	python src/data/data_reader.py

# Run pca
pca: src/run.py
	python src/run.py --pca