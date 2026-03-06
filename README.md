# NETRUNNER_PROTOCOLS_v2.0 — Portafolio Profesional

> *Desarrollado por **Ciro Cortes** — Full Stack Developer · Chile 🇨🇱*

Portafolio profesional con identidad visual inspirada en el universo **Cyberpunk 2077**, construido sobre una arquitectura Django + PostgreSQL lista para producción. Incluye gestión dinámica de proyectos y habilidades desde el panel admin, formulario de contacto funcional y despliegue continuo en Render.

---

## Stack Tecnológico

| Capa | Tecnología |
|---|---|
| Backend | Python 3.12 · Django 6.0 |
| Base de Datos | PostgreSQL (local) · Render PostgreSQL (producción) |
| Frontend | Tailwind CSS (CDN) · CSS3 Animations |
| Tipografía e Íconos | Space Grotesk · Material Symbols Outlined (servidos localmente) |
| Servidor de Producción | Gunicorn · WhiteNoise |
| Despliegue | Render (render.yaml) |
| Seguridad | python-dotenv · Variables de entorno |

---

## Arquitectura del Proyecto

```
portfolio_project/
├── config/               # Configuración Django (settings, urls, wsgi)
├── core/                 # App principal
│   ├── models.py         # Project, Skill, ContactMessage
│   ├── views.py          # Vista home (GET + POST)
│   ├── admin.py          # Panel de administración
│   └── management/
│       └── commands/
│           └── seed_portfolio.py  # Datos iniciales de portfolio
├── static/
│   ├── css/style.css     # Estilos custom + animaciones Cyberpunk
│   ├── fonts/            # Fuentes woff2 locales (sin CDN externo)
│   └── images/           # Assets visuales
├── templates/
│   └── core/
│       ├── base.html     # Plantilla madre (DRY)
│       └── index.html    # Vista principal
├── .env.example          # Plantilla de variables de entorno
├── render.yaml           # Configuración de despliegue en Render
├── Procfile              # Comando de inicio para Gunicorn
└── requirements.txt      # Dependencias del proyecto
```

---

## Instalación Local

### Requisitos previos
- Python 3.12+
- PostgreSQL corriendo localmente
- Git

### Pasos

```bash
# 1. Clonar el repositorio
git clone https://github.com/CiroCortes/netrunner-portfolio.git
cd netrunner-portfolio

# 2. Crear y activar entorno virtual
python -m venv venv
.\venv\Scripts\Activate.ps1        # Windows PowerShell
# source venv/bin/activate          # macOS / Linux

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Configurar variables de entorno
copy .env.example .env             # Windows
# cp .env.example .env             # macOS / Linux
# Editar .env con tus credenciales de PostgreSQL

# 5. Aplicar migraciones
python manage.py migrate

# 6. Cargar datos del portfolio
python manage.py seed_portfolio

# 7. Crear superusuario para el panel admin
python manage.py createsuperuser

# 8. Iniciar servidor de desarrollo
python manage.py runserver
```

Abre [http://localhost:8000](http://localhost:8000) en tu navegador.
Panel admin: [http://localhost:8000/admin](http://localhost:8000/admin)

---

## Despliegue en Render

El proyecto incluye `render.yaml` con configuración completa. Pasos:

1. Subir el repositorio a GitHub
2. Crear una cuenta en [render.com](https://render.com)
3. **New → Blueprint** → seleccionar el repositorio
4. Render detecta el `render.yaml` y crea automáticamente:
   - Servicio web (Django + Gunicorn)
   - Base de datos PostgreSQL gratuita
   - Variables de entorno (SECRET_KEY generada automáticamente)
5. Una vez desplegado, ejecutar en la consola de Render:
   ```bash
   python manage.py createsuperuser
   python manage.py seed_portfolio
   ```

### Variables de entorno en Render

| Variable | Descripción |
|---|---|
| `SECRET_KEY` | Generada automáticamente por Render |
| `DEBUG` | `False` (producción) |
| `ALLOWED_HOSTS` | `.onrender.com,localhost` |
| `DATABASE_URL` | Generada automáticamente desde la BD vinculada |

---

## Funcionalidades

- **Perfil Operativo** — Hero section con foto integrada en entorno holográfico
- **Neural Implants Tree** — Skills dinámicas desde BD, administrables via `/admin`
- **Data Shards** — Proyectos con badges de tecnologías, links a GitHub y fecha
- **Secure Uplink** — Formulario de contacto que persiste mensajes en PostgreSQL
- **Fondo Cyberpunk animado** — CSS puro: scanlines CRT, grilla holográfica pulsante y barrido de sensor
- **100% offline-ready** — Fuentes Space Grotesk y Material Symbols servidas localmente

---

## Buenas Prácticas Aplicadas

- **MVT** — Separación estricta de Modelos, Vistas y Templates
- **DRY** — `base.html` como plantilla madre heredada por todas las vistas
- **12-Factor App** — Configuración sensible en variables de entorno, nunca en código
- **WhiteNoise** — Servicio de archivos estáticos sin depender de nginx/S3
- **Property en modelo** — `tech_list` en `Project` encapsula la lógica de parseo del tech_stack
- **Fuentes locales** — Sin dependencia de CDN externo, funciona sin internet

---

## Reflexión Personal

> *¿Cómo crees que este portafolio contribuirá a tu inserción y proyección en la industria TI?*

Considero que este portafolio se convierte tanto en un catálogo de mis experiencias como en una demostración palpable e inmediata de capacidad técnica. Al implementar una infraestructura con un backend Django y PostgreSQL sólido bajo el capó —listo para escalar e integrarse con Docker u otras tecnologías en producción— y unirlo con una representación visual llamativa a nivel frontend, lograré dejar una huella memorable en los reclutadores.

En la industria TI actual —saturada de curriculums y plantillas HTML estáticas prefabricadas—, poseer una presentación técnica altamente temática que integra bases de datos reales manipulables desde un panel de administración, me posiciona de forma única. Me proyecta como un desarrollador íntegro: meticuloso al detalle en interfaz, pero lo suficientemente capaz y seguro para construir y gestionar soluciones lógicas completas en todo el ciclo de desarrollo backend/frontend.

---

## Licencia

MIT © 2025 Ciro Cortes — [github.com/CiroCortes](https://github.com/CiroCortes)
