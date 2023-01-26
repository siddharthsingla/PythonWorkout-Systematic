"""From /etc/passwd, create a dict in which the keys are the usernames (as in the
main exercise) and the values are themselves dicts with keys (and appropriate
values) for user ID, home directory, and shell."""

def passwd_to_dict(filename):
    output = {}
    for line in open(filename):
        if not line.startswith(("#", '\n')):
            fields = line.strip().split(":")
            output[fields[0]] = {"uid": fields[2], "home_dir": fields[5], "shell": fields[-1]}
    return output