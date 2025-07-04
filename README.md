# Veterinaria ERP API

Este proyecto implementa una API básica para la gestión de una veterinaria usando **Django** y **Django REST Framework**.

## Instalación local

```bash
pip install -r requirements.txt
cd vet_erp
python manage.py migrate
python manage.py runserver
```

## Uso con Docker

```bash
docker build -t vet_erp .
docker run -p 8000:8000 vet_erp
```

La API expone endpoints agrupados por módulos:

- `/api/clients/` – dueños y mascotas
- `/api/appointments/` – citas
- `/api/inventory/` – productos en inventario
- `/api/billing/` – facturación
