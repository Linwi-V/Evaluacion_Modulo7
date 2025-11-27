# Gestor de Productos - Django Framework

Sistema de gestión de productos desarrollado con Django que permite a los usuarios administrar productos, categorías, etiquetas y sus detalles de manera eficiente y organizada.

## Descripción del Proyecto

Este proyecto forma parte del portafolio del Módulo 7 del Bootcamp Desarrollo Full Stack de Python. Permite crear, visualizar, editar y eliminar productos, gestionando sus categorías, etiquetas y detalles. Se implementan funcionalidades completas de CRUD, validación de formularios y navegación con templates heredados, siguiendo las buenas prácticas del framework Django.

## Características Principales

### Funcionalidades Implementadas

#### Gestión de Productos

* Crear nuevos productos con nombre, descripción, precio, categoría y etiquetas.
* Visualizar lista completa de productos con tabla y etiquetas destacadas.
* Ver detalle de cada producto con sus detalles asociados (dimensiones y peso).
* Editar productos existentes.
* Eliminar productos con confirmación.

#### Gestión de Categorías y Etiquetas

* Crear, editar y eliminar categorías.
* Crear, editar y eliminar etiquetas.
* Listado de categorías y etiquetas con sistema de herencia de templates.

#### Seguridad y Validación

* Validación de datos mediante Django Forms.
* Tokens CSRF en todos los formularios.
* Protección de URLs mediante `get_object_or_404` para productos inexistentes.
* Validación de datos de formularios y mensajes de error visibles al usuario.

#### Panel de Administración

* Panel admin de Django configurado y funcional.
* Gestión de productos, categorías, etiquetas y detalles desde el admin.

#### Interfaz de Usuario

* Diseño responsivo con Bootstrap 5.3.
* Navegación intuitiva mediante navbar.
* Feedback visual en formularios y listas de productos.
* Plantillas con herencia para evitar duplicación de código.

## Tecnologías Utilizadas

* Python 3.12
* Django 5.2.7
* Bootstrap 5.3 (CDN)
* PostgreSQL
* HTML5 / CSS3
* Git / GitHub

## Arquitectura del Proyecto

El proyecto sigue el patrón MVT (Model-View-Template) de Django:

* **Models:** Definición de Producto, Detalle, Categoria y Etiqueta.
* **Views:** Lógica para CRUD de productos, categorías y etiquetas.
* **Templates:** Interfaces HTML dinámicas con herencia de `base.html`.
* **Forms:** Validación y procesamiento de datos de los productos.
* **Admin:** Configuración y personalización del panel de administración.

## Requisitos Previos

* Python 3.8 o superior
* pip (gestor de paquetes de Python)
* Git

## Instalación y Configuración

1. Clonar el repositorio:

<pre class="overflow-visible!" data-start="2874" data-end="2977"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"></div></pre>

<pre class="overflow-visible!" data-start="2874" data-end="2977"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>git </span><span>clone</span><span> https://github.com/Linwi-V/Evaluacion_Modulo7.git
</span><span>cd</span><span> gestion_productos
</span></span></code></div></div></pre>

2. Crear y activar entorno virtual:

En Windows:

<pre class="overflow-visible!" data-start="3028" data-end="3081"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"></div></pre>

<pre class="overflow-visible!" data-start="3028" data-end="3081"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>python -m venv venv
venv\Scripts\activate
</span></span></code></div></div></pre>

En Mac/Linux:

<pre class="overflow-visible!" data-start="3097" data-end="3154"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"></div></pre>

<pre class="overflow-visible!" data-start="3097" data-end="3154"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>python3 -m venv venv
</span><span>source</span><span> venv/bin/activate
</span></span></code></div></div></pre>

3. Instalar dependencias:

<pre class="overflow-visible!" data-start="3182" data-end="3225"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"></div></pre>

<pre class="overflow-visible!" data-start="3182" data-end="3225"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>pip install -r requirements.txt
</span></span></code></div></div></pre>

4. Ejecutar migraciones:

<pre class="overflow-visible!" data-start="3252" data-end="3288"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"></div></pre>

