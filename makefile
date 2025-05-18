# Variables
VENV=venv
PYTHON=$(VENV)/bin/python
PIP=$(VENV)/bin/pip

# 🛠️ Crear entorno virtual y activar
setup:
	@echo "🚀 Configurando entorno virtual..."
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -e .

# ▶️ Ejecutar el bot principal
run:
	@echo "🔁 Ejecutando Forex Bot..."
	$(PYTHON) src/main.py

# 🧪 Ejecutar tests
test:
	@echo "🧪 Ejecutando tests..."
	$(PYTHON) -m unittest discover -s tests

# 🧹 Limpiar archivos temporales
clean:
	@echo "🧹 Limpiando archivos temporales..."
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -exec rm -r {} +

# 🔄 Reinstalar dependencias
reinstall:
	@echo "♻️ Reinstalando proyecto..."
	rm -rf $(VENV)
	make setup

# 🆘 Ayuda
help:
	@echo "Comandos disponibles:"
	@echo "  make setup       => Crea entorno virtual e instala dependencias"
	@echo "  make run         => Ejecuta el bot principal"
	@echo "  make test        => Ejecuta los tests unitarios"
	@echo "  make clean       => Limpia archivos pyc y cachés"
	@echo "  make reinstall   => Borra y reinstala el entorno"
