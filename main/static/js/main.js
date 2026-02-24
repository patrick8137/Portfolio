function toggleMenu() {
    document.querySelector('.nav-links').classList.toggle('active');
}

setTimeout(function() {
    const msg = document.querySelector('.success-message');
    if (msg) {
        msg.style.display = 'none';
    }
}, 3000);