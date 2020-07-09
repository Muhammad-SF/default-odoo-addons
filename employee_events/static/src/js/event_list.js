odoo.define('employee_events.event_list', function (require) {
    "use strict";
    
    var FieldOne2Many = require('web.relational_fields').FieldOne2Many;
    var fieldRegistry = require('web.field_registry');
    var ListRenderer = require('web.ListRenderer');
    // Function ListRenderer_extnd    
    var ListRenderer_extnd = ListRenderer.extend({
        _renderRow: function (record, index) {
            var $row = this._super.apply(this, arguments);
            // Change on2many row's background colour based on event_type condition            
            if(record.data["event_type"]=='leave')
            {           
                this.$el.find('> table').removeClass('table-striped');     
                $row.addClass('events_leave');   
            }
            if(record.data["event_type"]=='calendar')
            {           
                this.$el.find('> table').removeClass('table-striped');     
                $row.addClass('events_calender');   
            }
            if(record.data["event_type"]=='activity')
            {           
                this.$el.find('> table').removeClass('table-striped');     
                $row.addClass('events_activity');   
            }            
            return $row;
        },
        
    });
    // Extending javascript one2many Render function 
    var EventListFieldOne2Many = FieldOne2Many.extend({        
        _getRenderer: function () {
            console.log("My Message inside");
            if (this.view.arch.tag === 'tree') {                
                //Calling python funtion default_events(hr.employee) using _rpc             
                this._rpc({
                    model: 'hr.employee',
                    method: 'default_events',
                    args: [this.res_id],
                }, {
                    shadow: true,
                });
                // Return ListRenderer_extnd
                return ListRenderer_extnd;
            }
            return this._super.apply(this, arguments);
        },
    });
    console.log("My Event List End!!!");
    fieldRegistry.add('Event_List_FieldOne2Many', EventListFieldOne2Many);
});