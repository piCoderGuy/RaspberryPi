from dateutil import parser
start = '9/30/2025 1:30PM'
end = '9/30/2025 2:00 PM'

start_date = parser.parse(start)
end_date = parser.parse(end)
type(start_date)
print((end_date-start_date).total_seconds())
