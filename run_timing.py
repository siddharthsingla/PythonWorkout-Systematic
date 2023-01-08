def run_timing():
    run_time = []
    while True:
        temp = input("Enter 10KM run time: ")
        if not temp:
            return sum(run_time)/len(run_time)
        run_time.append(int(temp))

def run_timingv2():
    no_of_runs = 0
    total_time = 0
    while True:
        temp = input("Enter 10kn runtimeL ")
        if not temp:
            break
        total_time += float(temp)
        no_of_runs += 1
    print(f"average run time is {total_time/no_of_runs}")
run_timingv2()