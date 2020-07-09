odoo.define('mail_reply_on_message.button', function (require) {
    "use strict";

    var ThreadWidget = require('mail.widget.Thread');
    var rpc = require('web.rpc');
    var core = require('web.core');
    var _t = core._t;

    ThreadWidget.include({
        events: _.extend({}, ThreadWidget.prototype.events, {
            'click .o_message_reply': '_onClickReply',
        }),
        _onClickReply: function (event) {
            var message_id = $(event.currentTarget).data('message-id');
            var self = this;
            rpc.query({
                model: 'mail.message',
                method: 'reply_context',
                args: [message_id],
            }).then(function (ctx) {
                var action = {
                    name: _t('Reply Message'),
                    type: 'ir.actions.act_window',
                    res_model: 'mail.compose.message',
                    view_mode: 'form',
                    view_type: 'form',
                    views: [[false, 'form']],
                    target: 'new',
                    context: ctx,
                };
                self.do_action(action, {
                    on_close: function () {
                        self.trigger_up('reload_mail_fields', {thread: true})
                    },
                }).then(self.trigger.bind(self, 'close_composer'));
            });
        },
    });
});