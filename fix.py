import re
import os

def normalize_math_blocks(content):
    # Paso 1: Reemplaza \[...\] por $$...$$
    content = re.sub(r'\\\[(.*?)\\\]', r'$$\1$$', content, flags=re.DOTALL)
    
    # Paso 2: Dentro de bloques $$...$$, reemplaza \text{...} por \mathrm{...}
    def fix_text_inside_dollars(match):
        body = match.group(1)
        fixed_body = re.sub(r'\\text\s*{([^}]*)}', r'\\mathrm{\1}', body)
        return f"$$ {fixed_body} $$"

    content = re.sub(r'\$\$(.*?)\$\$', lambda m: fix_text_inside_dollars(m), content, flags=re.DOTALL)
    return content

def process_markdown_files(folder):
    for root, _, files in os.walk(folder):
        for file in files:
            if file.endswith(".md"):
                path = os.path.join(root, file)
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                new_content = normalize_math_blocks(content)
                if new_content != content:
                    with open(path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"✓ Modificado: {path}")
                else:
                    print(f"- Sin cambios: {path}")

# Cambia la ruta si tus .md están en otro lugar
carpeta_md = "./docs"

process_markdown_files(carpeta_md)
