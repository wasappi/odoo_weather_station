import requests
from odoo import http, fields
from odoo.http import request
from datetime import timedelta

def format_since(measure_dt):
    if not measure_dt:
        return None
    now_utc = fields.Datetime.now()
    now_user = fields.Datetime.context_timestamp(request.env.user, now_utc)
    measure_user = fields.Datetime.context_timestamp(request.env.user, measure_dt)
    delta_seconds = int((now_user - measure_user).total_seconds())
    if delta_seconds <= 60:
        return "just now"
    minutes = delta_seconds // 60
    if minutes < 60:
        return f"{minutes} minute{'s' if minutes != 1 else ''} ago"
    hours = minutes // 60
    if hours < 24:
        return f"{hours} hour{'s' if hours != 1 else ''} ago"
    days = hours // 24
    return f"{days} day{'s' if days != 1 else ''} ago"