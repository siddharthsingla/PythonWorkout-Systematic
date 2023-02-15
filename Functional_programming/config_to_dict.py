def config_to_dict(filename):
    return {line.split("=")[0]: line.split("=")[1] for line in open(filename)}


"""Create a dict based on the config file, as in the previous exercise, but this time,
all of the values should be integers. This means that you’ll need to filter out
(and ignore) those values that can’t be turned into integers"""


def config_to_dict(filename):
    return {line.split("=")[0]: int(line.split("=")[1].strip()) for line in open(filename) if line.split("=")[1].strip().isdigit()}
