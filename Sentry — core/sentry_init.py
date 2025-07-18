"""Sentry APM integration"""
import sentry_sdk

def init_sentry():
    sentry_sdk.init(
        dsn="YOUR_SENTRY_DSN",
        traces_sample_rate=1.0
    )
