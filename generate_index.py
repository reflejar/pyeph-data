import os
from pathlib import Path

def generate_index():
    """Genera un index.html con todas las bases de datos disponibles."""
    
    # Obtener archivos de cada carpeta
    individual_files = []
    hogar_files = []
    canastas_files = []
    adulto_equivalente_files = []
    mautic_hogar_files = []
    mautic_individual_files = []
    
    if os.path.exists('individual'):
        individual_files = sorted(
            [f for f in os.listdir('individual') if f.endswith('.zip')],
            reverse=True
        )
    
    if os.path.exists('hogar'):
        hogar_files = sorted(
            [f for f in os.listdir('hogar') if f.endswith('.zip')],
            reverse=True
        )
    
    if os.path.exists('canastas'):
        canastas_files = sorted(
            [f for f in os.listdir('canastas') if f.endswith('.zip')],
            reverse=True
        )
    
    if os.path.exists('adulto_equivalente'):
        adulto_equivalente_files = sorted(
            [f for f in os.listdir('adulto_equivalente') if f.endswith('.zip')],
            reverse=True
        )
    
    if os.path.exists('mautic_hogar'):
        mautic_hogar_files = sorted(
            [f for f in os.listdir('mautic_hogar') if f.endswith('.zip')],
            reverse=True
        )
    
    if os.path.exists('mautic_individual'):
        mautic_individual_files = sorted(
            [f for f in os.listdir('mautic_individual') if f.endswith('.zip')],
            reverse=True
        )
    
    # Generar HTML
    html = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PyEPH Data - Bases de Datos EPH</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-50 min-h-screen">
    <div class="container mx-auto px-4 py-8 max-w-6xl">
        <div class="bg-white rounded-lg shadow-sm p-6 mb-6">
            <h1 class="text-3xl font-bold text-gray-800 mb-2">PyEPH Data Repository</h1>
            <p class="text-gray-600">
                Bases de microdatos de la Encuesta Permanente de Hogares (EPH) del INDEC <br />
                <small class="text-gray-500">(DDBB no oficiales)</small>

            </p>
        </div>
        
        <div class="grid md:grid-cols-2 gap-6">
            <!-- Carpeta Individual -->
            <div class="bg-white rounded-lg shadow-sm p-6">
                <div class="flex items-center mb-4">
                    <svg class="w-8 h-8 text-blue-500 mr-3" fill="currentColor" viewBox="0 0 20 20">
                        <path d="M2 6a2 2 0 012-2h5l2 2h5a2 2 0 012 2v6a2 2 0 01-2 2H4a2 2 0 01-2-2V6z"></path>
                    </svg>
                    <div>
                        <h2 class="text-xl font-semibold text-gray-800">individual/</h2>
                        <p class="text-sm text-gray-500">{} archivos</p>
                    </div>
                </div>
                <div class="space-y-1 max-h-96 overflow-y-auto">
""".format(len(individual_files))
    
    # Agregar archivos individuales
    for file in individual_files:
        html += f'                    <a href="individual/{file}" class="block px-3 py-2 text-sm text-gray-700 hover:bg-blue-50 hover:text-blue-600 rounded transition-colors">📄 {file}</a>\n'
    
    html += """                </div>
            </div>
            
            <!-- Carpeta Hogar -->
            <div class="bg-white rounded-lg shadow-sm p-6">
                <div class="flex items-center mb-4">
                    <svg class="w-8 h-8 text-green-500 mr-3" fill="currentColor" viewBox="0 0 20 20">
                        <path d="M2 6a2 2 0 012-2h5l2 2h5a2 2 0 012 2v6a2 2 0 01-2 2H4a2 2 0 01-2-2V6z"></path>
                    </svg>
                    <div>
                        <h2 class="text-xl font-semibold text-gray-800">hogar/</h2>
                        <p class="text-sm text-gray-500">{} archivos</p>
                    </div>
                </div>
                <div class="space-y-1 max-h-96 overflow-y-auto">
""".format(len(hogar_files))
    
    # Agregar archivos de hogar
    for file in hogar_files:
        html += f'                    <a href="hogar/{file}" class="block px-3 py-2 text-sm text-gray-700 hover:bg-green-50 hover:text-green-600 rounded transition-colors">📄 {file}</a>\n'
    
    html += """                </div>
            </div>
            
            <!-- Carpeta Canastas -->
            <div class="bg-white rounded-lg shadow-sm p-6">
                <div class="flex items-center mb-4">
                    <svg class="w-8 h-8 text-yellow-500 mr-3" fill="currentColor" viewBox="0 0 20 20">
                        <path d="M2 6a2 2 0 012-2h5l2 2h5a2 2 0 012 2v6a2 2 0 01-2 2H4a2 2 0 01-2-2V6z"></path>
                    </svg>
                    <div>
                        <h2 class="text-xl font-semibold text-gray-800">canastas/</h2>
                        <p class="text-sm text-gray-500">{} archivos</p>
                    </div>
                </div>
                <div class="space-y-1 max-h-96 overflow-y-auto">
