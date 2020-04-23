fn1 = lambda a, b: a + b
print(fn1(12, 2))

fn2 = lambda a, b: a if a > b else b
print(fn2(12, 43))

students = [{"name": "tom", "age": 12},
            {"name": "gyt", "age": 34},
            {"name": "hu", "age": 20}]

students.sort(key=lambda x: x["name"],reverse=True)
print(students)
