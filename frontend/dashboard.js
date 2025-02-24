function startScan() {
    let target = document.getElementById("target").value;
    fetch("/start_scan", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ target: target, modules: ["All"] })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("status").innerText = "Status: Running...";
        checkStatus(data.session_id);
    });
}

function checkStatus(session_id) {
    fetch(`/scan_status/${session_id}`)
    .then(response => response.json())
    .then(data => {
        document.getElementById("status").innerText = "Status: " + data.status;
        if (data.status === "Running") {
            setTimeout(() => checkStatus(session_id), 3000);
        }
    });
}
