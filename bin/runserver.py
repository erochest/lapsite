#!/usr/bin/env python


from lapsite import create_app

app = create_app()
app.run(host='0.0.0.0')

