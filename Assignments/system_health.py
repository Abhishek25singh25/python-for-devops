import psutil

def check_cpu_threshold():
    cpu_threshold = int(input("Enter the CPU Threshold: "))
    disk_threshold = int(input("Enter the Disk Threshold: "))
    memory_threshold = int(input("Enter the Memory Threshold: "))

    current_cpu = psutil.cpu_percent(interval=1)
    current_disk = psutil.disk_usage('/').percent
    current_memory = psutil.virtual_memory().percent

    print("Current CPU %: ", current_cpu)
    print("Current Disk %: ", current_disk)
    print("Current Memory %: ", current_memory)

    if current_cpu > cpu_threshold:
        print("CPU Alert Email sent...")
    else:
        print("CPU in Safe state...")

    if current_disk > disk_threshold:
        print("Disk Alert Email sent...")
    else:
        print("Disk in Safe state...")

    if current_memory > memory_threshold:
        print("Memory Alert Email sent...")
    else:
        print("Memory in Safe state...")

check_cpu_threshold()