#!/usr/bin/env python3

from app.ioc import injector
from app.types import AppRunner

injector.get(AppRunner)()
