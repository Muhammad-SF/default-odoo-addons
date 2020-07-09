 odoo.define('badge_on_menu', function (require) {
    'use strict';
    
    var Menu = require('web.Menu');
    var core = require('web.core');
    var QWeb = core.qweb;
    var session = require('web.session');
    
    Menu.include({
        start: function () {
            var self = this;
            var def = this._super.apply(this, arguments);
            $('ul.o_menu_apps > li > a.full').bind('click', function(ev){
                ev.preventDefault();
                var $target = $('.o_menu_apps .dropdown .show');
                if ($target.length == 0){
                    self.on_load_badge();
                }                
            });
            return def
        },
        on_load_badge: function () {   
            var self = this;
            var badge_count = $('[id=menu_counter]')                
            if (badge_count.length > 0){
                $('[id=menu_counter]').remove();
            }
            _.each(this.menu_data.children, function (item) {
                var isEnterprise = odoo.session_info.server_version_info[5] === 'e';
                if (isEnterprise){
                    var $menu_item = $('.o_apps').find('a[data-menu-id="' + item['id'] +'"]')
                }else{
                    var $menu_item = $('.dropdown-menu').find('a[data-menu-id="' + item['id'] +'"]')
                }                
                var postData = new FormData();
                postData.append("menu_id", item['id']);
                if (core.csrf_token) {
                    postData.append('csrf_token', core.csrf_token);
                }
                var def = $.ajax({
                    type: "POST",
                    dataType: 'json',
                    url: '/get_badge_count',
                    cache: false,
                    contentType: false,
                    processData: false,
                    data: postData,                    
                }).then(function (count) {                    
                    $menu_item.append(QWeb.render("badge_on_menu_counter", {widget: count}));
                });
            })                         
        },        
    });
    return {
        'Menu': Menu,
    };
});