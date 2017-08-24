import urllib, base64

from io import BytesIO

from IPython.display import HTML, display

def fig_to_uri(fig):
    buf = BytesIO()
    fig.savefig(buf, format='png')

    buf.seek(0)
    b64str = base64.b64encode(buf.read())

    return b64str


def fig_to_html(fig, style=None):
    b64str = fig_to_uri(fig)
    data_uri = "data:image/png;base64," + urllib.parse.quote(b64str)

    img_fmt = '<img src={}'
    if style is not None:
        img_fmt += ' style="{}"'.format(style)

    img_fmt += '>'
    return img_fmt.format(data_uri)


def display_figures(*figs):
    out_html_fmt = '<div class="output_png" style="text-align: center; display: block; width: 100%">{}<div style="clear: both;"/></div>'

    div_html = '<div style="display: inline-block; float:left; text-align: center; width: {}">{{}}</div>'
    div_html = div_html.format(str(98 // len(figs)) + '%')

    img_htmls = ''.join(div_html.format(fig_to_html(fig)) for fig in figs)

    html_out = out_html_fmt.format(img_htmls)

    display(HTML(html_out))
