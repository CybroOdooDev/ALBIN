odoo.define("certificates_licenses_expiry.portal_my_certificates", function (require) {
    "use strict";
    var ajax = require('web.ajax');
    var core = require('web.core');
    var QWeb = core.qweb;
     $("#search_certificates").on('click', function (ev) {
    var search_value = $("#certificates_search_box").val();
    ajax.jsonRpc('/certificatesearch', 'call', {
                'search_value': search_value,
            }).then(function(result) {
                $('.search_certificates').html(result);
                });
    })

})
