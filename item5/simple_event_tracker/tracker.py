class Tracker:
  def __init__(self):
    self.events = {}

  def add_event(self, event_name, time):
    if time not in self.events:
      self.events[time] = event_name

  def delete_event(self, event_name):
    delete = False
    for time in self.events:
      if self.events[time] == event_name:
        delete = True
        time_to_delete = time
    if delete:
      del self.events[time_to_delete]

  def get_event_time(self, event_name):
    for time in self.events:
      if self.events[time] == event_name:
        return time
    return None

  def fetch_soonest_event(self):
    if (self.events.keys()):
      soonest_time = min(self.events.keys())
      return self.events[soonest_time]
    return None
    