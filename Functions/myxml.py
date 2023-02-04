def myxml(tagname, content='', **kwargs):
    attrs = "".join(f' {k}="{v}"' for k, v in kwargs.items())
    output = f"<{tagname}{attrs}>{content}<\{tagname}>"
    return output

print(myxml("foo", "bar", a=1, b=2, c=3))