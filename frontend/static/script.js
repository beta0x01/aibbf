let selectedModules = [];

function toggleModule(module) {
    if (selectedModules.includes(module)) {
        selectedModules = selectedModules.filter(m => m !== module);
    } else {
        selectedModules.push(module);
    }
}

function uploadFile() {
    let file = document.getElementById("fileUpload").files[0];
    let formData = new FormData();
    formData.append("file", file);

    fetch("/api/upload", { method: "POST", body: formData })
    .then(response => response.json())
    .then(data => {
        document.getElementById("target").value = data.domains.join(", ");
    });
}

function startScan() {
    let target = document.getElementById("target").value;
    if (!target) {
        alert("Please enter a target.");
        return;
    }

    fetch("/api/start_scan", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ target, modules: selectedModules })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("status").innerText = "Status: " + data.status;
    });
}
