from tracker import Tracker

def test_add_event():
  tracker = Tracker()
  tracker.add_event('Buy toothpaste', 1800)
  assert tracker.get_event_time('Buy toothpaste') == 1800

def test_delete_event():
  tracker = Tracker()
  tracker.add_event('Buy toothpaste', 1900)
  tracker.add_event('Go to the gym', 2000)
  tracker.delete_event('Go to the gym')
  assert tracker.get_event_time('Go to the gym') == None
  assert tracker.get_event_time('Buy toothpaste') == 1900

def test_fetch_soonest_event():
  tracker = Tracker()
  tracker.add_event('Buy snacks', 700)
  tracker.add_event('Go shopping', 1200)
  tracker.add_event('Eat something', 900)
  assert tracker.fetch_soonest_event() == 'Buy snacks'
  tracker.delete_event('Buy snacks')
  assert tracker.fetch_soonest_event() == 'Eat something'
  tracker.delete_event('Go shopping')
  tracker.delete_event('Eat something')
  assert tracker.fetch_soonest_event() == None
