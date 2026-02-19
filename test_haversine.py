from math_utils import haversine

def test_haversine_same_point():
    # نفس النقطة → المسافة لازم تكون صفر
    dist = haversine(30.0444, 31.2357, 30.0444, 31.2357)  # القاهرة لنفسها
    assert abs(dist) < 0.001, "المسافة بين نفس النقطة لازم تكون قريبة من صفر"

def test_haversine_cairo_to_alex():
    # القاهرة إلى الإسكندرية – مسافة جوية تقريبًا 180 كم
    dist = haversine(30.0444, 31.2357, 31.2001, 29.9187)
    assert 175 <= dist <= 185, f"المسافة الجوية المتوقعة حوالي 180 كم، لكن طلعت {dist}"

def test_haversine_negative_values():
    # إحداثيات سالبة (نصف الكرة الجنوبي)
    dist = haversine(-33.8688, 151.2093, -27.4698, 153.0251)  # سيدني إلى بريسبان
    assert 700 <= dist <= 800, f"المسافة المتوقعة حوالي 730 كم، لكن طلعت {dist}"

def test_haversine_very_large_distance():
    # من القطب الشمالي للقطب الجنوبي تقريبًا (نصف محيط الأرض)
    dist = haversine(90.0, 0.0, -90.0, 0.0)
    assert 19900 <= dist <= 20100, f"متوقع حوالي 20000 كم، لكن {dist}"