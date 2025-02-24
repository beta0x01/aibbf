$(document).ready(function () {
    let socket = io.connect("http://localhost:8088");

    socket.on("scan_update", function (data) {
        $("#status").append(`<div class="alert alert-warning">${data.message}</div>`);
    });

    socket.on("scan_complete", function (data) {
        $("#status").append(`<div class="alert alert-success">${data.message}</div>`);
        loadScanHistory();
    });

    function loadScanHistory() {
        $.get("/get_history", function (data) {
            $("#scan-history").html("");
            data.forEach(scan => {
                $("#scan-history").append(
                    `<tr>
                        <td>${scan.target}</td>
                        <td>${scan.modules}</td>
                        <td>${scan.status}</td>
                        <td><a href="${scan.result}" target="_blank">Download</a></td>
                    </tr>`
                );
            });
        });
    });
    let selectedModules = [];

    $(".module-btn").click(function () {
        let module = $(this).data("module");
        if (module === "all") {
            selectedModules = ["recon", "web", "cloud", "network", "exploitation"];
            $(".module-btn").removeClass("btn-outline-primary").addClass("btn-primary");
        } else {
            if (selectedModules.includes(module)) {
                selectedModules = selectedModules.filter(m => m !== module);
                $(this).removeClass("btn-primary").addClass("btn-outline-primary");
            } else {
                selectedModules.push(module);
                $(this).removeClass("btn-outline-primary").addClass("btn-primary");
            }
        }
    });

    $("#toggle-dark-mode").click(function () {
        $("body").toggleClass("dark-mode");
    });

    $("#start-scan").click(function () {
        let target = $("#target").val();
        if (!target) {
            alert("Please enter a target domain!");
            return;
        }

        $.post("/start_scan", { target: target, modules: selectedModules.join(",") }, function (data) {
            $("#status").html(`<span class="alert alert-success">Scan started for ${target}</span>`);
            loadScanHistory();
        });
    });

    function loadScanHistory() {
        $.get("/get_history", function (data) {
            $("#scan-history").html("");
            data.forEach(scan => {
                $("#scan-history").append(
                    `<tr>
                        <td>${scan.target}</td>
                        <td>${scan.modules}</td>
                        <td>${scan.status}</td>
                        <td><a href="${scan.result}" target="_blank">Download</a></td>
                    </tr>`
                );
            });
        });
    }
});
