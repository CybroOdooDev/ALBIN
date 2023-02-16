odoo.define("certificates_licenses_expiry.portal_my_licences", function (require) {
    "use strict";
    var ajax = require('web.ajax');
    var core = require('web.core');
    var QWeb = core.qweb;
     $("#search_licences").on('click', function (ev) {
    var search_value = $("#licences_search_box").val();
    ajax.jsonRpc('/licencesearch', 'call', {
                'search_value': search_value,
            }).then(function(result) {
                $('.search_licences').html(result);
                });
    })

})
