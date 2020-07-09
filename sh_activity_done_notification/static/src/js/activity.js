odoo.define('sh_notification.Activity', function (require) {
"use strict";
 	
	var mailUtils = require('mail.utils');
	var Activity = require('mail.Activity');
	var ActivityRenderer = require('mail.ActivityRenderer');
	var AbstractField = require('web.AbstractField');
	var BasicModel = require('web.BasicModel');
	var core = require('web.core');
	var field_registry = require('web.field_registry');
	var time = require('web.time');
	
	var QWeb = core.qweb;
	var _t = core._t;
	var setDelayLabel = function (activities){
	
	    var today = moment().startOf('day');
	    _.each(activities, function (activity){
	        var toDisplay = '';
	        var diff = activity.date_deadline.diff(today, 'days', true); // true means no rounding
	        if (diff === 0){
	            toDisplay = _t("Today");
	        } else {
	            if (diff < 0){ // overdue
	                if (diff === -1){
	                    toDisplay = _t("Yesterday");
	                } else {
	                    toDisplay = _.str.sprintf(_t("%d days overdue"), Math.abs(diff));
	                }
	            } else { // due
	                if (diff === 1){
	                    toDisplay = _t("Tomorrow");
	                } else {
	                    toDisplay = _.str.sprintf(_t("Due in %d days"), Math.abs(diff));
	                }
	            }
	        }
	        if(activity.is_done_activity){
	        	toDisplay = _t("Activity Done.");
	        	
	        }
	        activity.label_delay = toDisplay;
	    });
	    return activities;
	};
	
	
	Activity.include({
		
		 _render: function () {
			
		        _.each(this._activities, function (activity) {
		            var note = mailUtils.parseAndTransform(activity.note || '', mailUtils.inline);
		            var is_blank = (/^\s*$/).test(note);
		            if (!is_blank) {
		                activity.note = mailUtils.parseAndTransform(activity.note, mailUtils.addLink);
		            } else {
		                activity.note = '';
		            }
		        });
		        var activities = setDelayLabel(this._activities);
		        if (activities.length) {
		            var nbActivities = _.countBy(activities, 'state');
		            this.$el.html(QWeb.render('mail.activity_items', {
		                activities: activities,
		                nbPlannedActivities: nbActivities.planned,
		                nbTodayActivities: nbActivities.today,
		                nbOverdueActivities: nbActivities.overdue,
		                dateFormat: time.getLangDateFormat(),
		                datetimeFormat: time.getLangDatetimeFormat(),
		            }));
		        } else {
		            this.$el.empty();
		        }
		    },
	
	});
	
	
	ActivityRenderer.include({
		
		_renderRow: function (data) {
	        var self = this;
	        var res_id = data[0];
	        var name = data[1];
	        var $nameTD = $('<td>')
	            .addClass("o_res_name_cell")
	            .html(name)
	            .data('res-id', res_id);
	        var $cells = _.map(this.state.data.activity_types, function (node) {
	            var $td = $('<td>').addClass("o_activity_summary_cell");
	            var activity_type_id = node[0];
	            var activity_group = self.state.data.grouped_activities[res_id][activity_type_id];
	            activity_group = activity_group || {count: 0, ids: [], state: false};
	            if (activity_group.state) {
	                $td.addClass(activity_group.state);
	            }
	            // we need to create a fake record in order to instanciate the KanbanActivity
	            // this is the minimal information in order to make it work
	            // AAB: move this to a function
	            var record = {
	                data: {
	                    activity_ids: {
	                        model: 'mail.activity',
	                        res_ids: activity_group.ids,
	                    },
	                    activity_state: activity_group.state,
	                },
	                fields: {
	                    activity_ids: {},
	                    activity_state: {
	                        selection: [
	                            ['overdue', _t("Overdue")],
	                            ['today', _t("Today")],
	                            ['planned', _t("Planned")],
	                            ['done', _t("Done")],
	                        ],
	                    },
	                },
	                fieldsInfo: {},
	                model: self.state.data.model,
	                ref: res_id, // not necessary, i think
	                type: 'record',
	                res_id: res_id,
	                getContext: function () {
	                    return {}; // session.user_context
	                },
	                //todo intercept event or changes on record to update view
	            };
	            var KanbanActivity = field_registry.get('kanban_activity');
	            var widget = new KanbanActivity(self, "activity_ids", record, {});
	            widget.appendTo($td);
	            // replace clock by closest deadline
	            var $date = $('<div>');
	            var formated_date = moment(activity_group.o_closest_deadline).format('ll');
	            var current_year = (new Date()).getFullYear();
	            if (formated_date.endsWith(current_year)) { // Dummy logic to remove year (only if current year), we will maybe need to improve it
	                formated_date = formated_date.slice(0, -4);
	                formated_date = formated_date.replace(/( |,)*$/g, "");
	            }
	            $date
	                .text(formated_date)
	                .addClass('o_closest_deadline');
	            $td.find('a')
	                .empty()
	                .append($date);
	            return $td;
	        });
	        var $tr = $('<tr/>', {class: 'o_data_row'})
	            .append($nameTD)
	            .append($cells);
	        return $tr;
	    },
		
	});
	
});