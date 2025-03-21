const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_body");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");
/** delete buttons constants**/
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

/**
* Initializes edit functionality for the provided edit buttons.
* - For each button in the `editButtons` collection:
* - Retrieves the associated review's ID upon click.
* - Fetches the content of the corresponding review.
* - Populates the `commentText` input/textarea with
  - the review's content for editing.
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit_review/{reviewId}` endpoint.
*/
for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let reviewId = e.target.getAttribute("review_id");
    let reviewContent = document.getElementById(`review${reviewId}`).innerText;
    commentText.value = reviewContent;
    submitButton.innerText = "Update";
    commentForm.setAttribute("action", `edit/${reviewId}`);
  });
}


/**
* Initializes deletion functionality for the provided delete buttons.
* -For each button in the `deleteButtons` collection:
* - Retrieves the associated reviews's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the
* - deletion endpoint for the specific comment.
* - Displays a confirmation modal (`deleteModal`) to prompt
* - the user for confirmation before deletion.
*/
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      let reviewId = e.target.getAttribute("review_id");
      deleteConfirm.href = `delete_review/${reviewId}`;
      deleteModal.show();
    });
  }
