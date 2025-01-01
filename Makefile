.PHONY: clean

VENV = .venv
PYTHON_VERSION = 3.13

.venv/bin/activate: requirements.txt
	python${PYTHON_VERSION} -m venv $(VENV)
	$(VENV)/bin/pip install --upgrade pip
	$(VENV)/bin/pip install --upgrade -r requirements.txt

clean:
	rm -rf $(VENV)
