# Esquema de la Base de Datos del Proyecto

## Tablas Principales

### 1. Usuarios (`users`)

Tabla para almacenar información sobre los usuarios.

- `id`: UUID, clave primaria
- `email`: String, único, requerido
- `hashed_password`: String, requerido
- `is_active`: Boolean, requerido
- `profile_image_url`: String, opcional
- `google_id`: String, opcional
- `facebook_id`: String, opcional
- `github_id`: String, opcional
- `first_name`: String, opcional
- `last_name`: String, opcional
- `bio`: Text, opcional
- `location`: String, opcional
- `website`: String, opcional
- `date_of_birth`: Date, opcional
- `language`: String, opcional
- `timezone`: String, opcional
- `notifications_enabled`: Boolean, opcional
- `created_at`: DateTime
- `updated_at`: DateTime, null
- `deleted_at`: DateTime, null

---

### 2. Proyectos (`projects`)

Tabla para almacenar proyectos, que son contenedores de tareas.

- `id`: UUID, clave primaria
- `name`: String, requerido
- `description`: Text, opcional
- `is_public`: Boolean, requerido
- `is_active`: Boolean, requerido
- `owner_id`: UUID, clave foránea (`users.id`)
- `created_at`: DateTime
- `updated_at`: DateTime, null
- `deleted_at`: DateTime, null

---

### 3. Tareas (`tasks`)

Tabla para almacenar tareas individuales que pertenecen a un proyecto.

- `id`: UUID, clave primaria
- `title`: String, requerido
- `description`: Text, opcional
- `status_id`: UUID, clave foránea (`statuses.id`)
- `project_id`: UUID, clave foránea (`projects.id`)
- `parent_id`: UUID, clave foránea (`tasks.id`), opcional (para sub-tareas)
- `priority`: Integer, opcional (clave foránea de `project_priorities.priority_level`)
- `due_date`: DateTime, opcional
- `created_at`: DateTime
- `updated_at`: DateTime, null
- `deleted_at`: DateTime, null

---

### 4. Etiquetas (`labels`)

Tabla para almacenar etiquetas que se pueden asignar a tareas.

- `id`: UUID, clave primaria
- `name`: String, requerido
- `color_code`: String (formato hexadecimal)
- `visibility`: String (Privada, Pública)
- `created_at`: DateTime
- `updated_at`: DateTime, null
- `deleted_at`: DateTime, null

---

### 5. Estados (`statuses`)

Tabla para almacenar estados posibles para las tareas.

- `id`: UUID, clave primaria
- `name`: String, requerido
- `color_code`: String (formato hexadecimal)
- `display_order`: Integer (para ordenar los estados en la UI)
- `created_at`: DateTime
- `updated_at`: DateTime, null
- `deleted_at`: DateTime, null

---

### 6. Categorías (`categories`)

Tabla para categorizar proyectos.

- `id`: UUID, clave primaria
- `name`: String, requerido
- `created_at`: DateTime
- `updated_at`: DateTime, null
- `deleted_at`: DateTime, null

---

### 7. Archivos Adjuntos (`attachments`)

Tabla para almacenar archivos que se pueden vincular a tareas y proyectos.

- `id`: UUID, clave primaria
- `file_path`: String, requerido
- `file_name`: String, requerido
- `task_id`: UUID, clave foránea (`tasks.id`), opcional
- `project_id`: UUID, clave foránea (`projects.id`), opcional
- `created_at`: DateTime
- `updated_at`: DateTime, null
- `deleted_at`: DateTime, null

---

## Tablas de Relación

### 8. Proyectos y Categorías (`project_categories`)

Tabla de relación entre proyectos y categorías.

- `project_id`: UUID, clave foránea (`projects.id`)
- `category_id`: UUID, clave foránea (`categories.id`)
- `created_at`: DateTime
- `updated_at`: DateTime, null
- `deleted_at`: DateTime, null

---

### 9. Prioridades de Proyectos (`project_priorities`)

Tabla para definir prioridades de tareas a nivel de proyecto.

- `project_id`: UUID, clave foránea (`projects.id`)
- `priority_level`: Integer
- `display_text`: String, opcional
- `created_at`: DateTime
- `updated_at`: DateTime, null
- `deleted_at`: DateTime, null

---

## Tabla de Auditoría (`audit_log`)

Tabla para capturar eventos importantes en la aplicación.

- `id`: UUID, clave primaria
- `user_id`: UUID, clave foránea (`users.id`)
- `action`: String
- `entity_type`: String
- `entity_id`: UUID
- `changed_fields`: Text
- `timestamp`: DateTime

