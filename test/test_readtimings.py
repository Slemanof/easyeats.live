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
        '11:00 - 11:00 (Út)', 'Út', {}) == {'Tuesday': '11:00-11:00'}, 'put_timings_standalone is bad with czech days of the week'


def test_sanitize_zomato_timings():
    assert readtimigs.satitize_zomato_timings(
        '11 AM to 11 PM (Mon-Fri)') == '11:00  11:00 (Mon-Fri)', 'sanitize_zomato_timings is bad'
    assert readtimigs.satitize_zomato_timings(
        '11 AM - 12 Midnight') == '11:00 - 24:00', 'sanitize_zomato_timings has a problem with Midnights'
    assert readtimigs.satitize_zomato_timings(
        '12 Noon - 6 PM') == '12:00 - 6:00', 'satitize_zomato_timings has problem with opening hours that conatin word Noon'
    assert readtimigs.satitize_zomato_timings(
        '10 AM to 7 PM') == '10:00  7:00', 'satitize_zomato_timings has a problem with removing word <<to>>'


def test_get_opening_hours():
    assert readtimigs.get_opening_hrs(
        '11:30 to 01:00 (Mon, Tue, Wed, Thu, Sun), 11:30 to 02:00 (Fri-Sat)') == '{"Monday": "11:30-01:00", "Tuesday": "11:30-01:00", "Wednesday": "11:30-01:00", "Thursday": "11:30-01:00", "Sunday": "11:30-01:00", "Friday": "11:30-02:00", "Saturday": "11:30-02:00"}', "The convertion to JSON is bad"
    assert readtimigs.get_opening_hrs(
        '11:00  - 12:00 (Mon-Sat), 11:00 - 12:00 (Sun)') == '{"Monday": "11:00-12:00", "Saturday": "11:00-12:00", "Tuesday": "11:00-12:00", "Wednesday": "11:00-12:00", "Thursday": "11:00-12:00", "Friday": "11:00-12:00", "Sunday": "11:00-12:00"}', "The convertion to JSON is bad"
