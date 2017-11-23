
$(document).ready(function(){

    var form = $('.js-csv-upload-form');
    var infoSection = $('.js-backend-info');
    var controlOverride = $('.js-allow-override');
    var overrideCheckControl = $('.js-input-allow-override');

    form.submit(function(e){
        e.stopPropagation();
        e.preventDefault();
        var formData = new FormData(form[0]);

        $.ajax({
            type: 'POST',
            url: form.prop('action'),
            data: formData,
            contentType: false,
            cache: false,
            processData: false,
            async: false,
            success: function(data) {
                infoSection.html(tmpl('id-upload-success', {
                    count: data.created
                }));
                controlOverride.hide();
                overrideCheckControl.prop('checked', false);
            },
            error: function(data) {
                infoSection.html(tmpl('id-server-error-tmpl', {
                    errors: data.responseJSON.errors
                }));
                controlOverride.show();
            }
        });
    });
});
