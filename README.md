# 🧪 Pre-Entrega: Automatización QA — SauceDemo

Suite de pruebas automatizadas sobre [saucedemo.com] (https://www.saucedemo.com) utilizando Selenium WebDriver y Python.

## 🛠 Tecnologías
- Python 3.10+
- Selenium WebDriver
- Pytest
- Webdriver Manager

## 📁 Estructura
pre-entrega-Atesting-[GiordanoFrancisco]/
├── tests/
│   └── test_saucedemo.py
├── utils/
│   └── helpers.py
├── reports/
├── README.md
└── requirements.txt

## ⚙️ Instalación
```bash
pip install -r requirements.txt
```

## ▶️ Ejecutar pruebas
```bash
# Ejecutar todos los tests con reporte HTML
pytest tests/test_saucedemo.py -v --html=reports/reporte.html

# Solo un test específico
pytest tests/test_saucedemo.py::TestLogin -v
```

## 🧪 Casos de Prueba
| Test | Descripción | Criterio validado |
|------|-------------|-------------------|
| `test_login_exitoso` | Login con credenciales válidas | Redirect a `/inventory.html` + título "Swag Labs" |
| `test_catalogo_inventario` | Verificación del catálogo | Título, productos presentes, nombre y precio del primero |
| `test_agregar_producto_al_carrito` | Flujo de carrito | Contador, navegación y presencia del ítem correcto |

