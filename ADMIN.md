# Anleitung für Administratoren

Diese Anleitung erklärt, wie Sie Inhalte der Dorf-Webseite verwalten. Alle Beispiele gehen davon aus, dass die Anwendung lokal läuft und die PostgreSQL-Datenbank erreichbar ist.

## Vorbereitung

1. Abhängigkeiten installieren und Anwendung starten:
   ```bash
   pip install -r requirements.txt
   flask --app run run
   ```
2. Für die Arbeit mit den Daten `flask shell` öffnen:
   ```bash
   flask --app run shell
   ```
   Dort stehen die Datenbankobjekte aus `app.models` zur Verfügung.

## News verwalten

```python
from app.models import db, News, User
# neuen Beitrag anlegen
autor = User.query.first()
beitrag = News(title="Titel", body="Text", author=autor)
db.session.add(beitrag)
db.session.commit()
# vorhandenen Beitrag bearbeiten
beitrag = News.query.get(1)
beitrag.title = "Neuer Titel"
db.session.commit()
```

## Veranstaltungen

```python
from app.models import db, Event
# neues Event erstellen
termin = Event(title="Dorffest", start=datetime(2024, 6, 1, 18), end=datetime(2024, 6, 1, 23))
db.session.add(termin)
db.session.commit()
# Event löschen
termin = Event.query.get(1)
db.session.delete(termin)
db.session.commit()
```

## Flurnamen

```python
from app.models import db, Flurname
f = Flurname(name="Bergwiese", erklaerung="Lage am Südhang")
db.session.add(f)
db.session.commit()
```

## Pinwand

```python
from app.models import db, PinboardPost
p = PinboardPost(title="Suche Fahrrad", body="Bitte melden")
db.session.add(p)
db.session.commit()
```

## Statische Seiten

Seiten wie Impressum oder Geschichte werden als `Page` gespeichert. Der Zugriff erfolgt über den Slug.

```python
from app.models import db, Page
seite = Page(slug="geschichte", title="Geschichte des Ortes", body="...")
db.session.add(seite)
db.session.commit()
```

Zum Bearbeiten den gewünschten Datensatz laden, Attribute ändern und `db.session.commit()` aufrufen.

## Hinweise

- Nach Änderungen an den Tabellen ist ein Neustart der Anwendung erforderlich.
- Für den produktiven Betrieb empfiehlt sich ein komfortableres Admin-Interface wie [Flask-Admin](https://flask-admin.readthedocs.io/).
