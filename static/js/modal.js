$(document).ready(function () {
    // when the modal is shown
    $("#deleteConfirmModal").on("show.bs.modal", function (event) {
    const button = $(event.relatedTarget);
    const contactId = button.data("id");
    const deleteUrl = button.data("url");
    // update modal content 
    $("#modal-contact-id").text(contactId);
    // set the delete url 
    $("#confirmDeleteBtn").attr("href", deleteUrl);  
    });
    // when delete button is clicked
    $("#confirmDeleteBtn").click(function(e) {
        // close the modal
        $("#deleteConfirmModal").modal("hide");
        // add a short delay before redirecting to the delete view
        setTimeout(function() {
            window.location.href = $("#confirmDeleteBtn").attr("href");
        }, 500);
    })
})