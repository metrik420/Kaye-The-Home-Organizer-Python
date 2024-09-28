from flask import Blueprint, render_template, jsonify, request
from app.models import CalendarEvent
from app.extensions import db
from app.forms import EventForm
from datetime import datetime

calendar_bp = Blueprint('calendar', __name__, template_folder='../templates')

@calendar_bp.route('/calendar', methods=['GET', 'POST'])
def manage_calendar():
    form = EventForm()
    if form.validate_on_submit():
        event = CalendarEvent(
            title=form.title.data,
            start_time=form.start_time.data,
            end_time=form.end_time.data,
            description=form.description.data
        )
        db.session.add(event)
        db.session.commit()
        flash('Event added successfully.')
        return redirect(url_for('calendar.manage_calendar'))
    
    events = CalendarEvent.query.all()
    return render_template('calendar.html', form=form, events=events)

@calendar_bp.route('/get-events-for-today', methods=['GET'])
def get_events_for_today():
    today = datetime.now().date()
    tomorrow = today + timedelta(days=1)
    events = CalendarEvent.query.filter(CalendarEvent.start_time >= today, CalendarEvent.start_time < tomorrow).all()
    
    return jsonify([{
        'title': event.title,
        'start_time': event.start_time.isoformat(),
        'end_time': event.end_time.isoformat() if event.end_time else None,
        'description': event.description
    } for event in events])
