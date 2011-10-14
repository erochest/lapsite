#!/usr/bin/env python

import lapsite

lapsite.create_app()

import lapsite.models

lapsite.db.create_all()

