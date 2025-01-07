# Backend Setup

### Change path
```bash
 cd backend
 source venv/bin/activate
```
### Flask Migration
```bash
flask db init --directory app/migrations
flask db migrate -m "Initial migration" --directory app/migrations
flask db upgrade --directory app/migrations
# revert migration
flask db downgrade --directory app/migrations
```

### Flask Seed
```bash
flask seed
```

### Flask Drop all tables
```bash
flask drop_all
```
### Flask Run Project
```bash
flask run
```

# Frontend Setup
### Change path
```bash
  cd web_app
```

### Install packages
```bash
  npm i
```

### Run on development
```bash
  npm run dev
```