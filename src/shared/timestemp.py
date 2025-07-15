from datetime import date, datetime, time, timedelta, timezone

def get_timestamp() -> datetime:
  return datetime.now(timezone.utc)
def get_date() -> date:
  return get_timestamp().date()
def get_time()-> time:
  return get_timestamp().time()