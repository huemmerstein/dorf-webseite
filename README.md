# dorf-webseite

Flask-Anwendung für eine Dorf-Webseite mit PostgreSQL, News-RSS, Veranstaltungen mit ICS-Export, Flurnamen, Pinwand und Kartenansicht.

## Entwicklung

```bash
pip install -r requirements.txt
flask --app run run --debug
```

Die Datenbank wird über die Umgebungsvariable `DATABASE_URL` konfiguriert (Standard: `postgresql://postgres:postgres@localhost:5432/dorfwebseite`).

## Administration

Hinweise zur Verwaltung der Inhalte finden sich in [ADMIN.md](ADMIN.md).
