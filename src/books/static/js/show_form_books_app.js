document.getElementById("openModalButton").addEventListener("click", function() {
    document.getElementById("myModal").classList.remove("hidden");
});

document.getElementById("closeModalButton").addEventListener("click", function() {
    document.getElementById("myModal").classList.add("hidden");
});