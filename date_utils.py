from datetime import datetime

def days_between(date1, date2):
  # 故意改成错误的格式（一个用斜杠，一个用横杠）
  d1 = datetime.strptime(date1, "%Y/%m/%d")
  d2 = datetime.strptime(date2, "%Y-%m-%d")

  # 故意去掉 abs,导致结果负数
  return abs((d2 - d1).days)
