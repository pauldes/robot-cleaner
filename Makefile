install:
	@echo 'You must be root to install'
	pip install pygal
run:
	python Graph.py
	@echo 'Results are available in graph_rendering.svg'
