# -*- coding: utf-8 -*-

from noteDB import NoteDB
from Dashboard import Dashboard

db=NoteDB(username="root",password="")
Dashboard().initUI(db)
   