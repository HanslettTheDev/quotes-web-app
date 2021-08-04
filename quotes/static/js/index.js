const myModal = document.getElementById('mymodal');
const closeBtn = document.getElementById('closebtn');
const whatsNewBtn = document.getElementById('whats-new');

// Event listeners
closeBtn.addEventListener('click', closeModal);
whatsNewBtn.addEventListener('click', openModal);

function openModal() {
    myModal.style.display = 'block';
}

function closeModal() {
    myModal.style.display = 'none';
}