num = int(input("Please type number: "))
if 1 =< num < int(1e6):
    from fizzbuzz_imports.mil1 import fizzbuzz
elif int(1e6) =< num < int(2e6):
    from fizzbuzz_imports.mil2 import fizzbuzz
elif int(2e6) =< num < int(3e6):
    from fizzbuzz_imports.mil3 import fizzbuzz
elif int(3e6) =< num < int(4e6):
    from fizzbuzz_imports.mil4 import fizzbuzz
elif int(4e6) =< num < int(5e6):
    from fizzbuzz_imports.mil5 import fizzbuzz
elif int(5e6) =< num < int(6e6):
    from fizzbuzz_imports.mil6 import fizzbuzz
elif int(6e6) =< num < int(7e6):
    from fizzbuzz_imports.mil7 import fizzbuzz
elif int(7e6) =< num < int(8e6):
    from fizzbuzz_imports.mil8 import fizzbuzz
elif int(8e6) =< num < int(9e6):
    from fizzbuzz_imports.mil9 import fizzbuzz
elif int(9e6) =< num < int(10e6):
    from fizzbuzz_imports.mil10 import fizzbuzz
else:
    raise Exception("Number not supported")
fizzbuzz(num)