# -*- coding: utf-8 -*-
# Copyright (c) 2017, iXSystem East Agile Team <ix@eastagile.com> and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class FootballPlayer(Document):
        def validate(self):
                if len(self.position.split(',')) > 5:
                        frappe.throw(_('A player can not play that much positions'))
