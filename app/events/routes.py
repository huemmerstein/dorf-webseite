from flask import Blueprint, render_template, Response
from icalendar import Calendar, Event as ICalEvent

from ..models import Event

bp = Blueprint('events', __name__, url_prefix='/events')


@bp.route('/')
def index():
    events = Event.query.order_by(Event.start).all()
    return render_template('events/index.html', events=events)


@bp.route('/ics')
def ics():
    cal = Calendar()
    cal.add('prodid', '-//Dorf Events//')
    cal.add('version', '2.0')
    for event in Event.query.all():
        ical_event = ICalEvent()
        ical_event.add('summary', event.title)
        ical_event.add('dtstart', event.start)
        if event.end:
            ical_event.add('dtend', event.end)
        ical_event.add('description', event.description)
        cal.add_component(ical_event)
    return Response(cal.to_ical(), mimetype='text/calendar')
