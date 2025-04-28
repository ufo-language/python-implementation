def show_elems(stream, elems, open, sep, close):
    stream.write(open)
    first_iter = True
    for elem in elems:
        if first_iter:
            first_iter = False
        else:
            stream.write(sep)
        elem.show(stream)
    stream.write(close)
