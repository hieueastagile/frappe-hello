// Copyright (c) 2017, iXSystem East Agile Team <ix@eastagile.com> and contributors
// For license information, please see license.txt

frappe.ui.form.on('FootballClub', {
	refresh: function(frm) {
	},
        country: function(frm, doctype, cdn) {
            frappe.call({
                method:"frappe_hello.api.get_continent",
                args: {
                    country: event.target.value
                },
                callback: function(r) {
                    frm.set_value('continent', r.message);
                }
            });
        }
});
