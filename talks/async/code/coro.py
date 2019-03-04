def this_is_sort_of_a_coroutine():
    print("running")
    name = yield
    while True:
        name = yield f"hello {name}"
        if name is None:
            break
        print(f"hello {name}")
