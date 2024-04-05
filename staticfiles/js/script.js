const commentText = document.getElementById("id_body");
console.log(commentText);
const commentForm = document.getElementById("commentForm");
console.log(commentForm);
const submitButton = document.getElementById("submitButton");
console.log(submitButton);

const editButtons = document.querySelectorAll('.btn-edit');

for (let buttons of editButtons) {
    buttons.addEventListener('click', (e) => {
        const id = e.target.getAttribute('comment_id');
        const comment_id = document.getElementById("comment_id");
        console.log(comment_id);
    })

}