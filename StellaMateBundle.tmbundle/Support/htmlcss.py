style = '''
    .container {
        border-bottom: 1px solid lightgray;
    }
    .bigtitle {
        font-size: 20px;
    }
    .linkmsg, .othermsg {
        background: lavender;
        border: 1px solid lightgray;
        border-bottom: 0;
        padding:20px;
    }
    a {
        color: navy;
        text-decoration: none;
    }'''

header = '''<html><head><style>%s</style></head>
    <body><h1 class="bigtitle">%s</h1><div class="container">'''

linkmsg = '''<div class="linkmsg">
    <a href="txmt://open?url=file://%s&line=%s">%s</a></div>'''

othermsg = '<div class="othermsg"><span>%s</span></div>'

footer = '</div></body></html>'
