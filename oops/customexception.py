
class Error(Exception):
    pass
class dobException(Error):
    pass

year =int(input("enter the year of birth: "))
age  =2021-year

try:
    if age<=30 & age>20:
        print("The age is valid. you can apply for the exams")
    else:
        raise dobException
except dobException:
    print("The year age is not within the range.you cannot apply for this job")
        