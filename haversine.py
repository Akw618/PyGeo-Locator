from math import radians, sin, cos, sqrt, atan2

def haversine(lat1, lot1, lat2, lo2):
    """
    تحسب المسافة بين نقطتين جغرافيتين (latitude, longitude)
    بالكيلومترات باستخدام صيغة هافرسين
    """
    # نصف قطر الأرض بالكيلومترات
    R = 6371.0

    # تحويل الدرجات إلى راديان (لأن الدوال الرياضية بتشتغل بالراديان)
    lat1_rad = radians(lat1)
    lon1_rad = radians(lon1)
    lat2_rad = radians(lat2)
    lon2_rad = radians(lon2)

    # فرق الإحداثيات
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    # الصيغة الرياضية لهافرسين
    a = sin(dlat / 2)**2 + cos(lat1_rad) * cos(lat2_rad) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    distance = r * c