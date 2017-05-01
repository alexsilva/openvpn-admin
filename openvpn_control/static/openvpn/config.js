/**
 * Created by alex on 01/05/2017.
 */

vpn = {
    objects: [],
    activate_fn: function () {
    },
    update_ip_info: function (pk) {
        $.ajax(Urls.vpn_control_status(pk), {
            success: function (data) {
                $("#vpn-ip").html(data.current_ip)
            },
            error: function (data) {
                console.log(data)
            }
        });
    },
    button: function (pk) {
        var button = $("#vpn-activate-" + pk);
        button.click(function (event) {
            event.preventDefault();
            var $this = $(this);
            $this.button('loading');
            $.ajax(Urls.vpn_control_activate(pk), {
                success: function (data) {
                    console.log(data);
                    $(".btn-vpn").removeClass("btn-success")
                        .removeClass("disabled")
                        .addClass("btn-default")
                        .text("activate");
                    $this.removeClass("btn-default")
                        .addClass("btn-success")
                        .addClass("disabled");
                    $this.text(data.status);
                    vpn.update_ip_info(pk);
                },
                error: function (data) {
                    $this.button('reset');
                    console.log(data)
                }
            });
        });
    },
    exec: function () {
        var arrayLength = this.objects.length;
        for (var i = 0; i < arrayLength; i++) {
            this.button(this.objects[i])
        }
        vpn.activate_fn();
    }
};


$(document).ready(function () {
    vpn.exec();
});