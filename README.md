# Solar Maintenance - Odoo Module

A custom Odoo module that extends maintenance requests with solar-specific fields for tracking plants, assets, equipment types, energy loss, and SCADA alarms.

## Prerequisites

- Docker & Docker Compose
- A modern web browser

## Quick Start

```bash
# Clone and start services
git clone <repo-url> && cd odoo-trial
docker compose up -d
```

Odoo will be available at **http://localhost:8069**.

## First-Time Database Setup

1. Open `http://localhost:8069` in your browser
2. Create a new database:
   - **Database Name**: e.g. `solar_db`
   - **Email**: your email
   - **Password**: your password
   - **Language**: select your preferred language
   - **Country**: optional
   - **Load demonstration data**: check this for testing
3. Click **Create database**

## Installing the Module

### Step 1 - Enable Developer Mode

Go to **Settings** (top-right gear icon) scroll to the bottom, and click **Activate the developer mode**.

The URL will change to include `?debug=1` and a bug icon will appear in the top-right menu.

### Step 2 - Update Apps List

Go to **Apps** menu. Click the **Updates** button (or **Update Apps List** in developer menu) to refresh the module list.

### Step 3 - Install the Module

Search for **Solar Maintenance** in the Apps list and click **Install**.

## Using the Module

1. Go to **Maintenance** app from the main dashboard
2. Create a new **Maintenance Request**
3. Fill in the solar-specific fields:
   - **Solar Plant** - name/identifier of the solar plant
   - **Solar Asset** - specific asset within the plant
   - **Equipment Type** - Inverter, PV Module, Transformer, Tracker, or Other
   - **Estimated Energy Loss (kWh)** - projected energy loss
   - **SCADA Alarm** - associated SCADA alarm reference
4. Save the request

## Docker Commands

### Start / Stop

```bash
docker compose up -d          # Start all services
docker compose down            # Stop all services
docker compose restart         # Restart all services
docker compose restart odoo    # Restart only Odoo (after code changes)
```

### Logs

```bash
docker compose logs -f         # Tail all logs
docker compose logs -f odoo    # Tail Odoo logs only
docker compose logs -f db      # Tail database logs only
```

### Rebuild

```bash
docker compose up -d --build   # Rebuild images and start
```

### Shell Access

```bash
docker compose exec odoo bash  # Shell into Odoo container
docker compose exec db psql -U odoo -d postgres  # Access PostgreSQL
```

### Database Management

```bash
# Create a backup
docker compose exec db pg_dump -U odoo <database_name> > backup.sql

# Restore from backup
cat backup.sql | docker compose exec -T db psql -U odoo -d <database_name>

# Drop and recreate a database
docker compose exec db dropdb -U odoo <database_name>
docker compose exec db createdb -U odoo -d <database_name>
```

## Project Structure

```
odoo-trial/
├── config/
│   └── odoo.conf                 # Odoo server configuration
├── custom_addons/
│   └── solar_maintenance/
│       ├── __init__.py
│       ├── __manifest__.py       # Module metadata and dependencies
│       ├── models/
│       │   ├── __init__.py
│       │   └── maintenance.py    # Extended maintenance.request model
│       ├── security/
│       │   └── ir.model.access.csv
│       └── views/
│           └── maintenance_views.xml
├── docker-compose.yml
└── README.md
```

## Troubleshooting

| Issue | Fix |
|---|---|
| Module not showing in Apps | Ensure developer mode is active, then click **Update Apps List** |
| Port 8069 already in use | Change the port mapping in `docker-compose.yml` under `odoo.ports` |
| Database connection error | Check that the `db` container is running: `docker compose ps` |
| Changes not reflected | Restart the Odoo container: `docker compose restart odoo` |
| Container fails to start | Check logs: `docker compose logs odoo` |
| Need a clean slate | `docker compose down -v` (deletes data volumes) then `docker compose up -d` |
