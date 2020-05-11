import readtimigs


def test_findtime():
    assert readtimigs.findtime(
        "12:00 - 18:00") == "12:00-18:00", "Time conversion method is bad"
    assert readtimigs.findtime(
        "16:00 - 1:00") == "16:00-1:00", "Time conversion method is bad"


def test_put_timings_order():
    assert readtimigs.put_timings_order('11:30 to 01:00 (Mon, Tue, Wed, Thu, Sun)', ['Mon', 'Tue', 'Wed', 'Thu', 'Sun'], {}) == {
        'Monday': '11:30-01:00', 'Tuesday': '11:30-01:00', 'Wednesday': '11:30-01:00', 'Thursday': '11:30-01:00', 'Sunday': '11:30-01:00'}, 'put_timings_order is bad'
    assert readtimigs.put_timings_order('1:00 - 11:00 (Po, Pá)', ['Po', 'Pá'], {}) == {
        'Monday': '1:00-11:00', 'Friday': '1:00-11:00'}, 'put_timings_order is bad'


def test_put_timings_interval():
    assert readtimigs.put_timings_interval('11:30 AM to 11:30 PM (Mon-Fri)', 'Mon-Fri', {}) == {
        'Monday': '11:30-11:30', 'Tuesday': '11:30-11:30', 'Wednesday': '11:30-11:30', 'Thursday': '11:30-11:30', 'Friday': '11:30-11:30'}, 'put_timings_interval is bad'
    assert readtimigs.put_timings_interval('11:00 - 11:00 (Po-Pá)', 'Po-Pá', {}) == {
        'Monday': '11:00-11:00', 'Tuesday': '11:00-11:00', 'Wednesday': '11:00-11:00', 'Thursday': '11:00-11:00', 'Friday': '11:00-11:00'}, 'put_timings_interval is working incorrectly with czech days of the week'


def test_put_timings_standalone():
    assert readtimigs.put_timings_standalone(
        '11:00 - 11:00 (Mon)', 'Mon', {}) == {'Monday': '11:00-11:00'}, 'put_timings_standalone is bad'
    assert readtimigs.put_timings_standalone(
        '11:00 - 11:00 (Út)', 'Út', {}) == {'Tuesday': '11:00-11:00'}
