#!/usr/bin/env python3

from app import injector
from app.util.types import AppRunner

injector.get(AppRunner)()
