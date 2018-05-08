import variants
import pathlib

@variants.primary
def print_text(txt):
    """Prints any text passed to this function"""
    print(txt)


@print_text.variant('from_stream')
def print_text(sobj):
    """Read text from a stream and print it"""
    print_text(sobj.read())


@print_text.variant('from_filepath')
def print_text(*path_components):
    """Open the file specified by `path_components` and print the contents"""
    fpath = pathlib.Path(*path_components)
    with open(fpath, 'r') as f:
        print_text.from_stream(f)
