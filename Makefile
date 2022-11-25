install: 
	poetry install

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-install-force:
	python3 -m pip install --force-reinstall --user ./dist/*.whl
	
package-install-winwsl:
	python -m pip install --user dist/*.whl
	
package-install-winwsl-force:
	python -m pip install --force-reinstall --user ./dist/*.whl

make lint:
	poetry run flake8 gendiff