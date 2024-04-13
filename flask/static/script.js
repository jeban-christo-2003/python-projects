/* script.js */
document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.getElementById('login-form');
    const loginMessage = document.getElementById('login-message');

    loginForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;

        // Simple validation (replace with server-side validation)
        if (username.trim() === '' || password.trim() === '') {
            loginMessage.textContent = 'Please enter username and password.';
            return;
        }

        // Simulate login (replace with actual login logic)
        if (username === 'admin' && password === 'password') {
            loginMessage.textContent = 'Login successful. Redirecting...';
            setTimeout(function() {
                window.location.href = '/dashboard';
            }, 1000); // Redirect after 1 second
        } else {
            loginMessage.textContent = 'Invalid username or password.';
        }
    });
});
function loginForm(){
    
}