""".format(len(canastas_files))
    
    for file in canastas_files:
        html += f'                    <a href="canastas/{file}" class="block px-3 py-2 text-sm text-gray-700 hover:bg-yellow-50 hover:text-yellow-600 rounded transition-colors">📄 {file}</a>\n'
    
    html += """                </div>
            </div>
            
            <!-- Carpeta Adulto Equivalente -->
            <div class="bg-white rounded-lg shadow-sm p-6">
                <div class="flex items-center mb-4">
                    <svg class="w-8 h-8 text-purple-500 mr-3" fill="currentColor" viewBox="0 0 20 20">
                        <path d="M2 6a2 2 0 012-2h5l2 2h5a2 2 0 012 2v6a2 2 0 01-2 2H4a2 2 0 01-2-2V6z"></path>
                    </svg>
                    <div>
                        <h2 class="text-xl font-semibold text-gray-800">adulto_equivalente/</h2>
                        <p class="text-sm text-gray-500">{} archivos</p>
                    </div>
                </div>
                <div class="space-y-1 max-h-96 overflow-y-auto">
""".format(len(adulto_equivalente_files))
    
    for file in adulto_equivalente_files:
        html += f'                    <a href="adulto_equivalente/{file}" class="block px-3 py-2 text-sm text-gray-700 hover:bg-purple-50 hover:text-purple-600 rounded transition-colors">📄 {file}</a>\n'
    
    html += """                </div>
            </div>
            
            <!-- Carpeta Mautic Hogar -->
            <div class="bg-white rounded-lg shadow-sm p-6">
                <div class="flex items-center mb-4">
                    <svg class="w-8 h-8 text-red-500 mr-3" fill="currentColor" viewBox="0 0 20 20">
                        <path d="M2 6a2 2 0 012-2h5l2 2h5a2 2 0 012 2v6a2 2 0 01-2 2H4a2 2 0 01-2-2V6z"></path>
                    </svg>
                    <div>
                        <h2 class="text-xl font-semibold text-gray-800">mautic_hogar/</h2>
                        <p class="text-sm text-gray-500">{} archivos</p>
                    </div>
                </div>
                <div class="space-y-1 max-h-96 overflow-y-auto">
""".format(len(mautic_hogar_files))
    
    for file in mautic_hogar_files:
        html += f'                    <a href="mautic_hogar/{file}" class="block px-3 py-2 text-sm text-gray-700 hover:bg-red-50 hover:text-red-600 rounded transition-colors">📄 {file}</a>\n'
    
    html += """                </div>
            </div>
            
            <!-- Carpeta Mautic Individual -->
            <div class="bg-white rounded-lg shadow-sm p-6">
                <div class="flex items-center mb-4">
                    <svg class="w-8 h-8 text-indigo-500 mr-3" fill="currentColor" viewBox="0 0 20 20">
                        <path d="M2 6a2 2 0 012-2h5l2 2h5a2 2 0 012 2v6a2 2 0 01-2 2H4a2 2 0 01-2-2V6z"></path>
                    </svg>
                    <div>
                        <h2 class="text-xl font-semibold text-gray-800">mautic_individual/</h2>
                        <p class="text-sm text-gray-500">{} archivos</p>
                    </div>
                </div>
                <div class="space-y-1 max-h-96 overflow-y-auto">
""".format(len(mautic_individual_files))
    
    for file in mautic_individual_files:
        html += f'                    <a href="mautic_individual/{file}" class="block px-3 py-2 text-sm text-gray-700 hover:bg-indigo-50 hover:text-indigo-600 rounded transition-colors">📄 {file}</a>\n'
    
    html += """                </div>
            </div>
        </div>
        
        <div class="mt-6 text-center text-gray-600 text-sm">
            <p>
                Datos originales publicados por <strong>INDEC</strong> bajo licencia de datos abiertos.<br>
                Este repositorio es parte del proyecto <a href="https://github.com/reflejar/pyeph" class="text-blue-500 hover:underline" target="_blank">PyEPH</a>
            </p>
        </div>
    </div>
</body>
</html>"""
    
    # Escribir archivo
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✓ index.html generado exitosamente")
    print(f"  - {len(individual_files)} archivos individuales")
    print(f"  - {len(hogar_files)} archivos de hogar")
    print(f"  - {len(canastas_files)} archivos de canastas")
    print(f"  - {len(adulto_equivalente_files)} archivos de adulto_equivalente")
    print(f"  - {len(mautic_hogar_files)} archivos de mautic_hogar")
    print(f"  - {len(mautic_individual_files)} archivos de mautic_individual")

if __name__ == '__main__':
    generate_index()
