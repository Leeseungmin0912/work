function showAlert(team) {
    alert(team + " 홈페이지로 이동합니다.");
}

function showModal(teamName, teamInfo) {
    document.getElementById("modalTitle").innerText = teamName;
    document.getElementById("modalContent").innerText = teamInfo;
    document.getElementById("teamModal").style.display = "block";
}

function closeModal() {
    document.getElementById("teamModal").style.display = "none";
}