<pre class="overflow-visible!" data-start="3252" data-end="3288"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>python manage.py migrate
</span></span></code></div></div></pre>

5. Crear superusuario para acceder al admin:

<pre class="overflow-visible!" data-start="3335" data-end="3379"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"></div></pre>

<pre class="overflow-visible!" data-start="3335" data-end="3379"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>python manage.py createsuperuser
</span></span></code></div></div></pre>

6. Ejecutar servidor de desarrollo:

<pre class="overflow-visible!" data-start="3417" data-end="3455"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"></div></pre>

<pre class="overflow-visible!" data-start="3417" data-end="3455"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>python manage.py runserver
</span></span></code></div></div></pre>

7. Acceder a la aplicación:

* Aplicación principal: [http://127.0.0.1:8000/]()

Panel de administración: [http://127.0.0.1:8000/admin/]()

## Estructura del Proyecto

<pre class="overflow-visible!" data-start="3684" data-end="4476"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"></div></pre>

<pre class="overflow-visible!" data-start="3684" data-end="4476"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>gestion_productos/
├── manage.py
├── requirements.txt
├── README.md
├── gestion_productos/           </span><span># Configuración del proyecto</span><span>
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── productos/                   </span><span># Aplicación principal</span><span>
    ├── models.py               </span><span># Modelos Producto, Categoria, Etiqueta, Detalle</span><span>
    ├── views.py                </span><span># Lógica de vistas CRUD</span><span>
    ├── urls.py                 </span><span># URLs de la aplicación</span><span>
    ├── forms.py                </span><span># Formularios Django</span><span>
    ├── admin.py                </span><span># Configuración del panel admin</span><span>
    └── templates/
        └── productos/
            ├── base.html
            ├── index.html
                ├── productos/
                   ├── lista.html
                   ├── crear.html
                   ├── detalle.html
                   ├── editar.html
                   └── eliminar.html
                ├── categorias/
                    ├── lista.html
                    ├── formulario.html
                    └── eliminar.html
                ├── etiquetas/
                    ├── lista.html
                    ├── formulario.html
                    └── eliminar.html
</span></span></code></div></div></pre>

## Funcionalidades Técnicas Implementadas

### Sistema de Plantillas Django

* Herencia de `base.html` para evitar duplicación.
* Bloques dinámicos para contenido principal.
* Integración con Bootstrap para diseño responsivo.

### Formularios Django

* `ProductoForm` y `DetalleForm` con validación integrada.
* Formularios con CSRF token y errores visibles.
* Validación automática de campos obligatorios.

### Panel de Administración

* Modelos registrados y personalización de listas.
* Gestión de productos, categorías, etiquetas y detalles desde admin.

### Seguridad Implementada

* Tokens CSRF en todos los formularios.
* Validación de formularios y manejo de errores.
* Uso de `get_object_or_404` para evitar errores 500.
* Control de acceso: solo usuarios logueados pueden crear o editar productos (si se implementa autenticación en futuro).

## Configuración para Producción

* `DEBUG = True` para desarrollo, debe cambiarse a `False` en producción.
* `ALLOWED_HOSTS` configurables.
* `SECRET_KEY` debe colocarse en variables de entorno para mayor seguridad.

## Aprendizajes Clave

* Arquitectura MVT de Django.
* Implementación completa de CRUD.
* Uso de Django Forms para validación.
* Integración de Bootstrap con Django.
* Manejo de relaciones FK y M2M.
* Panel admin personalizado.
* Buenas prácticas de documentación y control de versiones.

## Autor

Linwi Vargas - Productor de Videojuegos Junior

* GitHub: [@Linwi-V](https://github.com/Linwi-V)
* LinkedIn: Linwi Vargas Campos
* Itch.io: [linwi.itch.io](https://linwi.itch.io)

Proyecto desarrollado como parte del Bootcamp de Desarrollo Full Stack Python - Evaluación del Módulo 7.

## Licencia

Este proyecto es de uso educativo como parte del portafolio de aprendizaje.
