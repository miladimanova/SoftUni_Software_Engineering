number_of_pages_in_the_current_book = int(input())
pages_to_read_per_hour = int(input())
days_to_finish_the_book = int(input())

total_reading_time_for_the_book = number_of_pages_in_the_current_book // pages_to_read_per_hour
reading_hours_per_day = total_reading_time_for_the_book // days_to_finish_the_book
print(reading_hours_per_day)