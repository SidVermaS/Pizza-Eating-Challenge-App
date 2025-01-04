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

