function confirmDelete() {
    return confirm('are you sure you want to delete the game?');
}

document.addEventListener('DOMContentLoaded', function () {
    const messages = document.querySelector('.messages');
    if (messages) {
        setTimeout(() => { messages.style.display = 'none'; }, 5000);
    }
});