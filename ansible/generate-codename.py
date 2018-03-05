#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from faker import Faker
fake = Faker()
print("{}-{}{}".format(fake.safe_color_name(), fake.day_of_month(), fake.day_of_month()), end="")
