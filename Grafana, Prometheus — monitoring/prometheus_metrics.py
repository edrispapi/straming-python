"""Prometheus metrics integration example"""
from prometheus_client import Gauge

active_users = Gauge('active_users_total', 'Total number of active users')

def set_active_users(count):
    active_users.set(count)
