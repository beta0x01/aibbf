document.addEventListener("DOMContentLoaded", function () {
    const targetInput = document.getElementById("target");
    const uploadFileButton = document.getElementById("uploadFile");
    const fileInput = document.getElementById("fileInput");
    const startScanButton = document.getElementById("startScan");
    const statusElement = document.getElementById("status");

    let selectedFile = null;

    // File Upload Handling
    uploadFileButton.addEventListener("click", function () {
        fileInput.click();
    });

    fileInput.addEventListener("change", function (event) {
        selectedFile = event.target.files[0];
        if (selectedFile) {
            uploadFileButton.innerText = selectedFile.name;
        }
    });

    // Start Scan
    startScanButton.addEventListener("click", function () {
        let target = targetInput.value;
        let modules = getSelectedModules();

        if (!target && !selectedFile) {
            alert("Please enter a target or upload a file!");
            return;
        }

        let formData = new FormData();
        if (target) formData.append("target", target);
        if (selectedFile) formData.append("file", selectedFile);
        formData.append("modules", JSON.stringify(modules));

        fetch("/start_scan", {
            method: "POST",
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert("Error: " + data.error);
            } else {
                statusElement.innerText = "Scanning...";
                monitorScan(data.scan_id);
            }
        })
        .catch(error => console.error("Error:", error));
    });

    // Monitor Scan Progress
    function monitorScan(scanId) {
        let interval = setInterval(() => {
            fetch(`/get_results/${scanId}`)
                .then(response => response.json())
                .then(data => {
                    if (data.status === "Completed") {
                        statusElement.innerText = "Scan Completed!";
                        clearInterval(interval);
                        displayResults(data.results);
                    }
                })
                .catch(error => console.error("Error:", error));
        }, 5000);
    }

    // Display Results
    function displayResults(results) {
        let resultsContainer = document.getElementById("results");
        resultsContainer.innerHTML = "<h3>Results:</h3><pre>" + JSON.stringify(results, null, 2) + "</pre>";
    }

    // Get Selected Modules
    function getSelectedModules() {
        let selectedModules = [];
        document.querySelectorAll(".module-button.active").forEach(button => {
            selectedModules.push(button.getAttribute("data-module"));
        });
        return selectedModules;
    }

    // Toggle Module Selection
    document.querySelectorAll(".module-button").forEach(button => {
        button.addEventListener("click", function () {
            this.classList.toggle("active");
        });
    });
});
