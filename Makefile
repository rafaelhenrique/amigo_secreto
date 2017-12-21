clean:
	@echo "--> Cleaning pyc thrash"
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@echo ""

test:
	@coverage run manage.py test -v2
	@coverage report -m --fail-under 68

