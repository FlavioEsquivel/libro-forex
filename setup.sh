#!/bin/bash

echo "🚀 Iniciando configuración del entorno para Forex Bot..."

# Crear entorno virtual
echo "📦 Creando entorno virtual..."
python3 -m venv venv

# Activar entorno virtual
source venv/bin/activate

# Actualizar pip
echo "⬆️  Actualizando pip..."
pip install --upgrade pip

# Instalar el paquete en modo editable
echo "📚 Instalando Forex Bot en modo editable..."
pip install -e .

echo "✅ Instalación completada. Para activar el entorno en el futuro, usa:"
echo "    source venv/bin/activate"
echo "Y ejecuta el bot con:"
echo "    forex-bot"
