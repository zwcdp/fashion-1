# help function
help:
	@echo ""
	@echo "download-data:"
	@echo "	download data to data/raw/"
	@echo "show-single:"
	@echo "	print a single image from the raw data"

# Download data by calling get_data
download-data: src/data/get_data.sh
	bash src/data/get_data.sh

# Call data reader script and show single image in dataset
show-single: src/data/data_reader.py
	python src/data/data_reader.py

pca: src/analysis/pca.py
	python src/analysis/pca.py