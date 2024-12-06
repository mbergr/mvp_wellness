document.addEventListener('DOMContentLoaded', function() {
    // Handle notification dismissal
    const notifications = document.querySelectorAll('.notification .delete');
    notifications.forEach(button => {
        button.addEventListener('click', () => {
            button.parentElement.remove();
        });
    });

    // Handle mobile navigation menu
    const navbarBurgers = document.querySelectorAll('.navbar-burger');
    navbarBurgers.forEach(burger => {
        burger.addEventListener('click', () => {
            const targetId = burger.dataset.target;
            const targetMenu = document.getElementById(targetId);
            
            burger.classList.toggle('is-active');
            targetMenu.classList.toggle('is-active');
        });
    });

    // Enhance range input visualization
    const rangeInputs = document.querySelectorAll('input[type="range"]');
    rangeInputs.forEach(input => {
        input.addEventListener('input', function() {
            // Update the output value
            this.nextElementSibling.value = this.value;
            
            // Calculate the percentage for background styling
            const min = this.min ? parseInt(this.min) : 0;
            const max = this.max ? parseInt(this.max) : 100;
            const percentage = ((this.value - min) * 100) / (max - min);
            
            // Update input background
            this.style.background = `linear-gradient(to right, #00d1b2 ${percentage}%, #dbdbdb ${percentage}%)`;
        });
        
        // Trigger input event on load
        input.dispatchEvent(new Event('input'));
    });
});
