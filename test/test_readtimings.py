import readtimigs


def test_findtime():
    assert readtimigs.findtime(
        "12:00 - 18:00") == "12:00-18:00", "Time conversion method is bad"
    assert readtimigs.findtime(
        "16:00 - 1:00") == "16:00-1:00", "Time conversion method is bad"


def test_put_timings_order():
    assert readtimigs.put_timings_order('11:30 to 01:00 (Mon, Tue, Wed, Thu, Sun)', ['Mon', 'Tue', 'Wed', 'Thu', 'Sun'], {}) == {
        'Monday': '11:30-01:00', 'Tuesday': '11:30-01:00', 'Wednesday': '11:30-01:00', 'Thursday': '11:30-01:00', 'Sunday': '11:30-01:00'}, 'Function for putting time separated by coma is bad'
    assert readtimigs.put_timings_order('11:00 - 11:00 (Po, Pá)', ['Po', 'Pá'], {}) == {
        'Monday': '11:00-11:00', 'Friday': '11:00-11:00'}, 'Function for putting time separated by coma is bad'
