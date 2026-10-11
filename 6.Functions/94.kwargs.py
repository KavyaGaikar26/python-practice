def student_info(**kwargs):

    if len(kwargs) == 0:
        return "No information provided."

    for key, value in kwargs.items():
        print(key, ":", value)


student_info(
    name="Kavya",
    age=19,
    course="Computer Science",
    college="SST"
)