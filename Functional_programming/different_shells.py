def different_shells():
    print({line.strip().split(':')[-1] for line in open('/etc/passwd') if not line.startswith(('#', '\n'))})

different_shells()