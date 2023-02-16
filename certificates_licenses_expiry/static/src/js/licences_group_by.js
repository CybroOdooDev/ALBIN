odoo.define("certificates_licenses_expiry.portal_licences_group_by", function (require) {
    "use strict";
    var ajax = require('web.ajax');
    var core = require('web.core');
    var QWeb = core.qweb;

    $("#group_select_licences").on('change', function () {
    var search_value = $("#group_select_licences").val();
    ajax.jsonRpc('/licencesgroupby', 'call', {
                'search_value': search_value,
            }).then(function(result) {
                $('.search_licences').html(result);
                });
    })

})