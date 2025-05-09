# subjects.py

def get_subjects(current_period):
    subjects = {
        'morning': ['dawn light', 'new possibilities', 'sleepy consciousness'],
        'afternoon': ['passing hours', 'shifting shadows', 'daily rhythms'],
        'evening': ['fading light', 'accumulated moments', 'day\'s impressions'],
        'night': ['starry silence', 'lonely hours', 'nocturnal musings']
    }
    return subjects.get(current_period, ['starry silence', 'lonely hours', 'nocturnal musings'])
