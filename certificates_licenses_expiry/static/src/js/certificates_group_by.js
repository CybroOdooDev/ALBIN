odoo.define("certificates_licenses_expiry.portal_certificates_group_by", function (require) {
    "use strict";
    var ajax = require('web.ajax');
    var core = require('web.core');
    var QWeb = core.qweb;

    $("#group_select_certificates").on('change', function () {
    var search_value = $("#group_select_certificates").val();
    ajax.jsonRpc('/certificatesgroupby', 'call', {
                'search_value': search_value,
            }).then(function(result) {
                $('.search_certificates').html(result);
                });
    })

})